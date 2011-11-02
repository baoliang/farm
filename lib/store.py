from lib.db import db_update, db
import datetime
def update(collection, query, data_dic):
    db_update[collection].update(query, data_dic, upsert=True, safe=True )

def insert(collection, data):
    data.update({'date': datetime.datetime.now()})
    db_update[collection].insert(data)
def remove(collection, query, real=False):
    if real:
        db_update[collection].remove(query)
    else:
        db_update[collection].update(query, {'set': {'del': True}})

def find(collection, query, page=0, limit=0):
    return db[collection].find(query).skip(page*limit).limit(limit)
    

def find_one(collection, query):
    return db[collection].find_one(query)
    
