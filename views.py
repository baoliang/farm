from flaskext.mako import render_template
from flask import  session, request, make_response
from app import app
from service.account import vertify_user
from service.account import check_only_user
@app.route('/')
def index():
    '''
    @todo:index page:
    '''

    print session.get('city')
    if session.get('city', None):
        print session.get('city')
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
        request.form.get('uid', ''),
        request.form.get('pass', '')
    )
    if res:
        session['id'] = request.form.get('uid')
        return 'True'
    else:
        return 'False'
   

@app.route('/login')
def login():
    if vertify_user(
        request.args.get('uid', ''),
        request.args.get('password')
    ):
        session['uid'] = request.args.get('uid')
    
        return render_template('index.html')
    else:
        return render_template('login.html')
	

@app.route('/reg')
def reg():
	return render_template('reg.html')
	
	
@app.route('/reg_user')
def reg_user():
    '''
    '''
    res = reg_user(request.form) 
    if res:
       session['uid'] = request.form.get('uid')
       return render_template('index.html', {'_id': request.form.get('_id', '')})
    else:
       return render_template('reg.html', {'_id': request.form.get('_id', '')})

	
@app.route('/reg')
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
        update_user({'city': city})
        return render_template('index.html')
    else:
        return render_template('list_city.html')
