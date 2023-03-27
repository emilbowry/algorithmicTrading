import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import scipy
from scipy import signal, stats
from sincFunc import h

def lowpass(data,f,b=0.08):
    cuttOffFreq=(1/(60*2)) #1/5min freq
    fc=cuttOffFreq/f
    d2=list(data[data.columns[1]])
    y = np.convolve(d2, h(fc,b))
    x = data[data.columns[0]]
    return x,y