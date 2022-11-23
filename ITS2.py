import random
import numpy as np


def triangle(a):
    j = 1
    k = 0
    for i in range(4):
        print(a * " ", j * "*" + k * "*")
        a -= 1
        j += 1
        k += 1


def calcHist(tdata):
    hist1 = [0] * 10

    for i in range(0, len(tdata)):
        hist1[tdata[i] // 100] += 1

    return hist1


def funcRandomNumbers():
    data1 = [random.randint(0, 999) for i in range(1000000)]
    # print("Значения массива случайных чисел",data)
    return data1


def histDistanve(hist1, hist2):
    vctr1 = np.array(hist1)
    vctr2 = np.array(hist2)
    vctrSub = sum((vctr1 - vctr2) ** 2)
    distance = vctrSub ** 0.5
    return distance


def writeFile(hist1,hist2):
    np.savez("Histogramms",hist1,hist2)
def readFile():
    read=np.load("Histogramms.npz")
    print(read['arr_0'])
    print(read['arr_1'])



tdata1 = funcRandomNumbers()
hist1 = calcHist(tdata1)
tdata = funcRandomNumbers()
hist2 = calcHist(tdata)
distance = histDistanve(hist1, hist2)
triangle(3)
writeFile(hist1,hist2)
readFile()
print("Гистограмма 1:", hist1)
print("Гистограмма 2:", hist2)
print("Декартово расстояние:" ,distance)

