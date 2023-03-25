import numpy as np
from scipy.fft import fft, ifft, fftfreq
import pandas as pd
import scipy.stats as stat

import matplotlib.pyplot as plt


def displayfourier(data, sampleRate):
   data = stat.zscore(data)
   data = np.array(data)
   xf = fftfreq(data.size, sampleRate)
   yf = fft(data)

   plt.plot(xf,yf)
   plt.show()

