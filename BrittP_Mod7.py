import math, sys
import numpy as np
import BrittP_Mod6 as M6

bogus = np.genfromtxt(sys.argv[1], delimiter = ',', skip_header = 1)

temp = bogus[:,0]
humidity = bogus[:,1]


SVP = M6.getSVP(temp)
VP = M6.getVP(SVP, humidity)
VPD = M6.getVPD(SVP, VP)
