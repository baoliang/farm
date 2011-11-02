#coding: utf-8
from lib.store import find, insert, remove, update 
def create_info(collection, info, uid):
    info.update({'uid': uid})
    insert(collection, info)


def get_info_list(collection, query, page, limit): 
    lists = find(collection, query, page=page, limit=limit)
    return {
        'count': lists.count(),
        'lists': lists,
    }


def del_info(collection, query, real=False):
    remove(collection, query, real=real)


def update_info(collection, query, update_dic):
    update(collection, query, update_dic) 
