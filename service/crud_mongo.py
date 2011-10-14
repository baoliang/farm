from lib.db import db_update, db

def update_collecotion(json, collection):
    db_update[collection].update(json, )


def del_collection(collection):
    db_update[collection].remove()


def find_collection(collection, query):
    db[collection].find()
    

def find_one_collection(collection, query):
    return db[collection].find_one(query)
    
