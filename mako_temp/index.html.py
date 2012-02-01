# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328094297.6071801
_template_filename = 'templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'search', u'js']


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
        def search():
            return render_search(context.locals_(__M_locals))
        session = context.get('session', UNDEFINED)
        pages = context.get('pages', UNDEFINED)
        def js():
            return render_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'search'):
            context['self'].search(**pageargs)
        

        # SOURCE LINE 14
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 115
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 118
        __M_writer(u'\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        session = context.get('session', UNDEFINED)
        pages = context.get('pages', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\n<table>\n\t<thead>\n           <!-- \u8868\u5b57\u6bb5 -->\n      <tr>\n       \t  \n              <th width=100>\n            \t      \u53d1\u5e03\u4eba\n              </th>\n              <th>\n              \t\t\u65b0\u95fb\u6807\u9898\n              </th>\n              <th>\n              \t\u53d1\u5e03\u65f6\u95f4\t\n              </th>\n    \n              <!--\u8868\u5b57\u6bb5-->\n\t\t</tr>\n\t</thead>\n\t<tbody>\n\t\n       <!--\u8868\u6570\u636e-->\n      \n')
        # SOURCE LINE 38
        for news in pages.get('data', []):
            # SOURCE LINE 39
            __M_writer(u'            <tr>\n                   <td>\n                        ')
            # SOURCE LINE 41
            __M_writer(unicode(news.get('auther', '')))
            __M_writer(u'\n                   </td>\n                   <td>\n                        ')
            # SOURCE LINE 44
            __M_writer(unicode(news.get('title', '')))
            __M_writer(u'\n                   </td>\n\n                   <td>\n                        ')
            # SOURCE LINE 48
            __M_writer(unicode(news.get('create_time', '')))
            __M_writer(u'\n                   </td>\n            </tr>          \n')
            pass
        # SOURCE LINE 52
        __M_writer(u'         \n\t\t\n\t</tbody>\n           \n</table>\n <div>\n   <input type="hidden" id="last_time" value="')
        # SOURCE LINE 58
        __M_writer(unicode(pages['last_time']))
        __M_writer(u'" />\n\t<div class="float_left">\n\t\u5171')
        # SOURCE LINE 60
        __M_writer(unicode(pages['count']))
        __M_writer(u'\u6761\n\t\n    </div>\n\t<div class="float_right">\n\n      <a href="javascript:void(0)" id="first_page">\u9996\u9875</a>\n')
        # SOURCE LINE 66
        if pages['page'] !=1:
            # SOURCE LINE 67
            __M_writer(u'\t<a href="javascript:void(0)" id="pre_page"> \u4e0a\u4e00\u9875</a>\n')
            pass
        # SOURCE LINE 69
        if pages['count']/pages['limit'] >= 1:
            # SOURCE LINE 70
            __M_writer(u'\t<a href="javascript:void(0)" id="next_page"> \u4e0b\u4e00\u9875 </a>\n')
            pass
        # SOURCE LINE 72
        __M_writer(u'    <input type="hidden" id="old_page" value="')
        __M_writer(unicode(pages['page']))
        __M_writer(u'"  />\n\n   </div>\t\n\t\t\n\n</div>\n<div id="send_news_window" class="hide dialog">\n    <div class="dialog_title">\n        <span class="color_black">\u53d1\u5e03\u65b0\u95fb</span> \n        <a href="javascript:void(0)" id="add_dialog_close" > \n        <span class="dialog_close close">x</span>\n         </a>\n    </div>\n    <fieldset>                   \t\t\n    \n    <form action="/create_info" method="post">\n        <input type=\'hidden\' value=\'news\' name=\'collection\' />\n        <input type=\'hidden\' value=\'/\' name=\'return\' />\n\t\t<input name=\'auther\' value=\'')
        # SOURCE LINE 90
        __M_writer(unicode(session.get('name')))
        __M_writer(u'\' type=\'hidden\' />\n        <div class="clearfix">\n            <label for="xlInput">\u6807\u9898</label>\n            <div class="input">\n            <input type="text" class="xlarge" value=""  name="title" />\n            </div>\n        </div>\n        <div class="clearfix">\n            <label for="xlInput">\u5185\u5bb9</label>\n            <div class="input">\n                <textarea class="xxlarge" name="centent" id="textarea" rows="3" ></textarea>\n            </div>\n        </div>\n  \n    \n        <div class="actions">\n            <input type="submit" class="btn success" id="add_dialog_submit" value="\u53d1\u5e03"" />\n            <input type="button" class="btn"  id="add_dialog_cancel" value="\u6682\u4e0d\u6ce8\u518c"> \n        </div> \n    </fieldset>                   \t\t\n\n    </form>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_search(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def search():
            return render_search(context)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<div class="margin_top_5px">\n      <span>\n          \u5173\u952e\u8bcd:\n          <input class="medium" id="prependedInput" name="prependedInput" size="16" type="text" />\n          <button class="btn success">\u641c\u7d22</button> \n      </span>\n      <span>\n          <button id="send_news" class="btn danger">\u53d1\u5e03\u65b0\u95fb</button> \n      </span>\n  \n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        # SOURCE LINE 116
        __M_writer(u'\n<script src="/static/js/news.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


