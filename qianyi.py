from lib.store import update
from lib.utils import now
from pymongo.objectid import ObjectId
for i in range(1000):
    update('news', {'create_time':{'$ne': 'a'}}, {'create_time': str(now())})
    update('users', {'create_time':{'$ne': 'a'}}, {'create_time': str(now())})
    update('sell', {'create_time':{'$ne': 'a'}}, {'create_time': str(now())})