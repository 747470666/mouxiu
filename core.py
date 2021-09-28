import dash

app = dash.Dash(__name__)

# 设置允许超级回调，即DOM中一开始并不渲染该id元素，比较危险
app.config.suppress_callback_exceptions = True
