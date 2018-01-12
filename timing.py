# -*- coding: utf-8 -*-

import timeit
from math import ceil,floor
from pprint import pprint
import random
from timeit import Timer
from DataStructures import Node, LinkedList, Stack, HashTable
from collections import OrderedDict,Counter
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.font_manager import FontProperties
import sys
import time
import numpy
import multiprocessing as mp
from functools import partial
sys.setrecursionlimit(50000)
plt.rcParams['lines.linewidth'] = 1 


""" Test Functions """

#Recursive Fibonacci (Exponential Time)
def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

#Iterative Fibonacci w/ Storing (Linear Time)
def fib2(n):
    if n == 0:
        return 0

    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

def getRatio():
    c = 0
    while c <= 1:
        print "c = " + str(c) + " | c / 1-c = " + str(c/(1-c))
        c = c + .001
    return

finalTimes = []
startTime = None
def genList(x):
    return random.sample(xrange(x), x)

"""Returns best case runtime of a function in nanoseconds (μs). """

def time_function(fName,fCall,numCalls):
    t = timeit.Timer(fCall,"from __main__ import " + fName)
    return t.timeit(numCalls) * 1000


""" New Complexity Function """

def complexity2(fName,argType=None,numCalls=1,startSize=1,endSize=1000,stepSize=1,showGraph=True):
    inputSizes, times, benchSizes, benchTimes = [],[],[],[]
    currSize = startSize
    totalTime = 0

    while currSize <= endSize:
        fCall = ''
        if argType == int:
            fCall = str(fName) + "(" + str(currSize) + ")"
        elif argType == list:
            fCall = str(fName) + "(" + str(genList(currSize)) + ")"
        elif argType == None:
            fCall = str(fName) + "()"
        else:
            print 'Unsupported Argument Type. Function must take in 0 arguments OR an integer OR a list.'
            return
        
        time = time_function(fName,fCall,numCalls) # Call function w/ current input size
        
        if endSize % currSize == 0:
            if argType == list:
                print "Call: " + fName + '(list of length ' + str(currSize)  + ") | Runtime (milliseconds): " + str(round(time,2)) 
            else:  
                print "Call: " + fCall + " | Runtime (milliseconds): " + str(round(time,2))

        inputSizes.append(currSize)
        times.append(time)

        benchSizes.append(currSize-0.5)
        benchTimes.append(time)

        totalTime += time
        currSize = currSize + stepSize

    # Display Results
    secs = round(totalTime / 1000,2)
    millisecs = round(totalTime,2)
    if secs != 0.0:
        print "Total running time: " + str(millisecs) + " ms (" + str(secs) + " s)"
    else:
        print "Total running time: " + str(millisecs) + " ms"
    
    if showGraph:
        show_graph(fName,inputSizes,times,benchSizes,benchTimes,startSize,endSize)


""" Shows graph of input size vs. runtime """

def show_graph(fName,inputSizes,times,benchSizes,benchTimes,startSize,endSize):
    coefficients = numpy.polyfit(inputSizes,times,2)
    polynomial = numpy.poly1d(coefficients)
    xs = numpy.arange(startSize,endSize,0.1)
    ys = polynomial(xs)

    slope, intercept, r_value, p_value, std_err = stats.linregress(inputSizes,times)
    print slope

    plt.plot(inputSizes,times,'ro',markersize=3.5,alpha=1.0)
    plt.plot(xs,ys,linewidth=1.5)
    bars = plt.bar(benchSizes,benchTimes,width=1,color='red', edgecolor='black', alpha=0.55,align='edge')
    plt.xlabel('Input Size')
    plt.ylabel('Time (milliseconds)')
    plt.title('Time Complexity of ' + fName)
    plt.ylim(0,max(benchTimes)*1.1)
    plt.xlim(startSize-1,endSize+1)

    plt.show()
    
""" Parallel Time Complexity Function - Not Working """

def pcomplexity(fName,argType=None,numCalls=1,startSize=1,endSize=1000,stepSize=1,showGraph=True):
    inputSizes, times, benchSizes, benchTimes = [],[],[],[]
    currSize = startSize
    totalTime = 0

    pool = mp.Pool(processes=8)
    while currSize <= endSize:
        fCall = ''
        if argType == int:
            fCall = str(fName) + "(" + str(currSize) + ")"
        elif argType == list:
            fCall = str(fName) + "(" + str(genList(currSize)) + ")"
        elif argType == None:
            fCall = str(fName) + "()"
        else:
            print 'Unsupported Argument Type. Function must take in 0 arguments OR an integer OR a list.'
            return
        
        time = pool.apply_async(time_function, (fName,fCall,numCalls)).get() # Call function w/ current input size
        if endSize % currSize == 0:
            if argType == list:
                print "Call: " + fName + '(list of length ' + str(currSize)  + ") | Runtime (milliseconds): " + str(round(time,2)) 
            else:  
                print "Call: " + fCall + " | Runtime (milliseconds): " + str(round(time,2))
        
        inputSizes.append(currSize)
        times.append(time)

        benchSizes.append(currSize-0.5)
        benchTimes.append(time)

        totalTime += time
        currSize = currSize + stepSize

    pool.close()
    #pool.join()
    
    # Display Results
    secs = round(totalTime / 1000,2)
    millisecs = round(totalTime,2)
    if secs != 0.0:
        print "Total running time: " + str(millisecs) + " ms (" + str(secs) + " s)"
    else:
        print "Total running time: " + str(millisecs) + " ms"
    
    if showGraph:
        show_graph(fName,inputSizes,times,benchSizes,benchTimes,startSize,endSize)