import requests
from bs4 import BeautifulSoup
import zhconv


url= "https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


req = requests.get(url,headers=headers,timeout=2)
doc = BeautifulSoup(req.text,"html.parser")
for i in range(2,10):
    body=doc.find_all("tbody")[i]
    trs=body.find_all("tr")
    p=0
    prenum=0
    for tr in trs:
        if p>1:
            # print(f"{p}--------------------------")
            tds=tr.find_all("td")
            number=int((tds[0].text)[1:])
            if(prenum==number):
                continue
            prenum=number
            name=tds[2].text
            name=zhconv.convert(name,"zh-tw")
            if name[-2]=='*':
                print(f"\"{name[:-2]}\",")
            else:
                print(f"\"{name[:-1]}\",")
        p+=1