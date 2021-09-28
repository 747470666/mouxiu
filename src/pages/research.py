from dash import html
from dash import dcc
from src.components.article import creat_article


# 后期可以设置为自动加载文章，目前暂时作为测试
def research_page(style):
    return html.Div(
        id='body_research', className=style,
        children=[
            '研究或进展'
        ]
    )
