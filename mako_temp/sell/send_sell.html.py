# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328843091.032213
_template_filename = 'templates/sell/send_sell.html'
_template_uri = 'sell/send_sell.html'
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
        

        # SOURCE LINE 118
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 121
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
        __M_writer(u'\r\n\r\n<div id="send_news_window" class="">\r\n    <div class="dialog_title">\r\n        <span class="color_black">\u53d1\u5e03\u65b0\u95fb</span> \r\n        <a href="javascript:void(0)" id="add_dialog_close" > \r\n        <span class="dialog_close close"></span>\r\n         </a>\r\n    </div>\r\n    <fieldset>                   \t\t\r\n   \r\n    <form action="/create_info?return=/sell" method="post">\r\n        <input type=\'hidden\' value=\'news\' name=\'collection\' />\r\n\t\t<input name=\'auther\' value=\'')
        # SOURCE LINE 16
        __M_writer(unicode(session.get('name')))
        __M_writer(u'\' type=\'hidden\' />\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u73b0\u8d27\u671f\u8d27</label>\r\n            <div class="input">\r\n            \u671f\u8d27<input type="checkbox" class="xlarge" value=""  name="title" />\r\n            //\u4fe1\u606f\u6709\u6548\u65f6\u95f4\u6bb5\r\n            <input type="text" class="xlarge" value=""  name="title" />\r\n            <input type="text" class="xlarge" value=""  name="title" />\r\n            \u73b0\u8d27<input type="checkbox" class="xlarge" value=""  name="title" />\r\n            //\u4fe1\u606f\u6709\u6548\u65f6\u95f4\u6bb5\r\n            \r\n            </div>\r\n        </div>\r\n        //\u5982\u679c\u9009\u4e2d\u884c\u4e1a\u5c31\u4e0d\u9700\u8981\u586b\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u884c\u4e1a</label>\r\n            <div class="input">\r\n            \r\n          <input type="checkbox" class="xlarge" value=""  name="title" />\r\n            //\u4fe1\u606f\u6709\u6548\u65f6\u95f4\u6bb5\r\n            \r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u79cd\u7c7b</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u89c4\u683c</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u6570\u91cf</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u4ef7\u683c</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        \r\n        <div class="clearfix">\r\n            <label for="xlInput">\u51fa\u4ea7\u5730\u70b9</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u4ea4\u8d27\u5730\u70b9</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        //\u9ed8\u8ba4\u81ea\u5df2\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u4f9b\u5e94\u65b9</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        //\u9ed8\u8ba4\u81ea\u5df2\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u8054\u7cfb\u4eba</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        //\u9ed8\u8ba4\u81ea\u5df2\r\n        <div class="clearfix">\r\n            <label for="xlInput">\u8054\u7cfb\u7535\u8bdd</label>\r\n            <div class="input">\r\n                <input type="text" class="xlarge" value=""  name="title" />\r\n            </div>\r\n        </div>\r\n        \r\n        \r\n        \r\n        <div class="clearfix">\r\n            <label for="xlInput">\u5185\u5bb9</label>\r\n            <div class="input">\r\n                <textarea class="xxlarge" name="centent" id="textarea" rows="3" ></textarea>\r\n            </div>\r\n        </div>\r\n  \r\n    \r\n        <div class="actions">\r\n            <input type="submit" class="btn success" id="add_dialog_submit" value="\u53d1\u5e03"" />\r\n            <input type="button" class="btn"  id="add_dialog_cancel" value="\u6682\u4e0d\u6ce8\u518c"> \r\n        </div> \r\n    </fieldset>                   \t\t\r\n\r\n    </form>\r\n\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        # SOURCE LINE 119
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


