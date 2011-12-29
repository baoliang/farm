# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1324911844.6240001
_template_filename='templates/login.html'
_template_uri='login.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
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
        def css():
            return render_css(context.locals_(__M_locals))
        def js():
            return render_js(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'css'):
            context['self'].css(**pageargs)
        

        # SOURCE LINE 4
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 115
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js'):
            context['self'].js(**pageargs)
        

        # SOURCE LINE 120
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n\n\n<form action="/login" method="post">\n\n\n\t<div class="cb win900">\n\n\t\t<div id="conleft">\n\n\t\t\t<!--\u56fe\u7247\u8f6e\u64ad\u63a7\u4ef6-->\n\n\t\t\t<div id="ibanner">\n\n\t\t\t\t<div id="ibanner_pic"> <a><img src="/static/img/apple.jpg" /></a></div>\n\n\t\t\t</div>\n\n\t\t</div>\n\n\t\t<div id="conright">\n\n\t\t\t<ul class="login-scrool">\n\n\t\t\t\t<li class="hover" onclick="setTab(\'scrool\',1,2,this)" id="scrool1"><em></em>\u8d26\u6237\u767b\u5f55</li>\n\n\t\t\t\t<li onclick="setTab(\'scrool\',2,2,this)" id="scrool2"><em></em></li>\n\n\t\t\t</ul>\n\n\t\t\t<div class="scrool-bg">\n\n\t\t\t\t<div class="loginbox">\n\n\t\t\t\t\t<div id="tipDiv"></div>\n\n\t\t\t\t\t<table>\n\n\t\t\t\t\t\t<tr id="usernametr">\n\n\t\t\t\t\t\t\t<th>\u8d26\u6237\u540d</th>\n\n\t\t\t\t\t\t\t<td><input class="inp inw c_ccc" type="text" id="uid" name="_id" onfocus=\'if (this.value == "\u7528\u6237\u540d/\u7535\u5b50\u90ae\u7bb1") this.value = "";this.className = "inp inw";\' size="20" value="\u7528\u6237\u540d/\u7535\u5b50\u90ae\u7bb1" /></td>\n\n\t\t\t\t\t\t</tr>\n\n\t\t\t\t\t\t<tr id="passwordtr">\n\n\t\t\t\t\t\t\t<th>\u5bc6\u3000\u7801</th>\n\n\t\t\t\t\t\t\t<td style=" padding-bottom:5px;">\n\n\t\t\t\t\t\t\t\t<input class="inp inw" id="password" type="password" style="margin-bottom:7px;" name="password" size="20" onpaste="return false" value=""/>\n\n\t\t\t\t\t\t\t</td>\n\n\t\t\t\t\t\t</tr>\n\n\t\t\t\t\t\t<tr>\n\n\t\t\t\t\t\t\t<th>&nbsp;</th>\n\n\t\t\t\t\t\t\t<td style="padding: 0pt;">\n\n\t\t\t\t\t\t\t\t<input type="checkbox" style="vertical-align: middle;" id="coks" value="on" name="remember" />\n\n\t\t\t\t\t\t\t\t<label class="logintip" for="coks">30\u5929\u5185\u81ea\u52a8\u767b\u5f55 (\u516c\u5171\u573a\u6240\u614e\u7528)</label>\n\n\t\t\t\t\t\t\t</td>\n\n\t\t\t\t\t\t</tr>\n\n\t\t\t\t\t\t<tr>\n\n\t\t\t\t\t\t\t<th>&nbsp;</th>\n\n\t\t\t\t\t\t\t<td style="padding:0;">\n\n\t\t\t\t\t\t\t\t<span class="butt" style="line-height:34px;">\n\n\t\t\t\t\t\t\t\t<input type="submit" name="btnSubmit" value="\u767b\u5f55" class="btns" accesskey="l" id="btnSubmit" />\n\n\t\t\t\t\t\t\t\t</span><span class="reg-a"><a href="/reg">\u514d\u8d39\u6ce8\u518c</a>|<a href="/forgetpassword">\u627e\u56de\u5bc6\u7801</a> </span>\n\n\t\t\t\t\t\t\t</td>\n\n\t\t\t\t\t\t</tr>\n\n\t\t\t\t\t</table>\n\n\t\t\t\t</div>\n\n\n\n\t\t\t</div><!--scrool bg-->\n\n\t\t\t<div class="clear"></div>\n\n\t\t</div>\n\n\t\t<div class="c"></div>\n\n\t</div>\n\n\t<div id="footer" class="win900" >\n\n\n\t</div>\n\n</form>\n')
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
        __M_writer(u"\n<link href='/static/css/login.css' rel='stylesheet' type='text/css' />\n")
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
        __M_writer(u'\n<script>\n\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


