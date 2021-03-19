import urllib.request
import random

url = "http://www.whatismyip.com.tw"
iplist = ['182.34.26.189:9999','175.43.86.238:9999','175.42.123.234:9999']

#proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
proxy_support = urllib.request.ProxyHandler({'http':'127.0.0.1:1080'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent' ,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36')]
#help(opener.addheaders)
urllib.request.install_opener(opener)

response =urllib.request.urlopen(url)
print(response)
html=response.read().decode('utf-8')
print(html)
