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
from lib.cach import get_cach, set_cach
news = Blueprint('news_view', __name__)


@news.route('/')
def index():
    '''
    @todo:index page:
    '''
    print '______king_'
    print request.cookies['session']
    query = form2dic(request.args)
    query.update({'boot_time': session.get('boot_time', now())})
    content = query.get('content', None)
    title = query.get('title', None)
    search_value = ""
    if content or content == "":
       search_value = content
       query.update({"content":{"$regex": content}})
    if title or title == "":
        query.update({"title":{"$regex": title}})
    if session.get('page', None) or query.get('page', 1) == 1 or query.get('page', 1)  >=   query.get('old_page', 1):
        pages = get_info_list(
            'news', 
            query=query
        ) 
       
    else:
        pages =  get_cach('pages')
    session.update(
        {
            'url': request.url,
            'boot_time': pages.get('boot_time'),
         
            'page':   pages.get('page'),
        }
    )
    set_cach('pages', pages)
    return render_template('index.html', pages=pages, search_value=search_value) 

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
    