# structure是页面结构组件
from core import app
from dash import html
from dash import dcc
from dash.dependencies import Input, Output


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
    def my_head(self, page_index):
        return head_content(self._head['style'], page_index)

    # body部分
    def my_body(self, page_index):
        return body_content(self._body['style'], page_index)

    # foot部分
    def my_foot(self, page_index):
        return foot_content(self._foot['style'], page_index)


# 头内容样式
def head_content(style, page_index):
    return (
        html.Div(id='head', className=style,
                 children=[
                     dcc.Tabs(
                         id="head_tabs",
                         value=page_index,
                         parent_className='custom-tabs',
                         className='custom-tabs-container',
                         children=[
                             dcc.Tab(
                                 label='首页',
                                 value='page1',
                                 className='custom-tab',
                                 selected_className='custom-tab--selected'
                             ),
                             dcc.Tab(
                                 label='研究',
                                 value='page2',
                                 className='custom-tab',
                                 selected_className='custom-tab--selected'
                             ),
                             dcc.Tab(
                                 label='关于',
                                 value='page3',
                                 className='custom-tab',
                                 selected_className='custom-tab--selected'
                             ),
                         ]),
                     dcc.Location(id='head_url', refresh=True),
                 ])
    )


@app.callback(Output('head_url', 'pathname'),
              Input('head_tabs', 'value'))
def render_content(tab):
    if tab == 'page1':
        return '/'
    elif tab == 'page2':
        return '/research'
    elif tab == 'page3':
        return '/mine'


# 头内容样式
def body_content(style, page_index):
    if page_index == 'page1':
        return html.Div(id='body', className=style, children='这是首页！')
    elif page_index == 'page2':
        return html.Div(id='body', className=style, children='研究或进展')
    elif page_index == 'page3':
        return html.Div(id='body', className=style, children='关于我以及联系我')


# 头内容样式
def foot_content(style, page_index):
    import pandas as pd
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })
    import plotly.express as px
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    return html.Footer(id='foot', className=style, children=[
        dcc.Graph(
            id='example-graph',
            figure=fig
        ), html.Div('©版权所有，侵权必究'), html.Div(' 2021')])
