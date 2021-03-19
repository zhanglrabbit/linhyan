import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return  html


def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'    #[^"]  脱字符 ^ 如果出现在首位则表示匹配不包含其中的任意字符
    imglist =  re.findall(p,html)
    '''
    for each in imglist:
        print(each)
    '''
    for each in imglist:
        print(each)
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)

'''urlretrieve(url, filename=None, reporthook=None, data=None)
    Retrieve a URL into a temporary location on disk.'''


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/7226898597'
    #aa = open_url(url)
    #print(aa)
    get_img(open_url(url))
