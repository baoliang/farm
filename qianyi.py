from lib.store import update
from lib.utils import now
for i in range(100):
    update('news', {'_id':{'$ne': 'a'}}, {'create_time': str(now())})
    update('city', {'_id':{'$ne': 'a'}}, {'create_time': str(now())})
    update('users', {'_id':{'$ne': 'a'}}, {'create_time': str(now())})
    update('sell', {'_id':{'$ne': 'a'}}, {'create_time': str(now())})