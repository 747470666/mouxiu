# router是路由组件工具
from tools.structure import PageStruct
from tools.router_setting import get_router_setting

# 获取路径的设置
pathname_setting, pagename_setting, tab_id, tab_dict = get_router_setting()


def route_page(pathname):
    page_struct = PageStruct.get_instance()

    if pathname in pathname_setting:
        return [
            page_struct.my_head(tab_dict[pathname]),
            page_struct.my_body(tab_dict[pathname]),
            page_struct.my_foot(tab_dict[pathname]),
        ]
    else:
        return '404'
