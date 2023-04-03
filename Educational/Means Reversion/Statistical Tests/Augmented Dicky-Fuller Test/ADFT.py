import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go
import plotly.figure_factory as ff

from plotly.subplots import make_subplots

import matplotlib.pyplot as plt
fig = make_subplots(rows=2, cols=2)

from cycler import cycler



# Load
data = pd.read_csv('../EURUSD.csv')
data = data.head(1000)

def  getTrace(x,y,title):
        trace1 = go.Scatter(
            x=x,
            y=y,
            mode='lines',
            name=title

        )

        layout = go.Layout(
            title=title,
            showlegend=True
        )


        #trace_data = [trace1]
        return trace1



data['Value_Dif1']  = data["Value"].diff()
data['Value_Dif2'] = data["Value"].diff(2)
data = data.dropna()
result = adfuller(data["Value"])
result1 = adfuller(data['Value_Dif1'])
result2 = adfuller(data['Value_Dif2'])

print(result)
print(result1)
print(result2)
# Visualize
trace = getTrace(data["Date Time"], data["Value"], "euusd")

trace1 = getTrace(data["Date Time"], data['Value_Dif1'], "euusd")

trace2 = getTrace(data["Date Time"], data['Value_Dif2'], "euusd")


fig.add_trace(trace)
fig.add_trace(trace1)
fig.add_trace(trace2)
pyoff.plot(fig, filename="Plots")