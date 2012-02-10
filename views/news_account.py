# _*_ coding: utf-8 _*_
from flask import Blueprint 
from service.account import vertify_user
from service.account import check_only_user
from service.account import update_user
from service.account import reg_user
from service.city import get_city_by_id
from service.info import get_info_list
from service.info import get_one_info
from service.info import del_info
from service.info import create_info
from dic import level_html, collection_html, args
from lib.utils import form2dic
from lib.utils import now, DatetimeJSONEncoder
from flaskext.mako import render_template
from flask import  session, request, make_response, redirect, jsonify as return_json
account = Blueprint('account_view', __name__)