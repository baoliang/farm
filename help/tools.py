from lib.utils import form2dic
from service.info import get_info_list
from lib.cach import get_cach
from lib.cach import set_cach
def set_user_session(session, user):
    session['_id'] = user.get('_id', None)
    session['name'] = user.get('name', None)
    session['province'] = user.get('province', '')
    session['city'] = user.get('city', '')
    session['area'] = user.get('area', '')
    return session

def set_page_session(request_url, pages):  
        return {
                    'url': request_url,
                    'boot_time': pages.get('boot_time'),
                 
                    'page':   pages.get('page'),
                }     
    
def get_query(query_values, boot_time = None):
    query = form2dic(query_values)
    if boot_time:
        query.update({'boot_time': boot_time})
    content = query.get('content', None)
    title = query.get('title', None)
    search_value = ""
    if content or content == "":
       search_value = content
       query.update({"content":{"$regex": content}})
    if title or title == "":
        query.update({"title":{"$regex": title}})
    return query
    
def get_query_page(session_page, query, sid, collection):
    print  query.get('page', 1)  >= query.get('old_page', 1)
    if not session_page or query.get('page', 1) == 1 or query.get('page', 1)  >=   query.get('old_page', 1):
        print 'not in catch'
        
        pages = get_info_list(
            collection, 
            query=query
        ) 
        set_cach(sid+str(pages.get('page'))+'_news_pages', pages)
    else:
        pages =  get_cach(sid+str(query.get('page'))+'_news_pages') 
    return pages
    
def get_city_by_id(_id):
    if _id in ["1", "2", "9"]:
        _id  = get_one_info(
                'city',
                query={"f_id": _id}
        ).get("_id") 
 
    city_list = get_info_list(
        'city',
        query={"f_id": _id},
        return_type = "list",
        sort=1
    )
    print city_list
    return city_list
    