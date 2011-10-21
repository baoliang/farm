from lib.store import find_one
from lib.db import db, db_update

def vertify_user(uid, password,vertify_code = '' ):
 
    user = find_one('users', {'_id': uid})
    if user:
       if user.get('pass', '') == password:
          return True
       else:
          return False    
    else:
        return False
	
	
def check_only_user(uid):
    if find_one('users', {'_id': uid}):
        return False
    else:
        return True


def reg_user(user):
    try:
        db_update.users.insert(user)
        return True
    except:
        return False


