# _*_ coding: utf-8 _*_
"""
@todo: 存储层方法
"""
from lib.db import db_update, db, get_gridfs
from pymongo.objectid import ObjectId
import datetime
import settings_run

def update(collection, query, data_dic):
    """
    @todo: 更新数据
    @param collection: 集合名称
    @param query: 更新条件
    """
    if query.has_key("_id"):
        query["_id"] = ObjectId(str(query["_id"]))
 
    db_update[collection].update(query, {'$set': data_dic}, safe=True )

def insert(collection, data, st_code=settings_run.ST_CODE['norm']):
    """
    @todo: 添加数据
    @param collection: 集合名称
    @param data: 添加的数据
    @param st_code: 状态码
    """
    data.update({'create_time': str(datetime.datetime.now())})
    data.update({'st_code': st_code})
    return  db_update[collection].insert(data, safe=True)
    
def remove(collection, query={}, real=False):
    """
    @todo: 删除数据
    @param collection: 集合名称
    @param query:条件
    @param real: 是否物理删除
    """
    if real:
        db_update[collection].remove(query, safe=True)
    else:
        db_update[collection].update(
            query, 
            {
                '$set':
                {
                    'st_code': settings_run.ST_CODE['del']
                }
            }
        )


def find(collection, query={}, limit=0, sort=-1, return_type="list"):
    """
    @todo: 查询数据
    @param collection: 集合名称
    @param query: 查询条件
    @param limit: 返回条数
    @param sort: 正序逆序
    @param return_type: 返回类型
    """
    query.update({'st_code': settings_run.ST_CODE['norm']})
    result = db[collection].find(query).sort('create_time', sort).limit(limit)
    if settings_run.DEBUG:
        print query
    if return_type == "cusor":
        return result
    else:
        return list(result)

def find_one(collection, query={}):
    """
    @todo: 获取一条数据
    @param collection: 集合名称
    @param query: 查询条件
    """
    if query.has_key('_id'):
        query.update({'_id': ObjectId(query.get('_id'))})
    return db[collection].find_one(query)
    
def add_file(file_obj, content_type, filename):
    """
    @todo: 添加文件
    @param file_obj: 文件
    @param content_type: 文件类型
    @param filename: 文件名称
    """
    res = get_gridfs().put(
        file_obj,
        content_type=content_type,
        filename=filename
    )
    return  res
   
def get_file_by_id(_id):
    """
    @todo:根据文件ID获取文件
    @param _id: 文件ID
    """
    file_obj = get_gridfs().get(ObjectId(_id))
    return  {"content":file_obj.read()}
   
