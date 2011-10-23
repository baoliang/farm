from lib.store import find_one, update, insert
from lib.utils import print_err
def vertify_user(uid, password,vertify_code = '' ):
 
    user = find_one('users', {'_id': uid})
    if user:
       if user.get('password', '') == password:
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
        insert('users' ,user)
        return True
    except:
        print_err() 
        return False


def update_user(id, info):
    update('users', {'_id': id}, {'$set': info})    
