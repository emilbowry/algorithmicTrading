import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go
import plotly.figure_factory as ff


from datetime import datetime
import numpy as np
import pandas as pd
import scipy

from scipy import signal, stats
from scipy.fft import fft, ifft, fftfreq




def fourierTransform(data, samplerate):
    data=list(data[data.columns[1]])
    xf = fftfreq(len(data), samplerate)
    yf = fft(data)


    def getTrace(xf=xf, yf=yf):

        trace1 = go.Scatter(
            x=xf,
            y=np.abs(yf),
            mode='lines',
            name='Fourier Transform',
            marker=dict(
                color='#C54C82'
            )
        )

        layout = go.Layout(
            title='Fourier Transform',
            showlegend=True
        )


        return trace1, layout
        #fig = go.Figure(data=trace_data, layout=layout)


    return xf,yf




