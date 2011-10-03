import settings_run
MG_HOST = settings_run.mongo_host
MG_PORT = settings_run.mongo_port
MG_READ_HOST = settings_run.mongo_host
MG_READ_PORT = settings_run.mongo_port


def get_db_update():
    _db = pymongo.Connection(MG_HOST, MG_PORT)[MG_NAME]
    return _db


def get_db_read():
    _db = pymongo.Connection(MG_READ_HOST, MG_READ_PORT)
    return _db


db_update = get_db()
db = get_db_read()


