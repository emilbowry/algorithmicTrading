import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go
import plotly.graph_objs as go
import plotly.figure_factory as ff
from scipy import signal, stats
from scipy.fft import fft, ifft, fftfreq
import fourier
import matplotlib.pyplot as plt

from datetime import datetime
import numpy as np
import pandas as pd
import scipy
from fourier import fourierTransform
from scipy import signal, stats
from scipy.fft import fft, ifft, fftfreq


def domFreqWave(data, delta, samplerate):
    x1,y1=fourierTransform(data,samplerate)

    domfreqIndex = np.argmax(np.real(y1))

    domfreq = x1[domfreqIndex]
    #phaseShift = #np.arctan2(np.imag(y1[domfreqIndex]),np.real(y1[domfreqIndex3]))
    print(domfreqIndex)
    print(domfreq)

    Fs = 212#fix this!!!

    f = samplerate
    sample = delta
    x = np.arange(delta)
    y = np.sin((2 * np.pi * f * x / Fs))

    return x,y

