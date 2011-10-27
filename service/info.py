#coding: utf-8
from lib.store import find, insert 
def create_info(collection, info, uid):
    info.update({'uid': uid})
    insert(collection, info)


def get_info_list(collection, query, page, limit): 
    return find(collection, query, page=page, limit=limit)
