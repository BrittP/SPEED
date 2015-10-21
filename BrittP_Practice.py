import sys
import numpy as np


bogus = np.genfromtxt('C:\Users\Britt\Dropbox\Fall2015\SPEED\Bogus2014.csv', delimiter=',', skip_header=1)

temp = bogus[:, 0]
humidity = bogus[:, 1]


def getSVP(temp):
    if temp.all() <= 0:
        svpSol = 0.6108 * np.exp((21.88 * temp) / (265.5 + temp))
        print svpSol

    else:
        svpLiq = 0.6108 * np.exp((17.27 * temp) / (temp + 237.3))
        print svpLiq


def getVP(temp, humidity):
    VP = np.multiply(getSVP(temp), humidity)
    print 'For temperature %.1d degrees Celsius and % percent humidity your vapor pressure is %.2d' % (temp, humidity, VP)


def getVPD(temp, humidity):
    VPD = np.subtract(getSVP(temp) - getVP(temp, humidity))
    print 'This is my VPD %.2f in Bogus in 2014. The temperature was %.2f and the humidity %f' % (VPD,temp, humidity)
