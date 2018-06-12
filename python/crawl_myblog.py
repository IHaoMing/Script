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
        t = links.span
        u = 'http://ihaoming.top'+links['href']
        d = {'title': t.string, 'url': u}
        url.append(d)
     
        
    for i in range(2, 6):
        archives = "http://ihaoming.top/archives/page/" + str(i) + "/"
        r = requests.get(archives)
        s = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
        for links in s.find_all(class_="post-title-link"):
            t = links.span
            u = 'http://ihaoming.top'+links['href']
            d = {'title': t.string, 'url': u}
            url.append(d)
    
    return url

#获取所有文章html
def getHtml(blog_url):
    blog = []
    for info in blog_url:
        r = requests.get(info['url'])
        s = BeautifulSoup(r.text, 'html.parser')
        b = s.find(class_="post-body")
        lines = b.find_all(class_="gutter")
        [line.extract() for line in lines] 
        h = ht.HTML2Text()
        md = h.handle(str(b))
        with open(info['title'] + ".md", "wb+") as f:
            f.write(md.encode('utf-8'))
        #open(str(i) + ".md","wb+").write(md.encode('utf-8')) 
        f.close()
        blog.append(b)
    return blog

#转为markdown保存
def saveAsMD(blog):
    pass

def main():
    #u = {'title':'标题', 'url':'http://ihaoming.top/archives/643a1911.html'}
    
    #url =[]
    #url.append(u)
    #getHtml(url)
    r = getUrl()
    for info in r:
        print(info['title'])
        print(info['url'])

if __name__ == '__main__':
    main()
