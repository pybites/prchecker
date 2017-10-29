import calendar
from collections import namedtuple
from datetime import datetime
import os
import sys

from github import Github

GH_USER = os.environ.get('GH_USER')
GH_PW = os.environ.get('GH_PW')
if not GH_USER or not GH_PW:
    print('Please set GH_USER and GH_PW env vars')
    sys.exit(1)

REPO = 'pybites/challenges'

gh = Github(GH_USER, GH_PW)

Pr = namedtuple('Pr', 'user url title feedback created')


def _get_date_range():
    now = datetime.now()
    _, end_day = calendar.monthrange(now.year, now.month)
    yymm = '{}-{}-'.format(now.year, str(now.month).zfill(2))
    return '{0}01..{0}{1}'.format(yymm, end_day)


def get_open_challenges_prs():
    prs = []
    for pr in gh.get_repo(REPO).get_pulls('open'):
        if pr.body:
            body = '\n'.join(pr.body.split('\n')[2:-3])
        else:
            body = ''
        prs.append(Pr(user=pr.user,
                      url=pr.html_url,
                      title=pr.title,
                      feedback=body,
                      created=pr.created_at))
    return prs


def get_prs_user(username):
    created = _get_date_range()
    prs = []
    for pr in gh.search_issues('',
                               author=username,
                               type='pr',
                               created=created):
        prs.append(Pr(user=pr.user,
                      url=pr.html_url,
                      title=pr.title,
                      feedback=pr.body,
                      created=pr.created_at))
    return prs
