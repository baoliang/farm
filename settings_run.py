# _*_ coding: utf-8 _*_
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
DB_NAME = "farm_dev"
PAGE_LIMIT = 100
DEFAULT_LIMIT = 10
DEBUG = False
#状态码
ST_CODE = {
    'norm': 0,
    'del': 1,
    'v': 2,
}
# one or more directories
MAKO_DIR = 'templates'
# optional, if specified Mako will cache to this directory
MAKO_CACHEDIR = '/tmp/mako'
# optional, if specified Mako will respect the cache size
MAKO_CACHESIZE = 500
