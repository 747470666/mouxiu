from dash import html


def page_head(style, title):
    return html.Div(
        id='body_head', className=style,
        children=[
            html.H1(title, id='body_head_title', className=style)
        ]
    )
