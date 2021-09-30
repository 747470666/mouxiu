from dash import html
from dash import dcc
from src.components.article import creat_article


# 后期可以设置为自动加载文章，目前暂时作为测试
from src.components.page_head import page_head


def about_page(style):
    return html.Div(
        id='body_about', className=style,
        children=[
            page_head(style, '关于'),
            creat_article(
                [
                    {'src': 'assets/static/images/github_web.jpg', 'width': 0.2},
                ],
                [
                    '''
                    **查看开源代码**
                    
                    [VSWBD科研小站](https://github.com/747470666/mouxiu)
                    ''',
                    '''
                    ***
                    *我的邮箱*
                    **747470666@qq.com**
                    '''
                ]
            )
        ]
    )
