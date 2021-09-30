from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from core import app
from dash.dependencies import Input, Output, State, MATCH, ALL
# 引入自定义组件
from src.components.article import creat_article
from src.components.vtk import creat_vtk
from src.components.ploty import creat_ploty


# 单例模式，设置容器及内部元素id
class ResearchIDs(object):
    _status = None

    def __init__(self):
        ResearchIDs._status = self
        self._id_num = 0

    @classmethod
    def get_instance(cls):
        if ResearchIDs._status is None:
            raise RuntimeError(u"未初始化，请先初始化！")
        return ResearchIDs._status

    # 增加编号(1e8应该达不到=-=)
    def add_id(self):
        self._id_num = (self._id_num + 1) % 100000000

    # 获得当前id
    def get_id(self):
        # 获取id后就要+1
        self.add_id()
        return str(self._id_num)


# 实例化单例
research_id_num = ResearchIDs()


# 获取可视化内容区域
def get_card_body(research_introduction):
    introduction_list = []
    for i_introduction in research_introduction:
        type_tem = i_introduction["type"]
        if type_tem == 'article':
            introduction_tem = creat_article(i_introduction['content'][0], i_introduction['content'][1])
        elif type_tem == 'vtk':
            introduction_tem = creat_vtk(i_introduction['content'])
        elif type_tem == 'ploty':
            introduction_tem = creat_ploty(i_introduction['content'])
        else:
            introduction_tem = html.H1('Cant Resolve! Please Check!',
                                       style={'color': 'red', 'border': 'red dotted 2px', 'textAlign': 'center'})
        introduction_list.append(introduction_tem)
    return html.Div(introduction_list)


# 新建research模块
def creat_research(research_content):
    research_list = []
    for i_search in research_content:
        id_num = research_id_num.get_id()
        research_list.append(
            html.Div(
                id='research_div' + id_num,
                className='research_div',
                children=[
                    creat_article(i_search['describe'][0], i_search['describe'][1]),
                    dbc.Button(
                        "查看更多",
                        id={
                            "type": "research_collapse_button",
                            "index": id_num
                        },
                        className="research_collapse_button", color="info", n_clicks=0,
                    ),
                    dbc.Collapse(
                        dbc.Card(
                            id="research_card" + id_num,
                            className="research_card",
                            children=dbc.CardBody(
                                id="research_cardBody" + id_num,
                                className="research_cardBody",
                                children=get_card_body(i_search['introduction'])
                            )
                        ),
                        id={
                            "type": "research_collapse",
                            "index": id_num
                        },
                        className="research_collapse", is_open=False,
                    ),
                ]
            )
        )
    return html.Div(children=research_list)


@app.callback(
    Output({'type': 'research_collapse', 'index': MATCH}, "is_open"),
    [Input({'type': 'research_collapse_button', 'index': MATCH}, "n_clicks")],
    [State({'type': 'research_collapse', 'index': MATCH}, "is_open")],
)
def toggle_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open
