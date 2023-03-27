import pywt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal, stats
data  = pd.read_csv("../../EURUSD.csv")
#print(pywt.families())
#wavelet = pywt.Wavelet("haar")
#print(wavelet)
data=data[0:1000]
signalValue = data["Value"]

data2 = pd.DataFrame({"Date Time":[],"Value":[]})
data2["Date Time"] = data["Date Time"]
zoData = stats.zscore(data["Value"])
data2["Value"] = zoData
print(data2["Value"])

def HarrTrans(data):

   y = data["Value"]
   wavelet, detail = pywt.dwt(y, "haar",6)
   return(wavelet,detail)
#def format_array(arr):
#   return "[%s]" % ", ".join(["%.14f" % x for x in arr])

def lowpassOrthoFilterDec(data):
   y = data["Value"]
   #wavelet=pywt.Wavelet("haar",pywt.filter_bank)
   #format=wavelet.de
   a, b = pywt.dwt(y, "haar")
   #return(wavelet,detail)
   return a,b

def lowpassOrthoFilterRec(wavelet):
      a,b = wavelet.rec_lo
      return a,b

def highpassOrthoFilterDec(wavelet):
      a,b = wavelet.dec_hi
      return a,b

def highpassOrthoFilterRec(wavelet):
      a,b = wavelet.rec_hi
      return a,b


wavelet,detail = lowpassOrthoFilterDec(data2)
#harrtup =(wavelet,detail)

#w,d = lowpassOrthoFilterDec(detail)
#w1,d1 = lowpassOrthoFilterRec(detail)

plt.plot(np.linspace(1,len(wavelet), len(wavelet)), wavelet)
plt.plot(np.linspace(1,500, len(data2["Value"])), data2["Value"])
#plt.plot(np.linspace(1,len(d1), len(d1)), d1)


plt.show()