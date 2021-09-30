from dash import html
from dash import dcc


# 单例模式，设置容器、文章和图片id
class ArticleIDs(object):
    _status = None

    def __init__(self):
        ArticleIDs._status = self
        self._id_num = 0

    @classmethod
    def get_instance(cls):
        if ArticleIDs._status is None:
            raise RuntimeError(u"未初始化，请先初始化！")
        return ArticleIDs._status

    # 增加编号(1e8应该达不到=-=)
    def add_id(self):
        self._id_num = (self._id_num + 1) % 100000000

    # 获得当前id
    def get_id(self):
        # 获取id后就要+1
        self.add_id()
        return str(self._id_num)


# 实例化单例
article_id_num = ArticleIDs()

# 设置图片基础样式（左右流式布局）
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


# 新建article模块，这里是左右流式布局，后面可能要多设置一些样式，这里一切以simple为准
def creat_article(img_src=[], text_content=[], first_position='left'):
    '''
    :param img_src: {'src': 图片链接，没有则为空字符串, 'width': 图片宽度，比例值，最大为1（在手机上强制默认为1）}
    :param text_content: 字符串，段落内容，直接就是文字。
    :param first_position: 第一个图片是左还是右？字符串'left'or'right
    :return:
    '''
    num_record = 0 if first_position == 'left' else 1
    marry_len = min(len(img_src), len(text_content))
    # article是返回的结构
    article_list = []
    for i in range(marry_len):
        img_src_tem = img_src[i]["src"]
        if img_src_tem == '':
            img_style_tem = {
                'minWidth': '0px',
                'width': '0px',
            }
            img_style_tem.update(style_article_img[num_record % 2])
        elif text_content[i] == '':
            img_style_tem = {
                'width': str(img_src[i]["width"] * 100) + '%',
                'marginLeft': str((1-img_src[i]["width"])/2 * 100) + '%',
            }
        else:
            img_style_tem = {
                'width': str(img_src[i]["width"] * 100) + '%',
            }
            img_style_tem.update(style_article_img[num_record % 2])
        id_num = article_id_num.get_id()
        article_list.append(
            html.Div(
                id='article_div' + id_num,
                className='article_div',
                children=[
                    html.Img(id='article_img' + id_num, src=img_src_tem, className='article_img',
                             style=img_style_tem),
                    dcc.Markdown(id='article_md' + id_num, className='article_md', children=text_content[i]),
                ]
            )
        )
        num_record = num_record + 1
    # 多余的图片以居中的方式对齐向下排列（暂定）
    for i in range(marry_len, len(img_src)):
        img_src_tem = img_src[i]["src"]
        id_num = article_id_num.get_id()
        img_style_tem = {
            'width': str(img_src[i]["width"] * 100) + '%',
            'marginLeft': str((1 - img_src[i]["width"]) / 2 * 100) + '%',
        }
        article_list.append(
            html.Div(
                children=[
                    html.Img(id='article_img' + id_num, src=img_src_tem, className='article_img',
                             style=img_style_tem),
                ]
            )
        )
    # 多余的文字以缩小0.1，间距1.2的方式向下延伸（暂定）
    for i in range(marry_len, len(text_content)):
        id_num = article_id_num.get_id()
        article_list.append(
            html.Div(
                children=[
                    dcc.Markdown(id='article_md' + id_num, className='article_md_addition', children=text_content[i])
                ]
            )
        )
    return html.Div(children=article_list)
