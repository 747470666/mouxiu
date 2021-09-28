from dash import html
from dash import dcc

from src.components.article import creat_article


def index_page_head(style):
    return html.Div(
        id='body_index_head', className=style,
        children=[
            html.H1('主页', id='body_index_head_title', className=style),
            html.P('个人介绍与动态展示', id='body_index_head_introduction', className=style)
        ]
    )


# 后期可以设置为自动加载文章，目前暂时作为测试
def index_page(style):
    return html.Div(
        id='body_index', className=style,
        children=[
            index_page_head(style),
            creat_article([
                'assets/static/images/computer.png',
                'assets/static/images/computer.png',
                'assets/static/images/computer.png'
            ], [
                'aaa',
                'bbb',
                'ccc'
            ])
        ]
    )
