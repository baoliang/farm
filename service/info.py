#coding: utf-8
from lib.db import db, db_update 
def create_info(info, uid):
    info['uid'] = uid
    db_update.info.insert(info)
