#coding: utf-8
from flaskext.mako import render_template
from flask import  session, request, make_response
from app import app
from service.account import vertify_user
from service.account import check_only_user
from service.account import update_user
from service.account import reg_user
from service.city import get_city_by_id
@app.route('/')
def index():
    '''
    @todo:index page:
    '''
    if session.get('city', None):
        return render_template('index.html') 
    else:
        return render_template('list_city.html')


def find():
    '''
    @todo:find mongo collection
    '''
    pass


@app.route('/login_user')
def login_user():
    '''
    @todo: login user
    '''
    res = vertify_user(
        request.form.get('_id', ''),
        request.form.get('pass', '')
    )
    if res:
        session['id'] = request.form.get('_id')
        return 'True'
    else:
        return 'False'
   

@app.route('/login', methods=['GET','POST'])
def login():
    if vertify_user(
        request.form.get('_id', ''),
        request.form.get('password', '')
    ):
        session['_id'] = request.form.get('_id')
    
        return render_template('index.html')
    else:
        return render_template('login.html')
	

@app.route('/reg_user', methods=['POST', 'GET'])
def reg_user_by_form():
    '''
    '''
    res = reg_user(request.form) 
    if res:
       session['uid'] = request.form.get('_id')
       return render_template('index.html', name={'_id': request.form.get('_id', '')})
    else:
       return render_template('reg.html', name="错误")

	
@app.route('/reg')
def reg():
    return render_template('reg.html')


@app.route('/check_user')    
def check_user():
    if check_only_user(request.args.get('uid', '')):
        return 'True'
    else:
        return 'False'


@app.route('/post_info')
def post_info():
    create_info(request.form, session['uid']) 


@app.route('/list_city')
def list_city():
    return render_template('list_city.html')
    

@app.route('/catalog')
def catalog():
    city = request.args.get('city', None)
    if city:
        session['city'] = city
        id =  session.get('id', None)
        if id:
            update_user(id, {'city': city})
        return render_template('index.html')
    else:
        return render_template('list_city.html')


@app.route('/quit')
def quit():
    session['_id'] = None
    return render_template('index.html')
