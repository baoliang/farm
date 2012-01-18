from lib.db import db_update, db
import datetime
import settings_run
def update(collection, query, data_dic):
    db_update[collection].update(query, data_dic, upsert=True, safe=True )

def insert(collection, data, st_code=settings_run.ST_CODE['norm']):
    data.update({'create_time': datetime.datetime.now()})
    data.update({'st_code': st_code})
    db_update[collection].insert(data)
    
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


def find(collection, query={}, limit=0):
    query.update({'st_code': settings_run.ST_CODE['norm']})
    return db[collection].find(query).limit(limit)


def find_one(collection, query={}):
    return db[collection].find_one(query)
    
