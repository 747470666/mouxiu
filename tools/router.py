# router是路由组件工具
from tools.structure import PageStruct


def route_page(pathname):
    page_struct = PageStruct.get_instance()
    if pathname == '/':
        return [
            page_struct.my_head('page1'),
            page_struct.my_body('page1'),
            page_struct.my_foot('page1'),
        ]
    elif pathname == '/research':
        return [
            page_struct.my_head('page2'),
            page_struct.my_body('page2'),
            page_struct.my_foot('page2'),
        ]
    elif pathname == '/mine':
        return [
            page_struct.my_head('page3'),
            page_struct.my_body('page3'),
            page_struct.my_foot('page3'),
        ]
    else:
        return '404'
