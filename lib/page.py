#coding= utf-8
from store import find
from datetime import datetime
from lib.utils import now
import settings_run
import time
from lib.db import db
def get_page(
    collection,
    query={},
    limit=settings_run.DEFAULT_LIMIT
    ):
    '''
    @todo:获取分页
    @params collection:集合名称
    @params query:查询
    @params page: 页数
    @params limit: 数据数量
    @return:
    '''        
    page = int(query.get('page', 1))  
    if page == 1: query  = {}
    if (int(query.get('old_page', 1)) >= int(query.get('page', 1))):
        query_type = '$lt'
    else:
        query_type = '$gt'
    query.update(
        {
            'create_time': {
                query_type: (
                    query.get('last_time', now())
                )
            },
        }
    )
    if query.has_key('page'): query.pop('page')
    if query.has_key('old_page'): query.pop('old_page')
    if query.has_key('last_time'): query.pop('last_time')
    collection_data = find(collection, query, limit=limit)
    data = list(collection_data)
    length = len(data)
    if length:        
        last_time = data[length - 1]['create_time']
    else:
        last_time = None
    
    if query.has_key('create_time'): query.pop('create_time')
    return {
        'count': find(collection, query).count(),
        'data': data,
        'page': page,   
        'limit': limit,
        'last_time': last_time,
    }
    
    
