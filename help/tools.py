def set_user_session(session, user):
    session['_id'] = user.get('_id', None)
    session['name'] = user.get('name', None)
    session['province'] = user.get('province', '')
    session['city'] = user.get('city', '')
    session['area'] = user.get('area', '')
    return session
