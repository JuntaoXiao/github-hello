#import urllib2
#response = urllib2.urlopen("http://www.baidu.com")
#print response.read()

#import urllib2
#request = urllib2.Request("http://www.baidu.com")
#response = urllib2.urlopen(request)
#print response.read()

#import urllib
#import urllib2
#values = {"username":"1016903103@qq.com","password":"xxxx"}
#data = urllib.urlencode(values)
#url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#request = urllib2.Request("url,data")
#response = ("request")
#print response.read()

#values = {}
#values['username'] = "xiaojuntao0509@126.com"
#values['password'] = "19910509@126.com"
#data = urllib.urlencode(values)
#url = "http://www.ximublog.cn/ghost/signin"
#geturl = url + "?"+data
#request = urllib2.Request(geturl)
#response = urllib2.urlopen(request)
#print response.read()

#import urllib2
#import urllib
#url = 'http://www.baidu.com'
#user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
#values = {'username':'caa','password':'xix'}
#headers = {'User-Agent':user_agent}
#data = urllib.urlencode(values)
#request = urllib2.Request(url,data,headers)
#response = urllib2.urlopen(request)
#page = response.read()
#print page

#import urllib2
#response = urllib2.urlopen('http://www.baudi.com',timeout=10)
#requset = urllib2.Request('http://www.xiaojuntao.com')
#try:
#    urllib2.urlopen(requset)
#except urllib2.URLError,e:
#    print e.reason

import urllib2
req = urllib2.Request('http://blog.csdn.net/cqcre1')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print e.code
except urllib2.URLError,e:
    print e.reason
else:
    print"ok"




