# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328796398.2024751
_template_filename = 'templates/index.html'
_template_uri = 'index.html'
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
        session = context.get('session', UNDEFINED)
        pages = context.get('pages', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def js():
            return render_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 105
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 108
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
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n\n<div class="page-header hide">\n\t<div>\n\t\t<span>\n\t\t\t\u5730\u70b9:')
        # SOURCE LINE 9
        __M_writer(unicode(session.get('city','')))
        __M_writer(u'\n\t\t\t<button class="btn danger">\u9009\u62e9\u5730\u533a</button>\n\t\t</span>\n\t\t<span></span>\n\t</div>\n\t<div class="margin_top_5px">\n\t\t<span>\n\t\t\t\u7c7b\u578b:')
        # SOURCE LINE 16
        __M_writer(unicode(session.get('type','')))
        __M_writer(u'\n\t\t\t<button class="btn default">\u519c\u4e1a</button>\n\t\t\t<button class="btn default">\u7267\u4e1a</button>\n\t\t\t<button class="btn default">\u6e14\u4e1a</button>\n\t\t\t<button class="btn default">\u6797\u4e1a</button>     \n\t\t</span>\n\n\t</div>\n  \n\n\n</div>\n<div class="margin_top_5px">\n      <span>\n          \u5173\u952e\u8bcd:\n          <input class="medium" id="prependedInput" name="prependedInput" size="16" type="text" />\n          <button class="btn success">\u641c\u7d22</button> \n      </span>\n      <span>\n')
        # SOURCE LINE 35
        if session.get('_id', None) == 'admin':
            # SOURCE LINE 36
            __M_writer(u'        <a id="send_news" href="/news/send_news" class="btn danger">\u53d1\u5e03\u65b0\u95fb</a>\n')
            pass
        # SOURCE LINE 38
        __M_writer(u'      </span>\n  \n</div>\n<table>\n\t<thead>\n           <!-- \u8868\u5b57\u6bb5 -->\n      <tr>\n       \t  \n              <th width=100>\n            \t      \u53d1\u5e03\u4eba\n              </th>\n              <th>\n              \t\t\u65b0\u95fb\u6807\u9898\n              </th>\n              <th>\n              \t\u53d1\u5e03\u65f6\u95f4\t\n              </th>\n    \n              <!--\u8868\u5b57\u6bb5-->\n\t\t</tr>\n\t</thead>\n\t<tbody>\n\t\n       <!--\u8868\u6570\u636e-->\n      \n')
        # SOURCE LINE 63
        for news in pages.get('data', []):
            # SOURCE LINE 64
            __M_writer(u'            <tr>\n                   <td>\n                        ')
            # SOURCE LINE 66
            __M_writer(unicode(news.get('auther', '')))
            __M_writer(u'\n                   </td>\n                   <td>\n                        <a href="/news/detail?_id=')
            # SOURCE LINE 69
            __M_writer(unicode(news.get('_id',None)))
            __M_writer(u'">')
            __M_writer(unicode(news.get('title', '')))
            __M_writer(u'</a>\n                   </td>\n\n                   <td>\n                        ')
            # SOURCE LINE 73
            __M_writer(unicode(str(news.get('create_time', '')).split('.')[0]))
            __M_writer(u'\n                   </td>\n            </tr>          \n')
            pass
        # SOURCE LINE 77
        __M_writer(u'         \n\t\t\n\t</tbody>\n           \n</table>\n <div>\n   <input type="hidden" id="last_time" value="')
        # SOURCE LINE 83
        __M_writer(unicode(pages['last_time']))
        __M_writer(u'" />\n\t<div class="float_left">\n\t\u5171')
        # SOURCE LINE 85
        __M_writer(unicode(pages['count']))
        __M_writer(u'\u6761\n\t\n    </div>\n\t<div class="float_right">\n\n      <a href="javascript:void(0)" id="first_page">\u9996\u9875</a>\n')
        # SOURCE LINE 91
        if pages['page'] !=1:
            # SOURCE LINE 92
            __M_writer(u'\t<a href="javascript:void(0)" id="pre_page"> \u4e0a\u4e00\u9875</a>\n')
            pass
        # SOURCE LINE 94
        if pages['count']/pages['limit'] >= 1:
            # SOURCE LINE 95
            __M_writer(u'\t<a href="javascript:void(0)" id="next_page"> \u4e0b\u4e00\u9875 </a>\n')
            pass
        # SOURCE LINE 97
        __M_writer(u'    <input type="hidden" id="old_page" value="')
        __M_writer(unicode(pages['page']))
        __M_writer(u'"  />\n\n   </div>\t\n\t\t\n\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        # SOURCE LINE 106
        __M_writer(u'\n<script src="/static/js/news.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


