import random
import numpy as np
import matplotlib.pyplot as plt
import time

def calcHist(tdata):
    hist = [0] * 10
    for i in range(0, len(tdata)):
        hist[tdata[i] // 100] += 1
    return hist

def funcRandomNumbers():
    data=[random.randint(0, 999) for i in range(1000000)]
    #print("Значения массива случайных чисел",data)
    return data


def initListWithRandomNumbers():
    rand_list = []
    n = 1000
    for i in range(n):
        rand_list.append(random.randint(0, 999))
    return rand_list

def Time(Ttime):
    for i in range(Ttime):
        start = time.time()
        calcHist(tdata)
        end = time.time()
        mean=end-start
        listTime.append(mean)
        print(i,"time)","Runtime of the calcHist is ", (mean))
    print(listTime)
    return listTime

def calcInfo(listTime):
    summ = 0
    for val in listTime:
        summ = summ + val
    meanOfList=summ/len(listTime)
    print("Среднее значение",meanOfList)
    print("Минимальное значение",min(listTime))
    print("Максимально значение",max(listTime))

def gisto(hist):
    x=np.arange(1,11)
    fig,ax=plt.subplots()
    ax.bar(x,hist)
    plt.ylim([98000,105000])
    plt.title("Гистограмма распределения")
    plt.xlabel("Интервалы")
    plt.ylabel("'Элементы")
    plt.grid()
    plt.show()


tdata=funcRandomNumbers()
gisto(calcHist(tdata))
hist=calcHist(tdata)
print(hist)
listTime=[]
Time(100)
calcInfo(listTime=listTime)
