# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328714548.291822
_template_filename = 'templates/setting.html'
_template_uri = 'setting.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context.locals_(__M_locals))
        provice_list = context.get('provice_list', UNDEFINED)
        def js():
            return render_js(context.locals_(__M_locals))
        user = context.get('user', UNDEFINED)
        city_list = context.get('city_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 72
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 76
        __M_writer(u'\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        provice_list = context.get('provice_list', UNDEFINED)
        user = context.get('user', UNDEFINED)
        city_list = context.get('city_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n<div class="">\r\n<div id="reg" class="">\r\n    <div class="dialog_title">\r\n        <span class="color_black">\u5e10\u53f7\u7ba1\u7406</span> \r\n\r\n    </div>\r\n    <fieldset>               \r\n    \r\n    <form action="/update_user" method="post" id="update_form">\r\n        <input type=\'hidden\' value=\'1\' name=\'leval\' />\r\n\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u59d3\u540d\u6216\u5355\u4f4d\u540d\u79f0</label>\r\n            <div class="input">\r\n            <input type="text" class="xlarge" value="')
        # SOURCE LINE 19
        __M_writer(unicode(user.get('name', '')))
        __M_writer(u'"  name="name" />\r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u4f4d\u7f6e</label>\r\n            <div class="input">\r\n           \r\n                <select class="loc_select" name="province_id" id="province" defvalue="11">\r\n')
        # SOURCE LINE 27
        for provice in provice_list:
            # SOURCE LINE 28
            if  user.get('province_id', '') == provice.get('_id', ''):
                # SOURCE LINE 29
                __M_writer(u'                            <option value="')
                __M_writer(unicode(provice.get('_id', '')))
                __M_writer(u'" selected=true>')
                __M_writer(unicode(provice.get('city_name', '')))
                __M_writer(u'</option>\r\n')
                # SOURCE LINE 30
            else:
                # SOURCE LINE 31
                __M_writer(u'                            <option value="')
                __M_writer(unicode(provice.get('_id', '')))
                __M_writer(u'" >')
                __M_writer(unicode(provice.get('city_name', '')))
                __M_writer(u'</option>\r\n')
                pass
            # SOURCE LINE 33
            __M_writer(u'                        \r\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'                </select>\r\n                \r\n                <select class="loc_select" name="city_id" id="city" >\r\n')
        # SOURCE LINE 38
        for city in city_list:
            # SOURCE LINE 39
            if  user.get('city_id', '') == city.get('_id', ''):
                # SOURCE LINE 40
                __M_writer(u'                            <option value="')
                __M_writer(unicode(city.get('_id', '')))
                __M_writer(u'" selected=true>')
                __M_writer(unicode(city.get('city_name', '')))
                __M_writer(u'</option>\r\n')
                # SOURCE LINE 41
            else:
                # SOURCE LINE 42
                __M_writer(u'                            <option value="')
                __M_writer(unicode(city.get('_id', '')))
                __M_writer(u'">')
                __M_writer(unicode(city.get('city_name', '')))
                __M_writer(u'</option>\r\n')
                pass
            pass
        # SOURCE LINE 45
        __M_writer(u'                </select>\r\n             <select id="area" class="loc_select" name="area_id">\r\n                 <option value="')
        # SOURCE LINE 47
        __M_writer(unicode(user.get('area_id', '')))
        __M_writer(u'">')
        __M_writer(unicode(user.get('area', '')))
        __M_writer(u'</option>\r\n            </select>\r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u5bc6\u7801</label>\r\n            <div class="input">\r\n                <input type="password" name="password" class="xlarge" value="')
        # SOURCE LINE 54
        __M_writer(unicode(user.get('password', '')))
        __M_writer(u'" id="password" />\r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u786e\u8ba4\u5bc6\u7801</label>\r\n            <div class="input">\r\n                <input type="password" id="cpassword" value="')
        # SOURCE LINE 60
        __M_writer(unicode(user.get('password', '')))
        __M_writer(u'"  class="xlarge">\r\n            </div>\r\n        </div>\r\n        <div class="actions">\r\n            <input type="button" class="btn success" id="update_user_action" value="\u4fee\u6539" />\r\n            <input type="button" class="btn"  id="reuest_real_auth" value="\u7533\u8bf7\u5b9e\u540d\u8ba4\u8bc1"> \r\n        </div> \r\n    </fieldset>                   \t\t\r\n\r\n    </form>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\r\n<script src="/static/js/settings.js"></script>\r\n<script src="/static/js/loc.js"></script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


