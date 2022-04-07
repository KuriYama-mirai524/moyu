from cgitb import text
import time
import tkinter as tk
import requests
import simuse
import demjson
import os


path = os.getcwd()
print(path)
with open('data.json', mode='r', encoding='gbk', errors='ignore') as f:
    data = demjson.decode(f.read())
    group1 = data['group']



def down_img():
    headers = {
        'referer': 'http://d.jiek.top/',
        
    }
    resp = requests.get('https://api.j4u.ink/proxy/remote/moyu.json', headers=headers)
    url = resp.json()['data']['moyu_url']
    return url


# 连接到bot
p = simuse.Get_Session(data=data, getsession=1)
data['session'] = p
print(data['group'])
if p != 1:
    print('bot连接成功')
    print('插件启动成功')
    while True:
        msg = simuse.Fetch_Message(data=data, session=p, deal=1)
        
        try:
            key = str(msg[0]['messagechain'][1]['text'])
            group = str(msg[0]['group'])
        
        except:
            group = '无'
        if group in str(group1):
            print(data['word'])
            if '摸鱼' in key:
                url = down_img()
                print(url, '11111')
                print('找到关键词，发送图片')
                post = {
                         "sessionKey": data['session'],
                            "target": group,
                        "messageChain": [
                                        {"type": "Image", "url": str(url)}
                                    ]
                                }
                resp = requests.request('post', url='http://'+data['host']+'/sendGroupMessage', json=post)
                print(resp.text)
                 
        else:
            pass
        time.sleep(1)
        


else:
    print('bot连接失败,请检查data文件设置')








