#coding: utf-8
mongo_host = '127.0.0.1'
mongo_port = 27017
mongo_name = 'farm_dev'
mysql_host = '127.0.0.1'
mysql_port = 3306
DEBUG = True
MAKO_DIR = 'templates'
PAGE_LIMIT = 10
# optional, if specified Mako will cache to this directory
MAKO_CACHEDIR = 'mako_temp'
# optional, if specified Mako will respect the cache size
MAKO_CACHESIZE = 500
DEFAULT_LIMIT = 30
#状态码
ST_CODE = {
    'norm': 0,
    'del': 1,
    'v': 2,
}
