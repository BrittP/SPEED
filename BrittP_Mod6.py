__author__ = 'Britt'
import math, sys
import numpy as np

bogus = np.genfromtxt('C:\Users\Britt\Dropbox\Fall2015\SPEED\Bogus2014.csv', delimiter=',', skip_header=1)

temp = bogus[:, 0]
humidity = bogus[:, 1]


# print temp
# print humidity

def getSVP(t):
    SVPList = []
    for t in temp:
        if t <= 0:
            svpSol = 0.6108 * math.exp((21.88 * t) / (265.5 + t))
            SVPList.append(svpSol)

        else:
            svpLiq = 0.6108 * math.exp((17.27 * t) / (t + 237.3))
            SVPList.append(svpLiq)

    return SVPList


SVP = getSVP(temp)
for t, s in zip(temp, SVP):
    print 'For temperature %f degrees Celsius your saturated vapor pressure is %.4g' % (t, s)


def getVP(s, r):
    VPList = []
    for s, r in zip(SVP, humidity):
        VP = (s * r)/100
        VPList.append(VP)
    return VPList


VP = getVP(SVP, humidity)
for h, s in zip(humidity, VP):
    print 'For %f percent humidity the vapor pressure is %f' % (h, s)


def getVPD(s, v):
    VPDList = []
    for s, v in zip(SVP, VP):
        VPD = s - v
        VPDList.append(VPD)
    return VPDList


VPD = getVPD(SVP, VP)
for v, t, r in zip(VPD, temp, humidity):
    print 'This is my VPD %.2f in Bogus in 2014. The temperature was %.2f and the humidity %.2f' % (v, t, r)
