#coding: utf-8
from lib.store import find, insert, remove, update 
from lib.page import  get_page
import settings_run
def create_info(collection, info, _id):
    info.update({'uid': _id})
    insert(collection, info)


def get_info_list(collection, query={}, limit=settings_run.DEFAULT_LIMIT): 
    return get_page(collection, query=query, limit=settings_run.PAGE_LIMIT)


def del_info(collection, query, real=False):
    remove(collection, query, real=real)


def update_info(collection, query, update_dic):
    update(collection, query, update_dic) 
