from urllib.request import  Request,urlopen
from  urllib.error import  URLError
#url = 'https://www.jiabiango.com/xxoo'
#url = 'https://www.xiniaoxi.com/'
url = 'https://www.google.com/'
req =Request(url)
try:
    response = urlopen(url)
except URLError as e:
    if hasattr(e,'code'):
        print('The server couldn\`t fulfill the request.')
        print('Error code:', e.code)
    elif hasattr(e,'reason'):
        print('we failled to a server')
        print('reason:', e.reason)

else:
    pass
    print(response.getcode())