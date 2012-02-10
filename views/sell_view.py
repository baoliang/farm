# _*_ coding: utf-8 _*_
from flask import Blueprint 
from service.info import get_info_list
from service.info import get_one_info
from service.info import del_info
from service.info import create_info
from dic import level_html, collection_html, args
from lib.utils import form2dic
from lib.utils import now, DatetimeJSONEncoder
from flaskext.mako import render_template
from flask import  session, request, make_response, redirect, jsonify as return_json
sell = Blueprint('sell_view', __name__)


@sell.route('/sell')
def sell_index():
    query = form2dic(request.args)
    query.update({'last_time': session.get('last_time', now())})
    pages = get_info_list(
        'sell', 
        query=query
        
    ) 
    session['url'] = request.url
    session['last_time'] = pages.get('last_time')

    return render_template(
        'sell/index.html',
        pages = pages,
        provice_list = get_info_list("city", query={'f_id': "0"}, return_type = "list", sort=1),
        city_list = get_info_list("city", query={'f_id': "35"}, return_type = "list", sort=1)
    )     
    
@sell.route('/sell/send_sell')
def send_sell():
    '''
    @todo:index page:
    '''

    return render_template('sell/send_sell.html')
    