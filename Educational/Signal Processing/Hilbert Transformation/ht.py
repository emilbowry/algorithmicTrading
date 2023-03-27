from scipy.signal import hilbert
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

data = pd.read_csv("../EURUSD.csv")
data=data[0:1000]
data2 = pd.DataFrame({"Date Time":[],"Value":[]})
data2["Date Time"] = data["Date Time"]
zoData = stats.zscore(data["Value"])
data2["Value"] = zoData
data3 = data2["Value"]

plt.plot(data3)

analytical_signal = hilbert(data3)
plt.plot(analytical_signal.real)
plt.plot(analytical_signal.imag)


amplitude_envelope = np.abs(analytical_signal)
plt.plot(amplitude_envelope)
plt.show()