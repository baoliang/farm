from lib.store import find_one, update, insert
def get_cach(key):
        return find_one('cach', {'id': key})
def set_cach(key, data):
    if find_one('cach', {'id': key}):
        update('cach', {'id': key}, data)
    else:
        data['id'] =  key
        insert('cach', data)
        
