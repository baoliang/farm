# _*_ coding: utf-8 _*_
from flask import Blueprint 
from service.account import vertify_user
from service.account import check_only_user
from service.account import update_user
from service.account import reg_user
from service.city import get_city_by_id
from service.info import get_info_list
from service.info import get_one_info
from service.info import del_info
from service.info import create_info
from service.file import save_file
from service.file import get_file
from lib.utils import form2dic
from lib.utils import now, DatetimeJSONEncoder
from help.tools import set_user_session
from flaskext.mako import render_template
from flask import  session, request, make_response, redirect, jsonify as return_json, send_file
account = Blueprint('account_view', __name__)
        
@account.route('/login', methods=['GET','POST'])
def login():
    '''
    @todo:登录
    '''
    user =  vertify_user(
        request.form.get('id', ''),
        request.form.get('password', '')
    )
    if user:
        session.update(set_user_session({}, user))
        session.permanent = True
        return redirect(request.headers.get("Referer", "/"))
    else:
        session['err_msg'] = u"帐号密码错误"
        if request.form.get("return", None):
            return render_template('login.html',login="login",  info=u"帐号密码错误")
        else:
            return redirect(request.headers.get("Referer", "/"))
	
@account.route('/login_user', methods=['GET','POST'])
def login_user():
    '''
    @todo:登录
    '''
    return render_template('login.html', login="login", info="")
            
            
@account.route('/reg_user', methods=['POST', 'GET'])
def reg_user_by_form():
    '''
    @todo:注册用户
    '''
    res = reg_user(form2dic(request.form)) 
    if res:
        session.update(set_user_session({}, res))
        return redirect('/')
    else:
       return render_template('info.html', info=u"服务器错误")


@account.route('/reg')
def reg():
    return render_template(
        'reg.html',
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1)
    )

@account.route('/setting')
def settings():
    if session.get('id', None):
        return render_template(
            'setting.html',
            user=get_one_info("users", {'id': session.get('id', None)}),
            provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
            city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1)
        )
    else:
        return redirect('/')    
    
    
@account.route('/update_user', methods=['POST', 'GET'])
def update_user_action():
    _id = session.get('id', None)
    if _id:
        user = form2dic(request.form)
        user.pop('password')
        user = update_user(_id, user)
        session.clear()
        session.update(set_user_session({}, user))
        return redirect('/')  
    else:
        return redirect('/')       

@account.route('/quit')
def quit():
    session.clear()
    return redirect(request.headers.get("Referer", "/"))
 
@account.route('/check_user')    
def check_user():
    return return_json(success = check_only_user(request.args.get('id', '')))

@account.route('/upload_file', methods=['POST'])    
def upload_file():
    if request.values.get("dir", "") == "image":
            
        file = request.files['imgFile']
        _id = save_file(
            file.stream,
            file.content_type,
            file.filename
        )
        
    return return_json({
        "error" : 0,
        "url" : "/file?_id=" + str(_id)
    })  
    
@account.route('/file')    
def getfile():
    file = get_file(request.args.get("_id"))
    response = make_response(file["content"])
    response.headers["Content-type"] = "text/plain"
    return response
