import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return  html

'''Help on function findall in module re:

findall(pattern, string, flags=0)
    Return a list of all non-overlapping matches in the string.
    
    If one or more capturing groups (捕获组)are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.
    
    Empty matches are included in the result.
    (?:...)  ：非捕获组，即该子组匹配的字符串无法从后边获取
'''

def get_img(html):
    p = r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'     #返回res.group('129.', '129', '107')
    #p = r'(?:(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'
    iplist =  re.findall(p,html)

    for each in iplist:
        print(each)

    '''
    for each in imglist:
        print(each)
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)   '''

if __name__ == '__main__':
    url = 'https://www.kuaidaili.com/free/inha/1/'
    get_img(open_url(url))
