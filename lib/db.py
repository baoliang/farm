import settings_run as settings
import pymongo
MG_HOST = settings.mongo_host
MG_PORT = settings.mongo_port
MG_READ_HOST = settings.mongo_host
MG_READ_PORT = settings.mongo_port
MG_NAME = settings.mongo_name

def get_db_update():
    _db = pymongo.Connection(MG_HOST, MG_PORT)[MG_NAME]
    return _db


def get_db_read():
    _db = pymongo.Connection(MG_READ_HOST, MG_READ_PORT)
    return _db


db_update = get_db_update()
db = get_db_read()


