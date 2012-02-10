# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328841268.892307
_template_filename = 'templates/news/send_news.html'
_template_uri = 'news/send_news.html'
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
    return runtime._inherit_from(context, u'../base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context.locals_(__M_locals))
        session = context.get('session', UNDEFINED)
        def js():
            return render_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 41
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 51
        __M_writer(u'\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n<div id="send_news_window" class="">\r\n    <div class="dialog_title">\r\n        <span class="color_black">\u53d1\u5e03\u65b0\u95fb</span> \r\n        <a href="javascript:void(0)" id="add_dialog_close" > \r\n        <span class="dialog_close close"></span>\r\n         </a>\r\n    </div>\r\n    <fieldset>                   \t\t\r\n    \r\n    <form action="/create_info" method="post">\r\n        <input type=\'hidden\' value=\'news\' name=\'collection\' />\r\n        <input type=\'hidden\' value=\'/\' name=\'return\' />\r\n\t\t<input name=\'auther\' value=\'')
        # SOURCE LINE 17
        __M_writer(unicode(session.get('name')))
        __M_writer(u'\' type=\'hidden\' />\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u6807\u9898</label>\r\n            <div class="input">\r\n            <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u5185\u5bb9</label>\r\n            <div class="input">\r\n                <textarea id="editor_id" name="content" style="width:800px;height:400px;"></textarea>\r\n            </div>\r\n        </div>\r\n    \r\n        <div class="actions">\r\n            <input type="submit" class="btn success" id="add_dialog_submit" value="\u53d1\u5e03"" />\r\n            <input type="button" class="btn"  id="add_dialog_cancel" value="\u6682\u4e0d\u53d1\u5e03"> \r\n        </div> \r\n    </fieldset>                   \t\t\r\n\r\n    </form>\r\n\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\r\n<script src="/static/js/kindeditor-min.js"></script>\r\n<script src="/static/js/zh_CN.js"></script>\r\n<script>\r\n     var editor;\r\n        KindEditor.ready(function(K) {\r\n                editor = K.create(\'#editor_id\');\r\n        });\r\n\t\t</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


