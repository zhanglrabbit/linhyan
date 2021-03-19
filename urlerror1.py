from urllib.request import  Request,urlopen
from  urllib.error import  URLError,HTTPError
#url = 'https://www.jiabiango.com/xxoo'
#url = 'https://www.google.com/'
url = 'https://www.xiniaoxi.com/'
#url = 'https://www.baidu.com/'
req =Request(url)
try:
    response = urlopen(url)
except HTTPError as e:
    print('The server couldn\`t fulfill the request.')
    print('Error code:',e.code)
except URLError as e:
    print('we failled to a server')
    print('reason:' , e.reason)

else:
    pass
    print(response.getcode())