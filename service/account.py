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
        user = update_loc(user.get("_id"))     
        insert('users', user)
        return user
    except:
        print_err() 
        return None


def update_user(_id, info):
    info = update_loc(_id) 
    update('users', {'_id': _id}, info)
   
    return find_one("users", {"_id": _id})
    
def update_loc(_id):
        user  = find_one("users", {"_id": _id})
        area_id = user.get('area_id', None)  
        user.update(
            {
                'province': find_one("city", {"_id": user.get('province_id')}).get("city_name")
            }
        )
        user.update(
            {
                'city': find_one("city", {"_id": user.get('city_id')}).get("city_name")
            }
        )

        if area_id:
            user.update(
                {
                    'area': find_one("city", {"_id": area_id}).get("city_name", '')
                }
            )
        user.pop("_id")
        return user
