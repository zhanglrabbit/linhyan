import re

'''正则表达式编译re.compile,得到一个模式对象,r""  原始字符串来表示正则表达式
search(pattern, string, flags=0)  re.search(r'\bclass\b', 'no Class at all',re.I)  flag 标志位'''
print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','255.255.255.255'))
pattern = re.compile(r'(?<![\.\d])(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?![\.\d])')
#pattern = re.compile(r'(?<![\.\d])(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?![\.\d])')
#零宽断言：用于查找特定内容之前或之后的内容，但并不包括特定内容本身(零宽)。类似于^、 $、 \b一样的作用，指定某一位置需要满足某些条件(断言)
print(pattern.fullmatch('255.255.255.255'))

res = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','255.255.255.255')
print(res)
print(res.group())
print(res.group(1))
print(res.group(2))
print(res.group(3))
print(res.groups())
'''Help on built-in function groups:

groups(default=None) method of _sre.SRE_Match instance
    Return a tuple containing all the subgroups of the match, from 1.
'''
#print(res.group(4))
print(res.start())
print(res.end())
print(res.span())

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')  #命名组
print(p.search('Paris in the the spring'))
print(p.search('Paris in the the spring').group())
p1 = re.compile(r'(\b\w+)\s+\1')
print(p1.search('Paris in the the spring'))
print(p1.search('Paris in the the spring').group())
m = re.match(r"([abc])+", "abc")
m1 = re.match(r"(?:[abc])+", "abc")    #不能从非捕获组获得匹配的内容之外，其他的非捕获组跟普通子组没有什么区别了
print(m.group())
print(m1.group())
print(m.groups())
print(m1.groups())
print(re.search(r'(.*[.].*$)', "aa.bat"))
print(re.search(r'(.*[.](?!bat$).*$)', "aa.bat"))
print(re.search(r'(.*[.](?!bat$).*$)', "aa.batc"))
print(re.search(r'(.*[.](?!bat$|exe$).*$)', "aa.exe"))
'''(?=...)
前向肯定断言。如果当前包含的正则表达式（这里以 ... 表示）在当前位置成功匹配，则代表成功，否则失败
(?!...)
前向否定断言。这跟前向肯定断言相反（不匹配则表示成功，匹配表示失败）。'''
