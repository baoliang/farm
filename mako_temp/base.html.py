# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1328714694.2721131
_template_filename = u'templates/base.html'
_template_uri = u'base.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'css', u'js']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context.locals_(__M_locals))
        session = context.get('session', UNDEFINED)
        def css():
            return render_css(context.locals_(__M_locals))
        def js():
            return render_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n<title>\u519c\u7267\u9c7c\u6797\u7f51</title>\n    <link href="/static/css/bootstrap.css" rel="stylesheet" media="screen" type="text/css" />  \n    <link href="/static/css/layout.css" rel="stylesheet" media="screen" type="text/css" />      \n    <link href="/static/css/base.css" rel="stylesheet" media="screen" type="text/css" />\n    <link rel="shortcut icon" href="/static/img/favicon.ico">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'css'):
            context['self'].css(**pageargs)
        

        # SOURCE LINE 9
        __M_writer(u'\n\n</head>\n<body>\n<div class="topbar">\n  <div class="fill">\n    <div class="container menu_container">\n      <a class="brand" href="#"><img src="/static/img/farm.jpg" /></a>\n      <ul class="nav">\n        <li id="menu_news"><a href="/">\u8d44\u8baf\u4e13\u680f</a></li>\n        <li><a href="/sell">\u4f9b\u5e94\u4fe1\u606f</a></li>\n        <li><a href="/buy">\u6c42\u8d2d\u4fe1\u606f</a></li>\n        <li><a href="/teach">\u6280\u672f\u63a8\u5e7f</a></li>\n        <li><a href="#contact">\u62db\u5546\u52a0\u76df</a></li>\n        <li><a href="#about">\u5408\u4f5c\u7ecf\u8425</a></li>\n        <li><a href="#contact">\u62db\u8d44\u7533\u8bf7</a></li>\n        <li><a href="#about">\u9ec4\u9875\u5c55\u793a</a></li>        \n      </ul>\n        <form action="/login" class="login" method="POST">\n')
        # SOURCE LINE 28
        if  session.get('_id', {}):
            # SOURCE LINE 29
            __M_writer(u'                <span class="color_red welcome">\u6b22\u8fce ')
            __M_writer(unicode(session.get('name', None)))
            __M_writer(u'</span>\n                <a href="/quit" class="btn danger">\u9000\u51fa\u5e10\u53f7</a>\n                <a href="/setting" class="btn">\u5e10\u53f7\u8bbe\u7f6e</a>\n')
            # SOURCE LINE 32
        else:
            # SOURCE LINE 33
            __M_writer(u'                <input class="input-small" type="text" name="_id" placeholder="\u7528\u6237\u540d">\n                <input class="input-small" type="password" name="password" placeholder="\u5bc6\u7801">\n                <button class="btn" type="submit">\u767b\u5f55</button>\n                <a href="/reg" class="btn danger">\u6ce8\u518c</a>\n                <span class="color_red">')
            # SOURCE LINE 37
            __M_writer(unicode(session.get('err_msg', '')))
            __M_writer(u'</span>\n')
            pass
        # SOURCE LINE 39
        __M_writer(u'        </form>\n        \n    </div>\n  </div>\n</div>\n\n<div class="container">\n\n    <div class="content">\n\n        <div id="content">\n          \n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 51
        __M_writer(u'\n            \n        </div>\n        <div class="clearfix"></div> \n    </div>\n\n  <footer>\n    <p>&copy; \u519c\u7267\u6e14\u6797\u4fe1\u606f\u7f51 2011</p>\n  </footer>\n\n</div> <!-- /container -->\n\n<div id="alert" class="hide alert-message error" >\n    <a class="close" href="#"  id="alert_close">\xd7</a>\n    <p id="alert_content"></p>\n</div>\n</body>\n</html>\n<script type="text/javascript" src="/static/js/jquery-1.6.4.js" ></script>\n<script type="text/javascript" src="/static/js/lib.js" ></script>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 71
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def css():
            return render_css(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def js():
            return render_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


