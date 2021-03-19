import requests
import re
import time

READING_SPEED = 2       #内容阅读速度

class Reptiles:

    def __init__(self):
        pass

    def get_book_array(self, url):
        init_html = requests.get(url)
        author = re.findall(r'<span>(.*)</span>', init_html.text)
        temp = re.findall(r'</span><a href="(.*)</a></dt>', init_html.text)
        ret = []
        for i in range(len(temp)):
            ret.append([temp[i].split(r'">')[1], author[i], temp[i].split(r'">')[0]])
        return ret

    def get_book_chapter(self, url):
        chapter_html = requests.get(url)
        temp = re.findall(r'<dd><a href=\'(.*)</a></dd>', chapter_html.content.decode('utf-8', 'ignore'))
        ret = []
        for i in range(len(temp)):
            ret.append([temp[i].split('\' >')[1], 'http://www.xbiquge.la' + temp[i].split('\' >')[0]])
        return ret

    def get_book_content(self, url):
        content_html = requests.get(url)
        chapter = re.findall(r'<h1>(.*)</h1>', content_html.content.decode('utf-8', 'ignore'))
        temp = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*)<br /><br />', content_html.content.decode('utf-8', 'ignore'))
        content = temp[0].split('\r<br />\r<br />&nbsp;&nbsp;&nbsp;&nbsp;')
        previous_chapter = re.findall(r'投推荐票</a> <a href="(.*)">上一章</a>', content_html.content.decode('utf-8', 'ignore'))[0]
        next_chapter = re.findall(r'&rarr; <a href="(.*)">下一章</a>', content_html.content.decode('utf-8', 'ignore'))[0]
        if next_chapter[-4:] != 'html':
            ret = [chapter, content, url, 'http://www.xbiquge.la' + next_chapter]
        else:
            ret = [chapter[0], content, 'http://www.xbiquge.la' + previous_chapter, 'http://www.xbiquge.la' + next_chapter]
        return ret

    def get_next_page(self, url):
        return  self.get_book_content(url)

    def get_previous_page(self, url):
        return  self.get_book_content(url)

def show_book_type():
    msg = '''
    1.玄幻    2.修真    3.都市    
    4.穿越    5.网游    6.科幻
    '''
    print(msg)
    ret = input('请输入序号选择小说类型：')
    return  isret(ret, [['玄幻'], ['修真'], ['都市'], ['穿越'], ['网游'], ['科幻']]) + 1

def isret(ret, array):
    if ret == '-1':
        return -1
    if ret.isdigit():
        ret = int(ret)
        if ret < -1 or ret > (len(array)+1) or 0 == ret:
            print('输入不在范围！默认选择1【{0}】'.format(array[0][0]))
            ret = 1
    else:
        print('输入非数字！默认选择1【{0}】'.format(array[0][0]))
        ret = 1
    if ret != -1:
        ret = ret - 1
    return  ret

def show_book_name(book_array):
    for n in range(len(book_array)):
        print('{0}.书名：{1} 作者：{2}'.format(n+1, book_array[n][0], book_array[n][1]))
    ret = input('请输入序号选择小说：')
    return  isret(ret, book_array)

def show_book_chapter(book_chapter):
    n = 0
    while n+2 < len(book_chapter):

        print('{:15}\t{:15}\t{:15}\t{:15}\t{:15}'.format(book_chapter[n][0], book_chapter[n+1][0], \
                                                      book_chapter[n+2][0], book_chapter[n+3][0], \
                                                      book_chapter[n+4][0], chr(12288)))
        n = n + 5
        if 0 == n%2:
            i = input('是否继续显示下10章节（1.是|2.不）：')
            if 2 == int(i):
                break
            elif 1 == int():
                pass
            else:
                print('输入错误，默认显示下10章节')
    ret = input('请输入序号选择章节：')
    return  isret(ret, book_chapter)

def show_book_content(book_content):
    print(book_content[0])
    for i in book_content[1]:
        print(i)
        time.sleep(READING_SPEED)
    print('1.上一章        2.下一章')
    ret = input('请输入序号选择：')
    return isret(ret, [[0], [1]])


if __name__ == '__main__':

    while True:
        home_url = ''
        book_type = show_book_type()                          #选择浏览的类型
        if 1 == book_type:
            home_url = 'http://www.xbiquge.la/xuanhuanxiaoshuo/'
        elif 2 == book_type:
            home_url = 'http://www.xbiquge.la/xiuzhenxiaoshuo/'
        elif 3 == book_type:
            home_url = 'http://www.xbiquge.la/dushixiaoshuo/'
        elif 4 == book_type:
            home_url = 'http://www.xbiquge.la/chuanyuexiaoshuo/'
        elif 5 == book_type:
            home_url = 'http://www.xbiquge.la/wangyouxiaoshuo/'
        elif 6 == book_type:
            home_url = 'http://www.xbiquge.la/kehuanxiaoshuo/'
        elif -1 == book_type:
            break
        biqu_pavilion_home = Reptiles()
        book_array = []
        book_array = biqu_pavilion_home.get_book_array(home_url)      #获取书本作者网址数列  [[书名，作者，网址]，]
        while True:
            book_addres = show_book_name(book_array)              #选择书本 获得书本索引
            if -1 == book_addres:
                break
            chapter_url = book_array[book_addres][2]
            chapter_array = biqu_pavilion_home.get_book_chapter(chapter_url)           #获取章节数列    [[章节名，网址]，]
            while True:
                content_address = show_book_chapter(chapter_array)                     #选择章节，获取章节索引
                if -1 == content_address:
                    break
                content_url = chapter_array[content_address][1]
                content_array = biqu_pavilion_home.get_book_content(content_url)           #获取内容       [章节名，[内容, ]，上一章，下一章]
                while True:
                    n = show_book_content(content_array)                  #获取用户选择上下章
                    if -1 == n:
                        break
                    elif 0 == n:
                        content_array = biqu_pavilion_home.get_next_page(content_array[2])
                    elif 1 == n:
                        content_array = biqu_pavilion_home.get_previous_page(content_array[3])
