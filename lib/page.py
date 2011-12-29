#coding= utf-8
from store import find
from datetime import datetime
from lib.utils import now
import settings_run
from lib.db import db
def get_page(
    collection,
    query={},
    limit=settings_run.DEFAULT_LIMIT, 
    page=1,
    page_last_id='0',
    page_last_time=now()):
    '''
    @todo:获取分页
    @params collection:集合名称
    @params query:查询
    @params page: 页数
    @params limit: 数据数量
    @return:
    '''        
    if  page == 1:
        collection_data = find(collection, query, limit=limit)
    else:
        query.update(
            {
                '$gte': {'create_time': page_last_time},
                '$get': {'_id': page_last_id},
            }
        )
        collection_data = find(collection, query, limit=limit) 
    count = collection_data.count()
    data = list(collection_data)
    length = len(data) 
    if length:        
        last_time = data[length - 1]['create_time']
        last_id = data[length - 1]['_id']      
    else:
        last_time = None
        last_id = None 
    return {
        'count': count,
        'data': data,
        'page': page,   
        'limit': limit,
        'last_time': last_time,
        'last_id': last_id
        
    }
    
    
