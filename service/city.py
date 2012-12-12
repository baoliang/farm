#coding:utf-8
from lib.store import find_one

def get_city_by_id(id):
    return find_one('city', {'id': id})
