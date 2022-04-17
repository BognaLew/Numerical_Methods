from functions import getData, plotData, MACD, plotMACD
from algorithm import algorithm
from halfAlgorithm import halfAlgorithm
from fusionAlgorithm import fusionAlgorithm

data = getData()
plotData(data)

macd, signal = MACD(data)
plotMACD(macd, signal, data["Data"][35:len(data["Data"])])


print(str(1000*data["Otwarcie"][35]))
print("\n964 day period")
print("\n0 days of delay")

a = algorithm(0, 1000*data["Otwarcie"][35])
b = halfAlgorithm(0, 1000*data["Otwarcie"][35])
c = fusionAlgorithm(0, 1000*data["Otwarcie"][35])
for i in range(0, 964):
    a.decide(macd[i], macd[i+1], signal[i], signal[i+1], data["Otwarcie"][i+35])
    b.decide(macd[i], macd[i+1], signal[i], signal[i+1], data["Otwarcie"][i+35])
    c.decide(macd[i], macd[i+1], signal[i], signal[i+1], data["Otwarcie"][i+35])


print("\nalgorithm:")
a.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])
print("\nhalfAlgorithm:")
b.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])
print("\nfusionAlgorithm:")
c.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])

print("\n1 days of daley")

a = algorithm(0, 1000*data["Otwarcie"][35])
b = halfAlgorithm(0, 1000*data["Otwarcie"][35])
c = fusionAlgorithm(0, 1000*data["Otwarcie"][35])
for i in range(1, 964):
    a.decide(macd[i-1], macd[i], signal[i-1], signal[i], data["Otwarcie"][i+35])
    b.decide(macd[i-1], macd[i], signal[i-1], signal[i], data["Otwarcie"][i+35])
    c.decide(macd[i-1], macd[i], signal[i-1], signal[i], data["Otwarcie"][i+35])


print("\nalgorithm:")
a.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])
print("\nhalfAlgorithm:")
b.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])
print("\nfusionAlgorithm:")
c.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])

print("\n2 days of daley")

a = algorithm(0, 1000*data["Otwarcie"][35])
b = halfAlgorithm(0, 1000*data["Otwarcie"][35])
c = fusionAlgorithm(0, 1000*data["Otwarcie"][35])
for i in range(2, 964):
    a.decide(macd[i-2], macd[i-1], signal[i-2], signal[i-1], data["Otwarcie"][i+35])
    b.decide(macd[i-2], macd[i-1], signal[i-2], signal[i-1], data["Otwarcie"][i+35])
    c.decide(macd[i-2], macd[i-1], signal[i-2], signal[i-1], data["Otwarcie"][i+35])


print("\nalgorithm:")
a.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])
print("\nhalfAlgorithm:")
b.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])
print("\nfusionAlgorithm:")
c.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])

print("\n3 days of daley")

a = algorithm(0, 1000*data["Otwarcie"][35])
b = halfAlgorithm(0, 1000*data["Otwarcie"][35])
c = fusionAlgorithm(0, 1000*data["Otwarcie"][35])
for i in range(3, 964):
    a.decide(macd[i-3], macd[i-2], signal[i-3], signal[i-2], data["Otwarcie"][i+35])
    b.decide(macd[i-3], macd[i-2], signal[i-3], signal[i-2], data["Otwarcie"][i+35])
    c.decide(macd[i-3], macd[i-2], signal[i-3], signal[i-2], data["Otwarcie"][i+35])


print("\nalgorithm:")
a.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])
print("\nhalfAlgorithm:")
b.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])
print("\nfusionAlgorithm:")
c.printWallet(data["Otwarcie"][999], 1000*data["Otwarcie"][35])

print("31 day period")
print("\n0 days of delay")

a = algorithm(0, 1000*data["Otwarcie"][35])
b = halfAlgorithm(0, 1000*data["Otwarcie"][35])
c = fusionAlgorithm(0, 1000*data["Otwarcie"][35])
print(str(1000*data["Otwarcie"][35]))
for i in range(0, 31):
    a.decide(macd[i], macd[i+1], signal[i], signal[i+1], data["Otwarcie"][i+35])
    b.decide(macd[i], macd[i+1], signal[i], signal[i+1], data["Otwarcie"][i+35])
    c.decide(macd[i], macd[i+1], signal[i], signal[i+1], data["Otwarcie"][i+35])


print("\nalgorithm:")
a.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
print("\nhalfAlgorithm:")
b.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
print("\nfusionAlgorithm:")
c.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])

print("\n1 days of daley")

a = algorithm(0, 1000*data["Otwarcie"][35])
b = halfAlgorithm(0, 1000*data["Otwarcie"][35])
c = fusionAlgorithm(0, 1000*data["Otwarcie"][35])
for i in range(1, 31):
    a.decide(macd[i-1], macd[i], signal[i-1], signal[i], data["Otwarcie"][i+35])
    b.decide(macd[i-1], macd[i], signal[i-1], signal[i], data["Otwarcie"][i+35])
    c.decide(macd[i-1], macd[i], signal[i-1], signal[i], data["Otwarcie"][i+35])


print("\nalgorithm:")
a.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
print("\nhalfAlgorithm:")
b.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
print("\nfusionAlgorithm:")
c.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])

print("\n2 days of daley")

a = algorithm(0, 1000*data["Otwarcie"][35])
b = halfAlgorithm(0, 1000*data["Otwarcie"][35])
c = fusionAlgorithm(0, 1000*data["Otwarcie"][35])
for i in range(2, 31):
    a.decide(macd[i-2], macd[i-1], signal[i-2], signal[i-1], data["Otwarcie"][i+35])
    b.decide(macd[i-2], macd[i-1], signal[i-2], signal[i-1], data["Otwarcie"][i+35])
    c.decide(macd[i-2], macd[i-1], signal[i-2], signal[i-1], data["Otwarcie"][i+35])


print("\nalgorithm:")
a.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
print("\nhalfAlgorithm:")
b.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
print("\nfusionAlgorithm:")
c.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])

print("\n3 days of daley")

a = algorithm(0, 1000*data["Otwarcie"][35])
b = halfAlgorithm(0, 1000*data["Otwarcie"][35])
c = fusionAlgorithm(0, 1000*data["Otwarcie"][35])
for i in range(3, 31):
    a.decide(macd[i-3], macd[i-2], signal[i-3], signal[i-2], data["Otwarcie"][i+35])
    b.decide(macd[i-3], macd[i-2], signal[i-3], signal[i-2], data["Otwarcie"][i+35])
    c.decide(macd[i-3], macd[i-2], signal[i-3], signal[i-2], data["Otwarcie"][i+35])


print("\nalgorithm:")
a.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
print("\nhalfAlgorithm:")
b.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
print("\nfusionAlgorithm:")
c.printWallet(data["Otwarcie"][65], 1000*data["Otwarcie"][35])
