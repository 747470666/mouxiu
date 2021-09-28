# 输入各种页面
from src.pages.index import index_page
from src.pages.research import research_page
from src.pages.about import about_page

# 这里在下面利用了一个双向指向的字典，因此不要有重复的变量名
pathname_setting = ['/', '/research', '/about']
pagename_setting = ['首页', '研究', '关于']

tab_dict = {}
tab_id = []
for i in range(len(pathname_setting)):
    tab_id.append('page' + str(i))
    # 正反都映射好
    tab_dict[pathname_setting[i]] = tab_id[i]
    tab_dict[tab_id[i]] = pathname_setting[i]


def get_router_setting():
    return pathname_setting, pagename_setting, tab_id, tab_dict


page_index_dict = {}
for i in range(len(pathname_setting)):
    page_index_dict['page' + str(i)] = i


def get_router_page(style, page_index):
    pages_list = [
        index_page(style), research_page(style), about_page(style)
    ]
    return pages_list[page_index_dict[page_index]]
