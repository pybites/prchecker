from bottle import route, run, request, static_file, view

from header import get_header
from ghapi import get_open_challenges_prs, get_prs_user


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/')
@view('index')
def index():
    prs = get_open_challenges_prs()
    return {'prs': prs}


@route('/user', method='POST')
@view('index')
def user():

    username = request.forms.get('username') or None
    prs = None

    if username is not None:
        prs = get_prs_user(username)

    header = get_header(prs)

    return {'prs': prs,
            'header': header}


run(host='localhost', port=8080, reloader=True)
