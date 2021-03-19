# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入要翻译的内容：")
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = content
    data['from'] = "zh-CHS"
    data['to'] = 'en'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '16155345197872'
    data['sign'] = 'eac2d7f18ec5ff7229eae7b2f195315a'
    data['lts'] = '1615534519787'
    data['bv'] = '3d91b10fc349bc3307882f133fbc312a'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'

    print(data)
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url,data)
    print(response)
    html = response.read().decode('utf-8')
    print(html)
    target = json.loads(html)
    print(target)

    time.sleep(5)


