from bottle import (route, run, request,
                    static_file, jinja2_view)

from dates import NOW, MONTH_INT_TO_NAME
from header import get_header
from ghapi import get_challenges_prs, get_prs_user


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/')
@route('/<month>')
@jinja2_view('index.html')
def index(month=NOW.month):
    try:
        month_name = MONTH_INT_TO_NAME[month]
    except:
        month_name = MONTH_INT_TO_NAME[NOW.month]

    header = 'Challenge PRs for {} {}'.format(month_name,
                                              NOW.year)

    prs = get_challenges_prs(NOW.year, month)

    return {'prs': prs,
            'header': header}


@route('/user')
@route('/user/<month>')
@jinja2_view('index.html')
def user(month=NOW.month):

    username = request.query.get('username') or None
    prs = None

    if username is not None:
        prs = get_prs_user(month, username)

    header = get_header(prs)

    return {'prs': prs,
            'username': username or '',
            'header': header}


run(host='localhost', port=8080, reloader=True)
