# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328709013.88588
_template_filename = 'templates/reg.html'
_template_uri = 'reg.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'css', u'js']


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
        def css():
            return render_css(context.locals_(__M_locals))
        city_list = context.get('city_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'css'):
            context['self'].css(**pageargs)
        

        # SOURCE LINE 3
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 70
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 74
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        provice_list = context.get('provice_list', UNDEFINED)
        city_list = context.get('city_list', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<div class="">\n<div id="reg" class="">\n    <div class="dialog_title">\n        <span class="color_black">\u6ce8\u518c\u5e10\u53f7</span> \n\n    </div>\n    <fieldset>                   \t\t\n    \n    <form action="/reg_user" method="post" id="reg_form">\n        <input type=\'hidden\' value=\'1\' name=\'leval\' />\n        <div class="clearfix">\n            <label for="xlInput">\u7528\u6237\u540d(\u6700\u597d\u7528\u90ae\u7bb1)</label>\n            <div class="input">\n              <input type="text" class="xlarge" value=""  name="_id" id="_id" />\n              <span id=\'reg_tips\'></span>\n            </div>\n        </div>\n        <div class="clearfix">\n            <label for="xlInput">\u59d3\u540d\u6216\u5355\u4f4d\u540d\u79f0</label>\n            <div class="input">\n            <input type="text" class="xlarge" value=""  name="name" />\n            </div>\n        </div>\n        <div class="clearfix">\n            <label for="xlInput">\u4f4d\u7f6e</label>\n            <div class="input">\n           \n                <select class="loc_select" name="province_id" id="province" defvalue="11">\n')
        # SOURCE LINE 33
        for provice in provice_list:
            # SOURCE LINE 34
            __M_writer(u'                        <option value="')
            __M_writer(unicode(provice.get('_id', '')))
            __M_writer(u'">')
            __M_writer(unicode(provice.get('city_name', '')))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 36
        __M_writer(u'                </select>\n                \n                <select class="loc_select" name="city_id" id="city" >\n')
        # SOURCE LINE 39
        for city in city_list:
            # SOURCE LINE 40
            __M_writer(u'                        <option value="')
            __M_writer(unicode(city.get('_id', '')))
            __M_writer(u'">')
            __M_writer(unicode(city.get('city_name', '')))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 42
        __M_writer(u'                </select>\n             <select id="area" class="loc_select" name="area_id">\n                \n            </select>\n            </div>\n        </div>\n        <div class="clearfix">\n            <label for="xlInput">\u5bc6\u7801</label>\n            <div class="input">\n                <input type="password" name="password" class="xlarge" id="password" />\n            </div>\n        </div>\n        <div class="clearfix">\n            <label for="xlInput">\u786e\u8ba4\u5bc6\u7801</label>\n            <div class="input">\n                <input type="password" id="cpassword" class="xlarge">\n            </div>\n        </div>\n    \n        <div class="actions">\n            <input type="button" class="btn success" id="reg_user_action" value="\u6ce8\u518c" />\n            <input type="button" class="btn"  id="reg_user_cancel" value="\u6682\u65f6\u5148\u4e0d\u6ce8\u518c"> \n        </div> \n    </fieldset>                   \t\t\n\n    </form>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def css():
            return render_css(context)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        # SOURCE LINE 71
        __M_writer(u'\n<script src="/static/js/login.js"></script>\n<script src="/static/js/loc.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


