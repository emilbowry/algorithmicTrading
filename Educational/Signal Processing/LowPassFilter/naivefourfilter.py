import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go
import plotly.graph_objs as go
import plotly.figure_factory as ff
from scipy import signal, stats
from scipy.fft import fft, ifft, fftfreq
import fourier


from datetime import datetime
import numpy as np
import pandas as pd
import scipy

from scipy import signal, stats
from scipy.fft import fft, ifft, fftfreq


def naiveFilter(data, samplerate):


    x,y = fourier.fourierTransform(data, samplerate)
    x2=list(data[data.columns[0]])
    cutoffAm=10
    cutoff = int(len(y)/cutoffAm)
    y=y[0:cutoff]

    print("b")
    print(np.max(np.real(y)))
    print(x[np.argmax(np.real(y))])
    y = ifft(y)

    return x2,np.real(y)