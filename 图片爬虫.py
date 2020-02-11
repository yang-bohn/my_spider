encoding='utf-8'
import urllib.parse
import json
import requests
import jsonpath

# 爬虫的基本思路

# ***分析网站***
# 1.url
url='https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'
wd = '美女'
label = urllib.parse.quote(wd)
print(label)

#2.模拟浏览器请求资源
num = 0
for index in range(0,2400,24):
    url = url.format(label,index)
    we_data = requests.get(url).text
    #3。解析网页，提取数据
    html = json.loads(we_data)
    photo = jsonpath.jsonpath(html,'$..path')
    print(photo)
    # 4.保存数据
    for i in photo:
        a = requests.get(i)
        with open(f'C:\\Users\\yangbowen\\Desktop\\tupian\\{num}.jpg','wb') as f:
            f.write(a.content)
        num+=1
