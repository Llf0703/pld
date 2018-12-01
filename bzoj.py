import urllib.request
import re
import time


def get_html(url):
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    page = opener.open(url)
    html = page.read()
    html = html.decode('utf-8')
    return html


reglist = []

tmp = 1

user=input("请输入用户名：")

url = 'https://www.lydsy.com/JudgeOnline/status.php?user_id='+user

html,last_html="",""

while tmp==1:
    last_html=html
    html = get_html(url)
    reg = r'problem.php\?id=([0-9]{1,4})'
    c_reg = re.compile(reg)
    reglist += c_reg.findall(html)
    nxt = r'Previous Page</a>\]&nbsp;&nbsp;\[<a href=(.+?)>Next'
    c_nxt = re.compile(nxt)
    nxt_url = c_nxt.findall(html)
    for i in nxt_url:
        url="https://www.lydsy.com/JudgeOnline/"+i
    if (html==last_html):
        break
    time.sleep(0.5)

rslist = []

for i in range(len(reglist)):
    a=reglist.pop()
    if a not in rslist:
        rslist.append(a)

file = open(user+'.txt','w')

for result in rslist:
    file.write(result+'\n')

file.close()