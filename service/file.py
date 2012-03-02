from lib.store import add_file, get_file_by_id

def save_file(file, content_type, filename):
    return add_file(file, content_type, filename)
    
def get_file(_id):    
    return get_file_by_id(_id)