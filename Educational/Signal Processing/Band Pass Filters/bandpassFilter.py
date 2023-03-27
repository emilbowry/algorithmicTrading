import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go

import plotly.graph_objs as go
import plotly.figure_factory as ff


import numpy as np
import pandas as pd
import scipy

from scipy import signal, stats

data = pd.read_csv("../EURUSD.csv")
N=1000
d1 = data[0:N]

startDate = d1.at[0,"Date Time"]
endDate=d1.at[N-1,"Date Time"]

starttime = pd.to_datetime(startDate, infer_datetime_format=True).timestamp()
endtime = pd.to_datetime(endDate, infer_datetime_format=True).timestamp()

fL = 0.1
fH = 0.3
b = 0.08
N = int(np.ceil((4 / b)))
if not N % 2: N += 1  # Make sure that N is odd.
n = np.arange(N)

# low-pass filter
hlpf = np.sinc(2 * fH * (n - (N - 1) / 2.))
hlpf *= np.blackman(N)
hlpf = hlpf / np.sum(hlpf)

# high-pass filter
hhpf = np.sinc(2 * fL * (n - (N - 1) / 2.))
hhpf *= np.blackman(N)
hhpf = hhpf / np.sum(hhpf)
hhpf = -hhpf
hhpf[int((N - 1) / 2)] += 1

h = np.convolve(hlpf, hhpf)
s = list(d1['Value'])
new_signal = np.convolve(s, h)

trace1 = go.Scatter(
    x=list(range(len(new_signal))),
    y=new_signal,
    mode='lines',
    name='Band-Pass Filter',
    marker=dict(
        color='#BB47BE'
    )
)

layout = go.Layout(
    title='Band-Pass Filter',
    showlegend=True
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)
pyoff.plot(fig, filename='fft-band-pass-filter')