from bottle import route, run, request, static_file, view
from github import GithubException

from header import get_header
from ghapi import get_open_challenges_prs, get_prs_user


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/')
@view('index')
def index():
    try:
        prs = get_open_challenges_prs()
    except GithubException as exc:
        print(exc)
        prs = []

    return {'prs': prs,
            'header': None}


@route('/', method='POST')
@route('/<username>')
@view('index')
def user(username=None):
    prs = []

    if username is None:
        username = request.forms.get('username') or None

    if username is not None:
        try:
            prs = get_prs_user(username)
        except GithubException as exc:
            print(exc)
            prs = []

    header = get_header(prs)

    return {'prs': prs,
            'header': header}


run(host='localhost', port=8080, reloader=True)
