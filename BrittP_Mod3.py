# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:48:57 2015

@author: Britt
"""

# This is a program to convert W/m^2 to mm/day
initialevap=float(raw_input('What is your energy flux in W/msquared?'))

w_msq=1
js_w=1
kg_j=0.00000044248
mcu_kg=0.001
s_hr=3600
hr_day=24
mm_m=1000

evap=initialevap*w_msq*js_w*kg_j*mcu_kg*s_hr*hr_day*mm_m

print 'The evaporation is %e mm per day' % (evap)


