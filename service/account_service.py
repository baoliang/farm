from service.crud_mongo import find_one_collection


def vertify_user(uid, password,vertify_code = '' ):
 
    user = find_one_collection('users', {'_id': uid})
    if user:
       if user.get('pass', '') == password:
          return True
       else:
          return False    
    else:
        return False
	
	
def check_only_user(uid):
    if find_one_collection('users', {'_id': uid}):
        return False
    else:
        return True
