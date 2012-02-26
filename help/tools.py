from lib.utils import form2dic
from service.info import get_info_list
from service.info import get_one_info
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
    search_value = query.get('search_value', "")
    query_loc = []
    if boot_time:
        query.update({'boot_time': boot_time})
    if query.has_key("search_value"):
        query.pop("search_value")
    if search_value != "":
        query.update({
            "$or" :[
                {"content":{"$regex": search_value}},
                {"title":{"$regex": search_value}},
            ]
        })
    province = query.get("province", "")
    if province != "":
        query_loc.append(province)
    if query.has_key("province"): query.pop("province")
  
    city = query.get("city", "")    
    if city != "":
        query_loc.append(city)
    if query.has_key("city"): query.pop("city")
    area = query.get("area", "")    
    if  area != "":
        query_loc.append(area)
    if query.has_key("area"): query.pop("area")
    
    if query_loc:     
        query.update({
            "from_loc": {"$regex": " ".join(query_loc)}
        })
    if query.has_key("type"): 
        if query.get("type") == "": query.pop("type")
    start_price  = query.get("start_price", "")
    if start_price != "":
        try:
            start_price = int(start_price)
        except:
            start_price = 0
        query.update({"price": {"$gte": start_price}})
    if query.has_key("start_price"): query.pop("start_price") 

    end_price  = query.get("end_price", "")
    if start_price != "":
        try:
            end_price = int(end_price)
            query.update({"price": {"$lte": end_price}})
        except:
            pass
        
    if query.has_key("end_price"): query.pop("end_price")     
    return query
    
def get_query_page(session_page, query, sid, collection):
    page = query.get('page', 1)
    if not session_page or page == 1 or page > query.get('old_page', 1):
        pages = get_info_list(
            collection, 
            query=query
        ) 
        set_cach(sid+str(pages.get('page'))+'_news_pages', pages)
    else:
        pages =  get_cach(sid+str(query.get('page'))+'_news_pages') 
    return pages
    
def get_city_by_id(_id):
    if _id in ["1", "2", "9", "22"]:
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
    return city_list
    