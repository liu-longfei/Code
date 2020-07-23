#! usr/bin/python   #第一行是注释行，称之为“组织行”，用来告诉系统应该用哪个系统应该使用哪个解释器来执行该程序
# Author:zdx
# Aim：一个图片爬虫


import requests
import re
import random
#  http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=（你想输入的名字）

def spiderPic(html,keyword):
    print("正在查找{}，对应的图片正在下载....".format(keyword))
    for address in re.findall('"objURL":"(.*?)"',html,re.S):




        with open("./picture/" + "{}.jpg" .format(random.randrange(0,1000,4)) , "wb") as f:
            pic = requests.get(address, timeout=10)
            f.write(pic.content)

        # with open("picture","w") as f:
        #     f.write(pic.content)
        # i = 0
        # dir = './images/' + keyword + '_' + str(i) + '.jpg'
        # fp = open(dir, 'wb')
        # fp.write(pic.content)
        # fp.close()






if __name__ == '__main__':
    word = input("请输入你心目中的男神:")

    #header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    result = requests.get("http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word={}".format(word))
    #print(result.text)
spiderPic(result.text, word)