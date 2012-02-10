def auth(session, redirect):
    def new_deco(func):        
        if not session.get('_id', None):
            return redirect('/') 
    return new_deco