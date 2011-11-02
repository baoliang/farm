#coding: utf-8
from flaskext.mako import render_template
from flask import  session, request, make_response, redirect
from app import app
from service.account import vertify_user
from service.account import check_only_user
from service.account import update_user
from service.account import reg_user
from service.city import get_city_by_id
from service.info import get_info_list
from service.info import del_info
from service.info import create_info
from dic import level_html, collection_html, args
 


@app.before_request
def before_request():
    white_list = ['/login']
    if not session.get('_id', None) and  request.path != '/login':
        pass


@app.route('/admin')
def admin():
    return render_template('admin/login.html')


@app.route('/')
def index():
    '''
    @todo:index page:
    '''
    if not session.get('city', None) and session.get('_id', None):
        return render_template('list_city.html') 
    else:
        return render_template('index.html')


def find():
    '''
    @todo:find mongo collection
    '''
    pass


@app.route('/login', methods=['GET','POST'])
def login():
    '''
    @todo:登录
    '''
    user =  vertify_user(
        request.form.get('_id', ''),
        request.form.get('password', '')
    )
    if user:
        session['_id'] = request.form.get('_id')
        city = user.get('city', None)
        if city: 
            session['city'] = city 

            return render_template(level_html[user.get('level', '1')])
        else:
            return render_template('list_city.html')
    else:
        return render_template('login.html')
	

@app.route('/reg_user', methods=['POST', 'GET'])
def reg_user_by_form():
    '''
    @todo:注册用户
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
        _id =  session.get('_id', None)
        if _id:
            update_user(_id, {'city': city})
        return render_template('index.html')
    else:
        return render_template('list_city.html')


@app.route('/quit')
def quit():
    session['_id'] = None
    return render_template('index.html')


@app.route('/info_list')
def info_list():
    query = request.args.get('query', {})
    collection = request.args.get('collection', '')
    if query:
        query = eval(query)
    return render_template(
        collection_html.get(collection, '404.html'),
        info_list=get_info_list(
            collection,
            query,
            request.args.get('page','1'),
            request.args.get('limit', settings.PAGE_LIMIT),
    ))
    


@app.route('/create_info', methods=['GET', 'POST']) 
def create_info_action():
    _id = session.get('_id', None)
    if _id: 
        if request.form:
            create_info(request.form, _id)
            return render_template('info_list.html')
        else:
            return render_template('create_info.html')
    else:
        return render_template('login.html')


@app.route('/del_info')
def del_info_action():
    collection =  request.args.get('collection', '')
    real = request.args.get('_real', 'False')
    query = eval(request.args.get('query', '{}'))
    try:
        del_info(collection, query, real=real)   
        return '{success:true}'
    except:
        return '{success:false}' 

@app.route('/update_info')
def update_info_action():
    collection =  request.args.get('collection', '')
    query = eval(request.args.get('query', '{}'))
    udpate_dic = eval(request.args.get('update_dic', '{}'))
    try:
        update_info(collection, query, update_dic) 
        return '{success:true}'
    except:
        return '{success:false}'


