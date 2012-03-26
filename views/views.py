# _*_ coding: utf-8 _*_
from flask import Blueprint 
import os
import simplejson
from service.info import get_info_list
from service.info import get_one_info
from service.info import del_info
from service.info import create_info
from dic import level_html, collection_html, args
from lib.utils import form2dic
from lib.utils import now, DatetimeJSONEncoder
from flaskext.mako import render_template
from lib.cach import get_cach, set_cach
from help.tools import set_page_session
from help.tools import get_query_page
from help.tools import get_query
from help.tools import get_query
from help.tools import get_city_by_id
import random
from flask import  session, request, make_response, redirect, jsonify as return_json
app = Blueprint('views', __name__)

@app.before_request
def before():
    if 'sid' not in session:

        session['sid'] = str(random.randint(10**10,10**20))
        
@app.teardown_request
def teardown_request(exception):
    session["path"] = request.path        
        
        
@app.route('/get_city')    
def get_city():
    return return_json(city_list=get_city_by_id(request.args.get('_id')))

    

@app.route('/render_to')
def render_to():
     return render_template(request.args.get('html'),
            info=eval(request.args.get('info', '{}')),
        )

@app.route('/create_info', methods=['GET', 'POST']) 
def create_info_action():
    _id = session.get('_id', None)
    if _id: 
        if request.form:     
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
    req = urllib2.Request("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=python&ip=" + ip)
    res = urllib2.urlopen( req )
    html = res.read()
    res.close()
    return html
    
@app.route('/sell/detail')
def detail_sell():
    return render_template(
        'sell/detail_sell.html',
        info=get_one_info('sell', {'_id': request.args.get('_id')})
      
    )   
    
   
@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    @todo:index page:
    '''
    pages = get_query_page(
        session.get('page', None),
        get_query(request.values, session.get('boot_time', now())),
        session.get('sid'),
        'news'
    )
    return_html = "index.html"
    if request.values.get("ajax", None): 
        return_html = "news/list.html"
    session.update(set_page_session(request.url, pages))
    return render_template(
        return_html,
        pages=pages,
        search_value=request.args.get('title','')
    ) 


@app.route('/send')
def send_sell():
    '''
    @todo:index page:
    '''

    return render_template('sell/send_sell.html')

   
    
