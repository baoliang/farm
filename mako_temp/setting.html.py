# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328604535.496031
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
        def js():
            return render_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 32
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 35
        __M_writer(u'\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n<div class="">\r\n<div id="reg" class="">\r\n    <div class="dialog_title">\r\n        <span class="color_black">\u5e10\u53f7\u7ba1\u7406</span> \r\n\r\n    </div>\r\n    <fieldset>                   \t\t\r\n    \r\n    <form action="/reg_user" method="post" id="reg_form">\r\n        <input type=\'hidden\' value=\'1\' name=\'leval\' />\r\n\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u59d3\u540d\u6216\u5355\u4f4d\u540d\u79f0</label>\r\n            <div class="input">\r\n            <input type="text" class="xlarge" value=""  name="name" />\r\n            </div>\r\n        </div>\r\n\r\n        <div class="actions">\r\n            <input type="button" class="btn success" id="reg_user_action" value="\u4fee\u6539" />\r\n            <input type="button" class="btn"  id="reg_user_cancel" value="\u7533\u8bf7\u5b9e\u540d\u8ba4\u8bc1"> \r\n        </div> \r\n    </fieldset>                   \t\t\r\n\r\n    </form>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer(u'\r\n<script src="/static/js/setting.js"></script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


