import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import scipy
from scipy import signal, stats


from FourierTransforms.sincFunc import h

def highPass(data,fc,b=0):
    cutOff=round((1/(15*60*60)),28) #1/15min freq
    b=round((cutOff/fc),28)

    h_high1 = -h
    # h_highD =h_high1[int(())]

    d2=list(data[data.columns[1]])
    y = np.convolve(d2, h(fc,b))
    x = data[data.columns[0]]

    def getTrace(xf=x, yf=y):
        trace1 = go.Scatter(
            x=list(x),
            y=list(y),
            mode='lines',
            name='High-Pass Filter',
            marker=dict(
                color='#C54C82'
            )
        )

        layout = go.Layout(
            title='Low-Pass Filter',
            showlegend=True
        )

        return trace1, layout

    #fig = go.Figure(data=trace_data, layout=layout)
    #pyoff.plot(fig, filename='fft-high-pass-filter')