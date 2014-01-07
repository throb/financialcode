##########################################
# Python Options Pricing Module
#
# - throb@throb.net
#
##########################################

from math import *

# Cumulative normal distribution

def CND(X):

    (a1,a2,a3,a4,a5) = (0.31938153, -0.356563782, 1.781477937, 

                        -1.821255978, 1.330274429)
    L = abs(X)

    K = 1.0 / (1.0 + 0.2316419 * L)

    w = 1.0 - 1.0 / sqrt(2*pi)*exp(-L*L/2.) * (a1*K + a2*K*K + a3*pow(K,3) +

                                               a4*pow(K,4) + a5*pow(K,5))
    if X<0:

        w = 1.0-w

    return w

def blackScholes (curPrice,strikePrice,time,interest,vol):
    d1 =(log(curPrice/strikePrice)+(interest+vol^2/2)*time)/(vol*sqrt(time))
    d2 = d1-vol*sqrt(time)
    

def Blacksholes(cpFlag,s,x,t,r,v):
    '''
    s = stock Price
    x = strike Price of Option
    t = time to expiration in years	
    r = Risk free interest rate
    v = volatility
    '''
    d1 = (log(s/x)+(r+v*v/2.)*t)/(v*sqrt(t))

    d2 = d1-v*sqrt(t)
    if cpFlag=='c':

        return s*CND(d1)-x*exp(-r*t)*CND(d2)

    else:

        return x*exp(-r*t)*CND(-d2)-s*CND(-d1)