#############################
#
# Get prices
# from yahoo:
# http://chartapi.finance.yahoo.com/instrument/1.0/aapl/chartdata;type=quote;range=1y/csv
# fed rate from :
# http://research.stlouisfed.org/fred2/data/FEDFUNDS.txt

import urllib2
import time
from datetime import datetime

stockToPull = 'AAPL'

def pullData(stock):
    try:
        fileLine = stock + '.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/%s/chartdata;type=quote;range=1y/csv' % (stock)
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
        
        for curline in splitSource:
            splitLine = curline.split(',')
            if len(splitLine) == 6:
                if 'values' not in splitLine[0]:
                    saveFile = open('C:\\Users\\throbby\\Documents\\' + fileLine,'a')
                    lineToWrite = curline + '\n'
                    saveFile.write(lineToWrite)
        print 'Pulled %s' % (stock.upper())
    except Exception,e:
        print 'main loop',str(e)    

def pullRate():
    try:
        fileLine = 'rates.txt'
        urlToVisit = 'http://research.stlouisfed.org/fred2/data/FEDFUNDS.txt'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        saveFile = open('C:\\Users\\throbby\\Documents\\' + fileLine,'a')
        dateLines = sourceCode.split('\r\n')
        for curLine in dateLines[61:-1]:
            curline = curLine.replace('-','')
            curline = curline.split()
            outputLine = curline[0] + ',' + curline[1] + '\n'
            saveFile.write(outputLine)
        
    except Exception,e:
        print 'main loop',str(e)