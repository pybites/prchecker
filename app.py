from bottle import (route, run, request,
                    static_file, jinja2_view)

from dates import NOW
from feedback import get_feedback
from ghapi import get_prs


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/')
@route('/<month>')
@jinja2_view('index.html')
def index(month=NOW.month):

    username = request.query.get('username') or None
    prs = None

    if username is not None:
        prs = get_prs(month, username)

    feedback = get_feedback(prs)

    return {'prs': prs,
            'username': username or '',
            'feedback': feedback}


run(host='localhost', port=8080, reloader=True)
