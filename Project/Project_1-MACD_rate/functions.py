import pandas as pan
import pylab
import matplotlib.dates as dates


def getData():
    data = pan.read_csv("dane.csv", parse_dates=[0])
    data = data.head(1000)

    return data

def plotData(data):
    pylab.gca().xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))
    pylab.gca().xaxis.set_major_locator(dates.DayLocator(interval=200))
    pylab.plot(data["Data"], data["Otwarcie"], label="Cena otwarcia WIG20")
    pylab.gcf().autofmt_xdate()
    pylab.legend()
    pylab.show()

    return

def calculateEMA(N, p):
    alfa = 2/(N+1)
    denominator = 0
    numerator = 0
    for index in range(N-1, 0, -1):
        numerator += ((1-alfa)**index)*p[N-1-index]
        denominator += (1-alfa)**index
    e = numerator/denominator
    return e


def calculateMACD(data):
    macd = []
    list1 = []
    list2 = []
    for j in range(26, 1000):
        for i in range(j - 26, j):
            list1.append(data["Otwarcie"][i])
        for i in range(j - 12, j):
            list2.append(data["Otwarcie"][i])

        macd.append((calculateEMA(12, list2) - calculateEMA(26, list1)))
        list1 = []
        list2 = []
    return macd


def calculateSIGNAL(macd):
    signal = []
    temp = []
    for j in range(9, len(macd)):
        for i in range(j - 9, j):
            temp.append(macd[i])
        signal.append(calculateEMA(9, temp))
        temp = []
    return signal

def MACD(data):
    macd = calculateMACD(data)
    signal = calculateSIGNAL(macd)
    for j in range(0, 9):
        macd.pop(0)

    return macd, signal

def plotMACD(macd, signal, date):
    pylab.gca().xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))
    pylab.gca().xaxis.set_major_locator(dates.DayLocator(interval=200))
    pylab.plot(date, macd, label="Linia MACD")
    pylab.plot(date, signal, label="Linia SIGNAL")
    pylab.gcf().autofmt_xdate()
    pylab.legend()
    pylab.show()

    return
