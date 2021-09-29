from dash import html
from dash import dcc

style_article_img = [
    {
        'float': 'left',
        'padding': '20px 20px 8px 0px',
    },
    {
        'float': 'right',
        'padding': '20px 0px 8px 20px',
    }
]


def creat_article(img_src=[], text_content=[], first_position='left'):
    num_record = 0 if first_position == 'left' else 1
    marry_len = min(len(img_src), len(text_content))
    article_list = []
    for i in range(marry_len):
        article_list.append(
            html.Div(
                className='body_article_div',
                children=[
                    html.Img(src=img_src[i], className='body_article_img',
                             style=style_article_img[num_record % 2]),
                    html.P(text_content[i], className='body_article_p')
                ]
            )
        )
        num_record = num_record + 1
    for i in range(marry_len, len(img_src)):
        article_list.append(
            html.Div(
                children=[
                    html.Img(src=img_src[i])
                ]
            )
        )
    for i in range(marry_len, len(text_content)):
        article_list.append(
            html.Div(
                children=[
                    html.P(text_content[i])
                ]
            )
        )
    return html.Div(children=article_list)
