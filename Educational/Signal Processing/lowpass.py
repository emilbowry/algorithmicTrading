import numpy as np
from scipy.signal import butter, lfilter,  butter,filtfilt
import matplotlib.pyplot as plt
import scipy.stats as stat


def butter_lowpass_filter(data, cutoff, signalFreq, order, xf):

    data = stat.zscore(data)
    data = np.array(data)
    # Filter requirements.
    fs =signalFreq     # sample rate, Hz
    cutoff = 2      # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz
    nyq = 0.5 * fs  # Nyquist Frequency
    order = 2       # sin wave can be approx represented as quadratic
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients
    b, a = butter(order, 1, btype='low', analog=True)
    y = filtfilt(b, a, data)

    plt.plot(np.linspace(0,xf,len(y)),y)
    plt.show()






