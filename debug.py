import logging
logging.basicConfig(level=logging.INFO)         #允许你指定记录信息的级别

s = '0'
n = int(s)
logging.info('n = %d' % n)
#help(logging.info)
print(10 / n)