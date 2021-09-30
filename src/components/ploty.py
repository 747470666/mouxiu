from dash import html
from dash import dcc

import numpy as np
import plotly.figure_factory as ff

x1,y1 = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u1 = np.cos(x1)*y1
v1 = np.sin(x1)*y1

def creat_ploty(ploty_content):
    return html.Div([
        dcc.Graph(
            figure=dict(
                data=[
                    dict(
                        x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                           2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                        y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                           350, 430, 474, 526, 488, 537, 500, 439],
                        name='Rest of world',
                        marker=dict(
                            color='rgb(55, 83, 109)'
                        )
                    ),
                    dict(
                        x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                           2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                        y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                           299, 340, 403, 549, 499],
                        name='China',
                        marker=dict(
                            color='rgb(26, 118, 255)'
                        )
                    )
                ],
                layout=dict(
                    title='US Export of Plastic Scrap',
                    showlegend=True,
                    legend=dict(
                        x=0,
                        y=1.0
                    ),
                    margin=dict(l=40, r=0, t=40, b=30)
                )
            ),
            style={'height': 300},
            id='my-graph'
        ),
        dcc.Graph(figure=ff.create_quiver(x1, y1, u1, v1))
    ])
