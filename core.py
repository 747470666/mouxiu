import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 设置允许超级回调，即DOM中一开始并不渲染该id元素，比较危险
app.config.suppress_callback_exceptions = True
