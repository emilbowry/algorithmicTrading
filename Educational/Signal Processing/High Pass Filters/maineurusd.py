import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from fourier import displayfourier, fourier
from lowpass import butter_lowpass_filter

data=pd.read_csv("EURUSD.csv")

N=1000
d1 = data.head(N)


d1.plot()
#plt.show()

startDate = d1.at[0,"Date Time"]
endDate=d1.at[N-1,"Date Time"]

starttime = pd.to_datetime(startDate, infer_datetime_format=True).timestamp()
endtime = pd.to_datetime(endDate, infer_datetime_format=True).timestamp()

delta=endtime-starttime

samplerate=N/delta



print(delta)

xf,yf = fourier(d1["Value"], samplerate)

#displayfourier(d1["Value"], samplerate)
butter_lowpass_filter(yf, 2, samplerate, 2, xf)
