# ==============================================================
# Designed by 汪颖
# Start at 2021.09.27
# Version 0.1 Development

# ==============================================================
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# 尽量不要使用下面两个（旧版本方法）
# import dash_core_components as dcc
# import dash_html_components as html

# ==============================================================
# 引入dash包
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# ==============================================================
# 引入自定义框架及组件
from src.components.page_structures import PageStruct

# ==============================================================
# 初始化
# app的初始化，自动引入assets中的所有资源
app = dash.Dash(__name__)

# 页面结构初始化
# 开关 switch: on/off
# 默认样式 style: string （可以自己设计样式）
mySetting = {
    'head': {
        'switch': 'on',
        'style': 'wordpress',
    },
    'body': {
        'switch': 'on',
        'style': 'wordpress',
    },
    'foot': {
        'switch': 'on',
        'style': 'wordpress',
    },
}
# 结构初始化
page_struct = PageStruct(mySetting)

# ==============================================================
# app入口
app.layout = html.Div(id='app', children=[
    page_struct.my_head(),
    page_struct.my_body(),
    page_struct.my_foot(),
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Tab 1', value='tab-1'),
        dcc.Tab(label='Tab 2', value='tab-2'),
        dcc.Tab(label='Tab 3', value='tab-3'),
        dcc.Tab(label='Tab 4', value='tab-4'),
    ]),
    html.Div(id='tabs-content-inline')
])


# ==============================================================
# 定义回调
@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])
    else:
        return html.Div([
            html.H3('Error!')
        ])


server = app.server

# ==============================================================
# 主函数运行
if __name__ == '__main__':
    app.run_server(debug=True)
