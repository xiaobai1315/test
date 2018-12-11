#coding: UTF-8

import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'http://baijiahao.baidu.com/s?id=1605236544182897900&wfr=spider&for=pc'

    r = requests.get(url)
    bf = BeautifulSoup(r.text, features="html.parser")
    print(r.text)

    articleContent = bf.find_all('div', class_='article-content')
    # print(articleContent[0].text)
    #文本内容
    atricleContent = articleContent[0].text

    images = bf.find_all('div', class_='img-container')
    # print(images)
    #处理图片URL
    for image in images:
        strImage = str(image)
        tempImage = strImage.replace('<div class="img-container"><img class="large" data-loaded="0" data-loadfunc="0" src="', '')
        newStrImage = tempImage.replace('"/></div>', '')

        print(newStrImage)


