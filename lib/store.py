from lib.db import db_update, db
import pymongo
from pymongo.objectid import ObjectId
import datetime
import settings_run
def update(collection, query, data_dic):
    db_update[collection].update(query, data_dic, upsert=True, safe=True )

def insert(collection, data, st_code=settings_run.ST_CODE['norm']):
    data.update({'create_time': datetime.datetime.now()})
    data.update({'st_code': st_code})
    db_update[collection].insert(data, safe=True)
    
def remove(collection, query={}, real=False):
    if real:
        db_update[collection].remove(query, safe=True)
    else:
        db_update[collection].update(
            query, 
            {
                'set':
                {
                    'st_code': settings_run.ST_CODE['del']
                }
            }
        )


def find(collection, query={}, limit=0, sort=-1, return_type="list"):
    query.update({'st_code': settings_run.ST_CODE['norm']})
    result = db[collection].find(query).sort('create_time', sort).limit(limit)
    if return_type == "cusor":
        return result
    else:
        return list(result)


def find_one(collection, query={}):
    if query.has_key('_id')  and collection not in ['users', 'city']:
        query.update({'_id': ObjectId(query.get('_id'))})
    return db[collection].find_one(query)
    
