double getTimeDouble(double hours, double mins, double secs = 0, double offset=(0))
{
    double doubleHoursToSecs = hours * 3600;
    double minsToSecs = mins * 60;
    return (doubleHoursToSecs + minsToSecs + secs+offset);
}
double getCTimeDouble(double hours, double mins, double secs = 0)
{
    double doubleHoursToSecs = hours * 3600;
    double minsToSecs = mins * 60;
    return (doubleHoursToSecs + minsToSecs + secs);
    }
double CalculateVolume(string symbol)
{
    double bal = AccountInfoDouble(ACCOUNT_BALANCE);
    double actionableBalance =  (bal/riskCalc(bal))/(SymbolInfoDouble(symbol,SYMBOL_ASK));
    double min_vol = SymbolInfoDouble(symbol, SYMBOL_VOLUME_MIN);
    double max_vol = SymbolInfoDouble(symbol, SYMBOL_VOLUME_MAX);
    
    if(actionableBalance<min_vol){
    actionableBalance = min_vol;
    }else if(actionableBalance>min_vol){
    actionableBalance=max_vol;
    }
    
    //double actionableVolume = (MathFloor(actionableBalance));
    //return 3;
    return 1;//(min_vol);
    //return (actionableBalance);
}

double accumulator=0;
double accumulatorOffset=0;
double accumulatorIndex=0;