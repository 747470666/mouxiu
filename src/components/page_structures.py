import dash
from dash import dcc
from dash import html


# my_head、my_body、my_foot三块区域的大小及相对位置的设置（默认html全部在body中）
# 单例模式，后期方便设置一键切换模式
class PageStruct(object):
    _status = None

    def __init__(self, my_setting):
        PageStruct._status = self
        self._head = my_setting['head']
        self._body = my_setting['body']
        self._foot = my_setting['foot']

    @classmethod
    def get_instance(cls):
        if PageStruct._status is None:
            raise RuntimeError(u"未初始化，请先初始化！")
        return PageStruct._status

    # head部分
    def my_head(self):
        if self._head['switch'] == 'on':
            return html.Header(id='head', className='app', children='Head')
        else:
            return

    # body部分
    def my_body(self):
        if self._body['switch'] == 'on':
            return html.Div(id='body', className='app', children='Body')
        else:
            return

    # foot部分
    def my_foot(self):
        if self._foot['switch'] == 'on':
            return html.Footer(id='foot', className='app', children=[html.Div('©版权所有，侵权必究'), html.Div(' 2021')])
        else:
            return
