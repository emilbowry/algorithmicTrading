import chart_studio.plotly as plotly
import plotly.offline as pyoff
import plotly.graph_objs as go

import plotly.graph_objs as go
import plotly.figure_factory as ff


import numpy as np
import pandas as pd
import scipy

from scipy import signal, stats


def h(fc,b):
   b = 0.08  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).
   N = int(np.ceil((4 / b))) #
   if not N % 2: N += 1  # Make sure that N is odd.
   n = np.arange(N)

   # Compute sinc filter.
   h = np.sinc(2 * fc * (n - (N - 1) / 2))

   # Compute Blackman window.
   w = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + \
   0.08 * np.cos(4 * np.pi * n / (N - 1))

   # Multiply sinc filter by window.
   h = h * w

   # Normalize to get unity gain.
   h = h / np.sum(h)
   return h

