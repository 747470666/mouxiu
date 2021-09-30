from dash import html
from dash import dcc

from src.components.article import creat_article
from src.components.page_head import page_head


# 后期可以设置为自动加载文章，目前暂时作为测试
def index_page(style):
    return html.Div(
        id='body_index', className=style,
        children=[
            page_head(style, '主页'),
            creat_article(
                [
                    {'src': '', 'width': 0},
                    {'src': 'assets/static/images/computer.png', 'width': 0.3},
                    {'src': 'assets/static/images/running.gif', 'width': 0.4},
                ],
                [
                    '''
                    1. [中国科学院](https://www.cas.cn/)
                    2. [中国国家航天局](http://www.cnsa.gov.cn/index.html)
                    3. [ESA-欧洲空间局](https://www.esa.int/)
                    4. [NASA-美国国家航空航天局](https://www.nasa.gov/)
                    ''',
                    '''
                    # 谋秀 - VSWBD科研小站 (Virtual Science Web Base-on Dash)
                    **本项目目前由*汪颖*独立开发，目标是为科研工作者提供简单可用的个人网站建设**
                    > Dash是一个很强大的全栈包（React for Python），整体代码采用Python开发，大大增加了可读性与减少了工程量，在不追求高并发、强交互的要求下是非常合适的开发选择。
                    ## [Open Dash](https://github.com/plotly/dash)
                    ### *Dash is the most downloaded, trusted Python framework for building ML & data science web apps*.
                    #### 如何使用
                    在你的`terminal`中, 下载包 `dash`：
                    ```bash
                    pip install dash
                    ```
                    在国内，我推荐使用`pip`代理来下载包：
                    ```bash
                    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple dash
                    ```
                    如果仍然存在问题，我推荐采用`trust`模式来下载：
                    ```bash
                    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn dash
                    ```

                    #### 记住
                    还需要下载pandas
                    ```bash
                    pip install pandas
                    ```
                    还有各种插件
                    ```bash
                    pip install dash-bootstrap-components
                    pip install dash_vtk
                    ```
                    
                    ## 启动
                    ```bash
                    python app.py
                    ```
                    
                    ## 目录结构
                    本项目的初始目录结构及介绍如下
                    ```text
                    |-- project #项目根目录
                        |-- assets #项目使用资源库
                            |-- css 样式库
                            |-- js 脚本库
                            |-- static 静态资源
                        |-- src #页面源文件
                            |-- components #页面组件库
                            |-- pages #页面内容
                        |-- tools #项目工具库
                            |-- router.py #路由配置
                            |-- router_setting.py #在无数据库时的路由基本参数
                            |-- structure.py 页面基本结构
                            |-- style.py 一些结构的样式
                        |-- core.py #引入Dash.app方便回调
                        |-- app.py #App入口
                        |-- README.md #介绍文档
                    ```
                    ''',
                    '''
                    PS：分享以下代码
                    ```py
                    import dash
                    import dash_bootstrap_components as dbc
                    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
                    # 设置允许超级回调，即DOM中一开始并不渲染该id元素，比较危险
                    app.config.suppress_callback_exceptions = True
                    ```
                    ''',
                ],
            )
        ]
    )
