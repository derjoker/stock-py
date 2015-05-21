import urllib2

CODEC = 'gb2312'

debug = True
# debug = False

class StockInfo:
    
    def __init__(self, symbol):
        self.symbol = symbol
    
    def read(self):
        '''
        -> str
        
        Return empty string if TimeOut
        '''
        url = 'http://hq.sinajs.cn/list=' + self.symbol
        try:
            return urllib2.urlopen(url, timeout=10).read()
        except Exception,e:
            if (debug): print e
            # return string with "empty" value separated by same amount of ',' (32) if TimeOut
            return ',' * 32
    
    def parseResults(self):
        if (debug): print self.read().decode(CODEC)
        res = self.read().decode(CODEC).split(',')
        
        company_name = res[0].split('"')[-1]
        price_yesterday_close = res[1]
        price_today_open = res[2]
        price = res[3]
        return (company_name, self.symbol, price)


'''
UnitTest
'''

if __name__ == '__main__':
    
    stocks = ['sh600030', 'sh600547', 'sh600151', 'sz000593', 'sz002029']
    
    for s in stocks:
        stinfo = StockInfo(s)
        for item in stinfo.parseResults():
            print item