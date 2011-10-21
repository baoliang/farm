from lib.db import db_update, db

def update(query, data, collection, type='mongo'):
    
    db_update[collection].update(query, data )


def del_collection(collection):
    db_update[collection].remove()


def find_collection(collection, query):
    db[collection].find()
    

def find_one(collection, query):
    return db[collection].find_one(query)
    
