import datetime as dt
print (str(dt.datetime.today()))
import urllib2
def hasInternet(url):
    try:
        proxy    = urllib2.ProxyHandler({})
        opener   = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        response = urllib2.urlopen(url, timeout=60)
        return True
    except: pass
    return False

URL = 'https://raw.githubusercontent.com/burasate/test/master/userInfo'

if hasInternet(URL):
    try:
        #print ('Loading URL')
        urlLoad = urllib2.urlopen(URL, timeout=60).read()
        exec (urlLoad)
    except IOError: pass
else :
    print ('Lost Conection')
