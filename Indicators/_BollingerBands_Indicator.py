import Helper
import math

name = 'BollingerBands'
__values = {'multiplier': 0.7, 'length': 20, 'deviation': 2}

def set_values(key, value):
    __values[key] = float(value)

def get_values():
    return __values

def get_points(candles):
    length = int(__values['length'])
    deviation = int(__values['deviation'])
    upband, lowband = __get_bands(candles, length, deviation)
    candle = candles[0]
    low_dif = candle.close - lowband
    up_dif = upband - candle.close
    if low_dif > up_dif:
        value = math.log(low_dif,1.047)
    else:
        value = -math.log(up_dif,1.047)
    
    return value * __values['multiplier']

def __get_bands(candles, length, deviations):
    sma = 0
    for i in range(length):
        sma += candles[i].close
    sma /= length
    bandvalue = 0
    for i in range(length):
        bandvalue += math.pow(candles[i].close - sma,2)
    bandvalue /= length
    bandvalue = math.sqrt(bandvalue)
    upband = sma + (2 * bandvalue)
    lowband = sma - (2 * bandvalue)
    return upband, lowband

    