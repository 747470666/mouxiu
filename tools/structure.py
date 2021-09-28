# structure是页面结构组件
from core import app
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

from tools.router_setting import get_router_setting, get_router_page
from tools.style import head_tab_selected


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


pathname_setting, pagename_setting, tab_id, tab_dict = get_router_setting()


# 制作导航栏的按钮
def head_tab(style):
    tab_list = []
    for i in range(len(pagename_setting)):
        tab_list.append(
            dcc.Tab(label=pagename_setting[i], value=tab_id[i], className=style,
                    selected_style=head_tab_selected(style))
        )
    return tab_list


# 头内容样式
def head_content(style, page_index):
    return (
        html.Div(
            id='head', className=style,
            children=[
                html.Div(id='head_titles', className=style, children=[
                    html.H1('汪颖', id='head_titles_name', className=style),
                    html.P('人生如逆旅，我亦是行人。', id='head_titles_introduction', className=style)
                ]),
                dcc.Tabs(id="head_tabs", value=page_index, className=style, children=head_tab(style)),
                dcc.Location(id='head_url', refresh=True),
            ])
    )


@app.callback(Output('head_url', 'pathname'),
              Input('head_tabs', 'value'))
def render_content(tab):
    return tab_dict[tab]


# 主体内容样式
def body_content(style, page_index):
    return (
        html.Div(
            id='body', className=style,
            children=get_router_page(style, page_index)
        )
    )


# 页脚内容样式
def foot_content(style, page_index):
    return html.Footer(id='foot', className=style, children=[
        html.Div('©版权所有，侵权必究'), html.Div(' 2021')])
