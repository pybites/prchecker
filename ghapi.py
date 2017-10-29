import os
import sys

from github import Github

from dates import get_date_range

GH_USER = os.environ.get('GH_USER')
GH_PW = os.environ.get('GH_PW')
if not GH_USER or not GH_PW:
    print('Please set GH_USER and GH_PW env vars')
    sys.exit(1)

REPO = 'pybites/challenges'
gh = Github(GH_USER, GH_PW)


def get_challenges_prs(year, month):
    prs = []
    for pr in gh.get_repo(REPO).get_pulls('all'):
        if pr.created_at.year != year and pr.created_at.month != month:
            continue
        prs.append(pr)
    return prs


def get_prs_user(month, username):
    created = get_date_range(month)

    prs = gh.search_issues('',
                           author=username,
                           type='pr',
                           created=created)
    return prs
