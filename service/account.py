from lib.store import find_one, update, insert
from lib.utils import print_err
def vertify_user(uid, password, collection='users' ,vertify_code = '' ):
 
    user = find_one(collection, {'_id': uid})
    if user:
       if user.get('password', '') == password:
          return user
       else:
          return False    
    else:
        return False
	
	
def check_only_user(_id):
    if find_one('users', {'_id': _id}):
        return False
    else:
        return True


def reg_user(user):
    try:
        print user
        insert('users' ,user)
        return True
    except:
        print_err() 
        return False


def update_user(id, info):
    update('users', {'_id': id}, {'$set': info})    
