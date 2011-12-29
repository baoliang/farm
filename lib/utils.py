#coding: utf-8
import sys
import os
from datetime import datetime
import traceback
def print_err():
    '''
    @todo: 打印错误信息
    '''
    sys.stderr.write('=='*30+os.linesep)
    sys.stderr.write('err time: '+str(datetime.now())+os.linesep)
    sys.stderr.write('--'*30+os.linesep)
    traceback.print_exc(file=sys.stderr)
    sys.stderr.write('=='*30+os.linesep)
    
def now():
    return datetime.now()

def form2dic(form):
    temp_dic = {}
    for i in form:
        temp_dic[i] = form[i]
    return temp_dic