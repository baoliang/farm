import settings_run as settings
import pymongo
MG_HOST = settings.MONGO_HOST
MG_PORT = settings.MONGO_PORT
MG_READ_HOST = settings.MONGO_HOST
MG_READ_PORT = settings.MONGO_PORT
MG_NAME = settings.DB_NAME

def get_db_update():
    _db = pymongo.Connection(MG_HOST, MG_PORT)[MG_NAME]
    return _db


def get_db_read():
    _db = pymongo.Connection(MG_READ_HOST, MG_READ_PORT)[MG_NAME]
    return _db


db_update = get_db_update()
db = get_db_read()


