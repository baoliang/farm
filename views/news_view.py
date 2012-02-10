# _*_ coding: utf-8 _*_
from flask import Blueprint 
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
news = Blueprint('news_view', __name__)


@news.route('/')
def index():
    '''
    @todo:index page:
    '''
    query = form2dic(request.args)
    query.update({'last_time': session.get('last_time', now())})
    content = query.get('content', '.*')
    title = query.get('title', '.*')
    if query.has_key('content'):
        pass
    pages = get_info_list(
        'news', 
        query=query
        
    ) 
    session['url'] = request.url
    session['last_time'] = pages.get('last_time')

    return render_template('index.html', pages=pages) 

@news.route('/news/send_news')
def send_news():
    return render_template('news/send_news.html')

@news.route('/news/detail')
def news_detail():
    '''
    @todo:index page:
    '''
    return render_template(
        'news/news_detail.html',
        news=get_one_info('news', {'_id': request.args.get('_id')})
    )    
    