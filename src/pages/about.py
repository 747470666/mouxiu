from dash import html
from dash import dcc
from src.components.article import creat_article


# 后期可以设置为自动加载文章，目前暂时作为测试
def about_page(style):
    return html.Div(
        id='body_about', className=style,
        children=[
            '关于我以及联系我'
        ]
    )
