import urllib.request
#req = urllib.request.Request('https://m.360buyimg.com/babel/jfs/t1/169647/40/9143/140259/603f66d9E7a868433/9bfc9eb1bdc0cd93.jpg')
#response = urllib.request.urlopen(req)
response = urllib.request.urlopen('https://m.360buyimg.com/babel/jfs/t1/169647/40/9143/140259/603f66d9E7a868433/9bfc9eb1bdc0cd93.jpg')
print(dir(response))
print(response.__dict__)
print(response.geturl())
print(response.info())
print(response.getcode())
help(response.read)
img = response.read()

with open('a.jpg','wb')  as f:
    f.write(img)