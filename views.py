# _*_ coding: utf-8 _*_
from flaskext.mako import render_template
from flask import  session, request, make_response, redirect, jsonify as return_json
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
from lib.utils import form2dic
from lib.utils import now

@app.before_request
def before_request():
    white_list = ['/login']
    #if not session.get('_id', None) and  request.path != '/login':
    pass


@app.route('/admin')
def admin():
    return render_template('admin/login.html')


@app.route('/sell')
def sell():
    return render_template('sell.html', sells=[])


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/')
def index():
    '''
    @todo:index page:
    '''
    query = form2dic(request.args)
    query.update({'last_time': session.get('last_time', now())})
    if (int(session.get('pages', {'page': 1}).get('page', 1)) == int(query.get('page', 1))) and  int(query.get('page', 1)) !=1:  
        print query.get('page')
        print 'dddd'
        pages = session['pages']
    else:
        print query
        pages = get_info_list(
            'news', 
            query=query,
            
        ) 
    session.update({
        'last_time': pages.get('last_time', now()),
        'pages': pages   
    })
    
    return render_template('index.html', pages=pages) 

@app.route('/user')
def user():
    '''
    @todo:index page:
    '''

    return render_template('user.html')


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
        session['_id'] = user.get('_id', None)
        session['name'] = user.get('name', None)
        return redirect('/')
    else:
        session['err_msg'] = u"帐号密码错误"
        return redirect('/')
	

@app.route('/reg_user', methods=['POST', 'GET'])
def reg_user_by_form():
    '''
    @todo:注册用户
    '''
    res = reg_user(form2dic(request.form)) 
    if res:
        session['_id'] = request.form['_id']
        session['name'] = request.form['name']
        return redirect('/')
    else:
       return render_template('error.html', name="服务器错误")

	
@app.route('/reg')
def reg():
    
    return render_template(
        'reg.html',
        provice_list=get_info_list("city", query={'f_id': "0"}, return_type = "list")
    )

    
@app.route('/setting')
def settings():
    return render_template('setting.html')
    

@app.route('/check_user')    
def check_user():
    return return_json(success = check_only_user(request.args.get('_id', '')))

    
@app.route('/get_city')    
def get_city():
    city  = get_info_list('city', query={"f_id": request.args.get("_id")}
    return return_json(city)

    

@app.route('/post_info')
def post_info():
    create_info(request.form, session['_id']) 


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
    session.clear()
    return redirect('/')


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
            print request.form
            create_info(request.form['collection'], form2dic(request.form), _id)
            return redirect(request.form['return'])
        else:
            return redirect('/')
    else:
        return redirect('/')


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

        
@app.route('/get_loc_by_ip')
def get_loc_by_ip():
    import urllib2
    ip = request.remote_addr
    if ip == "127.0.0.1": 
        ip = request.headers["X-Real-IP"]
    req = urllib2.Request("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=python&ip="+ip)
    res = urllib2.urlopen( req )
    html = res.read()
    res.close()
    
    return html

     
