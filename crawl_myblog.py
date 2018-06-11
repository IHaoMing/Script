#爬取自己的博客

import requests
from bs4 import BeautifulSoup
import html2text as ht

#获取所有文章的链接
def getUrl():
    url = []
    #归档页面
    archives = "http://ihaoming.top/archives/"
    r1 =  requests.get(archives)
    s1 = BeautifulSoup(r1.text, 'html.parser', from_encoding='utf-8')
    for links in s1.find_all(class_="post-title-link"):
        url.append('http://ihaoming.top'+links['href'])

    for i in range(2, 6):
        archives = "http://ihaoming.top/archives/page/" + str(i) + "/"
        r = requests.get(archives)
        s = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
        for links in s.find_all(class_="post-title-link"):
            url.append('http://ihaoming.top'+links['href'])
    
    return url

#获取所有文章html
def getHtml(blog_url):
    blog = []
    for url in blog_url:
        r = requests.get(url)
        s = BeautifulSoup(r.text, 'html.parser')
        b = s.find(class_="post-body")
        lines = b.find_all(class_="gutter")
        [line.extract() for line in lines] 
        b_str = b.content.decode('utf-8')
        h = ht.HTML2Text()
        md = h.handle(b_str)
        open("1.md","w").write(md) 
        blog.append(b)
    return blog

#转为markdown保存
def saveAsMD(blog):
    pass

def main():
    u = "http://ihaoming.top/archives/1ca6b62d.html"
    url =[]
    url.append(u)
    getHtml(url)

if __name__ == '__main__':
    main()
