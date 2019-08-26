from urllib import request as re

url = 'http://www.baidu.com/'

res = re.urlopen(url=url).read().decode('utf-8')
print(res)
