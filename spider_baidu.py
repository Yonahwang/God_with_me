import urllib.request
from urllib.parse import quote
import re
import requests

def down_file(url,filk_path):
    try:
        res = requests.get(url, stream=True)
    except:
        return
    f = open(filk_path,'wb')
    for chunk in res.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()
    f.close()

def baidu_search(keyword):
    html=urllib.request.urlopen("http://www.baidu.com/s?wd="+quote(keyword)).read()
    return html

def getList(regex,text):
    arr = []
    res = re.findall(regex, text)
    if res:
        for r in res:
            arr.append(r)
    return arr

def getMatch(regex,text):
    res = re.findall(regex, text)
    if res:
        return res[0]
    return ""


html = baidu_search('filetype:pdf')
content = html.decode('utf-8')
#print(content)
arrList = getList(r"<div class=\"result c-container \" id=.*?>[\s\S]*?\"url\":\"", content)
for item in arrList:
    regex = r"href = \".*?\""
    link = getMatch(regex,item)
    url = link[8:-1]
    regex = "{\"title\":\".*?\",\""
    title = getMatch(regex,item)[10:-3]
    print(url)
    print(title)
down_file(url,'1.pdf')