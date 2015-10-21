# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:56:24 2015

@author: Britt
"""
#IMPORTING
from __future__ import division
import math
import csv
#from itertools import islice

#OPENING EXCEL FILE
f= open('Treeline_HrlySummary_2014.csv')
csv_f=csv.reader(f)
#for row in islice(csv_f, 30, None):
    
#CREATING LISTS FOR TEMPERATURE & HUMIDITY
tempList = []
rHumList = []
for row in csv_f:
    tempList.append(row[2])
    rHumList.append(row[5])
    
#TURNING VALUES IN LIST FROM STRING TO INTEGER
tempList = map(float, tempList)
rHumList = map(float, rHumList)

#PROOFING
print tempList
print rHumList

#DEFINING SATURATED VAPOR PRESSURE FUNCTION
def getSVP(t):
    for t in tempList:
    #SATURATED VAPOR PRESSURE EQUATION
        if t<=0:
            SVP=0.6108*math.exp((21.88*t)/(265.5+t))  #SOLID
        else:
            SVP=0.6108*math.exp((17.27*t)/(t+237.3)) #LIQUID
        return SVP

#DEFINING ACTUAL VAPOR PRESSURE FUNCTION        
def getVP(getSVP,r):
    for r in rHumList:
        #ACTUAL VAPOR PRESSURE EQUATION
        VP=getSVP*r
        return VP

#DEFINING THE VAPOR PRESSURE DEFICIT FUNCTION    
def getVPD(getSVP, getVP): 
    #VAPOR PRESSURE DEFICIT EQUATION
    VPD=getSVP-getVP
    return VPD

#CREATING LOOP TO IMPLEMENT FUNCTIONS AND OUTPUTTING RESULTS
#THE ZIP FUNCTION ALLOWS FOR THE BOTH LISTS TO BE INTERATED AT THE SAME TIME
for t, r in zip(tempList, rHumList):
    VPD1 = getVPD (t, r) # this is still not right
    print 'Temperature is equal to %.4f, Humidity is equal to %.4f, the Vapor Pressure is %.4f' %(t, r, VPD1)