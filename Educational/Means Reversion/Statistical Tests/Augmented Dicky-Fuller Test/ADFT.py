from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np
data = pd.read_csv("../../../EURUSD.csv")

N=1000
data = data.head(N)

res = adfuller(np.array(data["Value"]))

print(res)