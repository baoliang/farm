# _*_ coding: utf-8 _*_
from flask import Blueprint 
import simplejson
from service.city import get_city_by_id
from service.info import get_info_list
from service.info import get_one_info
from service.info import del_info
from service.info import create_info
from dic import level_html, collection_html, args
from lib.utils import form2dic
from lib.utils import now, DatetimeJSONEncoder
from flaskext.mako import render_template
from flask import  session, request, make_response, redirect, jsonify as return_json
app = Blueprint('views', __name__)
    
@app.route('/get_city')    
def get_city():
    _id = request.args.get('_id')
    if _id in ["1", "2", "9"]:
        _id  = get_one_info(
                'city',
                query={"f_id": _id}
        ).get("_id") 
 
    city_list = get_info_list(
        'city',
        query={"f_id": _id},
        return_type = "list",
        sort=1
    )
    
    return return_json(city_list=simplejson.dumps(city_list, cls=DatetimeJSONEncoder))

    

@app.route('/render_to')
def render_to():
        return render_template(request.args.get('html'),
            info=eval(request.args.get('info')),
        )

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
    
    

     
