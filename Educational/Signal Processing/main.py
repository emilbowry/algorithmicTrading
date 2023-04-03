import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.graph_objects as go
import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import scipy
from scipy import signal, stats
from plotly.subplots import make_subplots

from FourierTransforms.fourier import fourierTransform
from FourierTransforms.dominantPeriod import domFreqWave
from LowPassFilter.lowpass import lowpass
from LowPassFilter.naivefourfilter import naiveFilter


fig = make_subplots(rows=2, cols=2)

data=pd.read_csv("EURUSD.csv")

N=1000
d1 = data.head(N)


startDate = d1.at[0,"Date Time"]
endDate=d1.at[N-1,"Date Time"]

starttime = pd.to_datetime(startDate, infer_datetime_format=True).timestamp()
endtime = pd.to_datetime(endDate, infer_datetime_format=True).timestamp()

delta=(endtime-starttime)/1000


samplerate=N/delta
print("a")
print(delta)
print(samplerate)

zoDF = pd.DataFrame({"Date Time":[],"Value":[]})
zoDF["Date Time"] = d1["Date Time"]
zoData = stats.zscore(d1["Value"])
zoDF["Value"] = zoData
def  getTrace(x,y,title):
        trace1 = go.Scatter(
            x=x,
            y=y,
            mode='lines',
            name=title,
            marker=dict(
                color='#C54C82'
            )
        )

        layout = go.Layout(
            title=title,
            showlegend=True
        )


        #trace_data = [trace1]
        return trace1



x,y = fourierTransform(zoDF, samplerate)
fttrace_data = getTrace(list(x),list(np.abs(y)),"FT")
x1,y1= lowpass(zoDF,samplerate)
lptrace_data = getTrace(list(x1),list(y1),"LPF")

lpdf = pd.DataFrame({"Date Time":[],"Value":[]})
lpdf["Date Time"] = x1
y1=list(y1[0:1000])
lpdf["Value"]=y1
x2,y2=naiveFilter(zoDF,samplerate)
nftrace_data = getTrace(list(x2),list(y2),"NF")
x3,y3 = domFreqWave(lpdf,delta,samplerate)
dftrace_data = getTrace(list(x3),list(y3),"DFW")
#print(trace_data)
fig.add_trace(fttrace_data,row=1,col=1)
fig.add_trace(lptrace_data,row=1,col=2)
fig.add_trace(nftrace_data,row=2,col=1)
fig.add_trace(dftrace_data,row=2,col=2)

pyoff.plot(fig, filename='Plots')
