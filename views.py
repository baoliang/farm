from flaskext.mako import render_template
from flask import  session, request, make_response
from app import app
from service.account_service import vertify_user
@app.route('/')
def index():
    '''
    @todo:index page:
    '''
    return render_template('index.html')


def find():
    '''
    @todo:find mongo collection
    '''
    pass


@app.route('/login')
def login():
    '''
    @todo: login user
    '''
    res = vertify_user(
        request.form.get('uid', ''),
        request.form.get('pass', '')
    )
    if res:
        session['id'] = request.form.get('uid')
        make_response('true')
    else:
        make_response('false')
   
