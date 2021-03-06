#coding: utf-8
from lib.store import find, find_one, insert, remove, update 
from lib.page import  get_page
import settings_run
def create_info(collection, info, _id):
    info.update({'uid': _id})
    insert(collection, info)


def get_info_list(collection, query={}, limit=settings_run.DEFAULT_LIMIT, return_type = "page", sort=-1): 
    if return_type == "page":
        return get_page(collection, query=query, limit=settings_run.PAGE_LIMIT)
    else:
        return find(collection, query=query, sort=sort);
        
def get_one_info(collection, query={}): 
    return find_one(collection, query=query);

def del_info(collection, query, real=False):
    remove(collection, query, real=real)


def update_info(collection, query, update_dic):
    update(collection, query, update_dic) 
