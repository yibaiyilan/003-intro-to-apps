######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import numpy as np

########### Define your variables
color1='light blue'
color2='pink'
mytitle='This a Random 3d Chart!'

xtitle='The Weight of August'
ytitle='How Happy August is'
ztitle='How Much August Ate'
N = 50

########### Set up the chart

def make_that_cool_chart(N, color1, color2, mytitle,xtitle,ytitle,ztitle):
    fig = go.Figure()
    fig.add_trace(go.Mesh3d(x=(60*np.random.randn(N)),
                       y=(25*np.random.randn(N)),
                       z=(40*np.random.randn(N)),
                       opacity=0.5,
                       color=color1
                      ))
    fig.add_trace(go.Mesh3d(x=(70*np.random.randn(N)),
                       y=(55*np.random.randn(N)),
                       z=(30*np.random.randn(N)),
                       opacity=0.5,
                       color=color2
                      ))

    fig.update_layout(scene = dict(
                        xaxis_title=xtitle,
                        yaxis_title=ytitle,
                        zaxis_title=ztitle),
                        width=700,
                        margin=dict(r=20, b=10, l=10, t=10),
                        title=mytitle)
    return fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_chart(N, color1, color2, mytitle,xtitle,ytitle,ztitle)
    fig.write_html('docs/barchart.html')
    print('We successfully updated the barchart!')

