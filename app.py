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
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# ==============================================================
# app的初始化，自动引入assets中的所有资源
from core import app
# 引入自定义框架及组件
from tools.structure import PageStruct
import tools.router as router

# ==============================================================
# 初始化

# 页面结构初始化
# 开关 switch: on/off
# 默认样式 style: string （可以自己设计样式）
mySetting = {
    'head': {
        'style': 'simple',
    },
    'body': {
        'style': 'simple',
    },
    'foot': {
        'style': 'simple',
    },
}
# 结构初始化
page_struct = PageStruct(mySetting)

# ==============================================================
# app入口
app.layout = html.Div(id='app', children=[
    dcc.Location(id='url', refresh=False),
    html.Div(id='page')
])


# ==============================================================
# 定义router响应回调
@app.callback(Output('page', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    return router.route_page(pathname)


server = app.server

# ==============================================================
# 主函数运行
if __name__ == '__main__':
    app.run_server(debug=True)
