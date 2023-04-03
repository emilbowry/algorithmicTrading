import pandas as pd

def computeKelly(winProb, winLossRatio):
    return (winProb-((1-winProb)/winLossRatio))

def computeKellyReturns(returnRate, riskFreeRate, sigma):
    variance = sigma*sigma

def computeWinProb(values, prediction):
    #as pd DF
