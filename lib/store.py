from lib.db import db_update, db

def update(collection, query, data, type='mongo'):
    db_update[collection].update(query, data, upsert=True )

def insert(data):
    db_update[collection].insert(data)

def remove(collection, query, real=False):
    if real:
        db_update[collection].remove(query)
    else:
        db_update[collection].update(query, {'set': 'del': True})


def find(collection, query):
    db[collection].find()
    

def find_one(collection, query):
    return db[collection].find_one(query)
    
