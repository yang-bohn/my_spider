# -*- coding:utf-8 -*-


import json
import requests


#1.获取目标网址
url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
#2.模拟浏览器实现访问url
data = json.loads(requests.get(url).json()['data'])
#3.从网页源代码中提取数据
china=data['areaTree'][0]['children']



data1=[]
for i in range(len(china)):
    data1.append([china[i]['name'],china[i]['total']['confirm'],china[i]['total']['dead'],china[i]['total']['heal']])


import pandas
data=pandas.DataFrame(data1,columns=['地区','确诊','死亡','治愈'])
data.to_excel("data1.xlsx",index=False)