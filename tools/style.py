# 这里CSS不好放定义选中样式，这里摆一些特定的样式

def head_tab_selected(style):
    head_tab_selected_style = {
        'none': {},
        'simple': {
            'fontWeight': 'bolder',
        }
    }
    return head_tab_selected_style[style]
