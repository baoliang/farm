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
    
@app.route('/buy/detail')
def detail_buy():
    return render_template(
        'buy/detail_buy.html',
        info=get_one_info('buy', {'_id': request.args.get('_id')})
      
    )

@app.route('/news/detail')
def news_detail():
    '''
    @todo:index page:
    '''
    return render_template(
        'news/news_detail.html',
        news=get_one_info('news', {'_id': request.args.get('_id')})
    )    

@app.route('/teach/detail')
def teach_detail():
    '''
    @todo:index page:
    '''
    return render_template(
        'teach/teach_detail.html',
        info=get_one_info('teach', {'_id': request.args.get('_id')})
    )  
    
@app.route('/yellow_page/detail')
def yellow_page_detail():
    '''
    @todo:index page:
    '''
    return render_template(
        'yellow_page/yellow_page_detail.html',
        info=get_one_info('yellow_page', {'_id': request.args.get('_id')})
    )  

@app.route('/invest/detail')
def invest_detail():
    '''
    @todo:index page:
    '''
    return render_template(
        'invest/invest_detail.html',
        info=get_one_info('invest', {'_id': request.args.get('_id')})
    )     
    
@app.route('/collaborate/detail')
def collaborate_detail():
    '''
    @todo:index page:
    '''
    return render_template(
        'collaborate/collaborate_detail.html',
        info=get_one_info('collaborate', {'_id': request.args.get('_id')})
    )        

@app.route('/business/detail')
def business_detail():
    '''
    @todo:index page:
    '''
    return render_template(
        'business/business_detail.html',
        info=get_one_info('business', {'_id': request.args.get('_id')})
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


    
@app.route('/sell', methods=['GET', 'POST'])
def sell_index():
    pages = get_query_page(
        session.get('page', None),
        get_query(request.values, session.get('boot_time', now())),
        session.get('sid'),
        'sell'
    )
    return_html = "sell/index.html"
    if request.values.get("ajax", None): 
        return_html = "sell/list.html"

    session.update(set_page_session(request.url, pages))
    return render_template(
        return_html,
        pages = pages,
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1),
        search_value=request.args.get('title','')
        
    )     
    
@app.route('/buy', methods=['GET', 'POST'])
def buy_index():
    pages = get_query_page(
        session.get('page', None),
        get_query(request.values, session.get('boot_time', now())),
        session.get('sid'),
        'buy'
    )
    return_html = "buy/index.html"
    if request.values.get("ajax", None): 
        return_html = "buy/list.html"

    session.update(set_page_session(request.url, pages))
    return render_template(
        return_html,
        pages = pages,
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1),
        search_value=request.args.get('title','')
        
    )     

@app.route('/teach', methods=['GET', 'POST'])
def teach_index(): 
    pages = get_query_page(
        session.get('page', None),
        get_query(request.values, session.get('boot_time', now())),
        session.get('sid'),
        'teach'
    )
    return_html = "teach/index.html"
    if request.values.get("ajax", None): 
        return_html = "teach/list.html"
 
    
    session.update(set_page_session(request.url, pages))
    return render_template(
        return_html,
        pages = pages,
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1),
        search_value=request.args.get('title','')
        
    )  
    
@app.route('/business', methods=['GET', 'POST'])
def business_index(): 
    pages = get_query_page(
        session.get('page', None),
        get_query(request.values, session.get('boot_time', now())),
        session.get('sid'),
        'business'
    )
    return_html = "business/index.html"
    if request.values.get("ajax", None): 
        return_html = "business/list.html"
 
    
    session.update(set_page_session(request.url, pages))
    return render_template(
        return_html,
        pages = pages,
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1),
        search_value=request.args.get('title','')
        
    )  
    
@app.route('/collaborate', methods=['GET', 'POST'])
def collaborate_index(): 
    pages = get_query_page(
        session.get('page', None),
        get_query(request.values, session.get('boot_time', now())),
        session.get('sid'),
        'collaborate'
    )
    return_html = "collaborate/index.html"
    if request.values.get("ajax", None): 
        return_html = "collaborate/list.html"
 
    
    session.update(set_page_session(request.url, pages))
    return render_template(
        return_html,
        pages = pages,
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1),
        search_value=request.args.get('title','')
        
    )  
    
@app.route('/invest', methods=['GET', 'POST'])
def invest_index(): 
    pages = get_query_page(
        session.get('page', None),
        get_query(request.values, session.get('boot_time', now())),
        session.get('sid'),
        'invest'
    )
    return_html = "invest/index.html"
    if request.values.get("ajax", None): 
        return_html = "invest/list.html"
 
    
    session.update(set_page_session(request.url, pages))
    return render_template(
        return_html,
        pages = pages,
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1),
        search_value=request.args.get('title','')
        
    ) 
    
@app.route('/yellow_page', methods=['GET', 'POST'])
def yellow_page_index(): 
    pages = get_query_page(
        session.get('page', None),
        get_query(request.values, session.get('boot_time', now())),
        session.get('sid'),
        'yellow_page'
    )
    return_html = "yellow_page/index.html"
    if request.values.get("ajax", None): 
        return_html = "yellow_page/list.html"
 
    
    session.update(set_page_session(request.url, pages))
    return render_template(
        return_html,
        pages = pages,
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1),
        search_value=request.args.get('title','')
        
    )     
@app.route('/sell/send_sell')
def send_sell():
    '''
    @todo:index page:
    '''

    return render_template('sell/send_sell.html')

@app.route('/news/send_news')
def send_news():
    return render_template('news/send_news.html')

             
@app.route('/buy/send_buy')
def send_buy():
    '''
    @todo:index page:
    '''

    return render_template('buy/send_buy.html')
          
@app.route('/teach/send_teach')
def send_teach():
    '''
    @todo:index page:
    '''

    return render_template('teach/send_teach.html')
    
@app.route('/yellow_page/send_yellow_page')
def send_yellow_page():
    '''
    @todo:index page:
    '''
    return render_template('yellow_page/send.html')    
    
@app.route('/invest/send_invest')
def send_invest():
    '''
    @todo:index page:
    '''
    return render_template('invest/send.html')    
    
@app.route('/business/send_business')
def send_business():
    '''
    @todo:index page:
    '''
    return render_template('business/send.html')     

@app.route('/collaborate/send_collaborate')
def send_collaborate():
    '''
    @todo:index page:
    '''
    return render_template('collaborate/send.html')  
    
    