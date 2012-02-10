# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328803131.899668
_template_filename = 'templates/news/news_detail.html'
_template_uri = 'news/news_detail.html'
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
        news = context.get('news', UNDEFINED)
        session = context.get('session', UNDEFINED)
        def js():
            return render_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 10
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 13
        __M_writer(u'\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        news = context.get('news', UNDEFINED)
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n<div>\r\n    ')
        # SOURCE LINE 5
        __M_writer(unicode(news.get('content', '')))
        __M_writer(u'\r\n</div>\r\n<div>\r\n<a href="')
        # SOURCE LINE 8
        __M_writer(unicode(session.get('url')))
        __M_writer(u'" class="btn success">\u8fd4\u56de</a>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


