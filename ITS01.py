
import random
import numpy as np
import matplotlib.pyplot as plt
import time


def calcHist(tdata):
    hist = [0] * 10
    b = 1
    c = 1
    q = 1
    w = 1
    e = 1
    r = 1
    z = 1
    x = 1
    c = 1
    v = 1
    d = 1
    hist = [0] * 10
    for i in range(0, len(tdata)):
        a = tdata[i]
        if a <= 99:
            hist[0] = b
            b += 1
        elif (99 < a and a <= 199):
            hist[1] = c
            c += 1
        elif (199 < a and a <= 299):
            hist[2] = q
            q += 1
        elif (299 < a and a <= 399):
            hist[3] = w
            w += 1
        elif (399 < a and a <= 499):
            hist[4] = d
            d += 1
        elif (499 < a and a <= 599):
            hist[5] = e
            e += 1
        elif (599 < a and a <= 699):
            hist[6] = r
            r += 1
        elif (699 < a and a <= 799):
            hist[7] = z
            z += 1
        elif (799 < a and a <= 899):
            hist[8] = x
            x += 1
        elif (899 < a and a <= 999):
            hist[9] = v
            v += 1
    #print(hist)
    return hist

def funcRandomNumbers():
    data=[random.randint(0, 999) for i in range(1000000)]
    #print("Значения массива случайных чисел",data)
    return data
tdata=funcRandomNumbers()

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
        #hist = calcHist(tdata=[random.randint(0, 999) for i in range(1000000)])
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
    # fig.set_figheight(5)
    # fig.set_figwidth(10)

    plt.grid()
    plt.show()

gisto(calcHist(tdata))

calcHist(tdata)
listTime=[]
Time(100)
calcInfo(listTime=listTime)