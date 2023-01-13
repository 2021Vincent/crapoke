import requests
from bs4 import BeautifulSoup
# import urllib
# import listcopy
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
def query():
    search_string = input()
    url = "https://wiki.52poke.com/wiki/" +  search_string 
    return url
def get_parser_output(url):
    try:
        result = requests.get(url,headers=headers,timeout=5)
        if result.status_code==200:
            doc = BeautifulSoup(result.text,"html.parser")
            body=doc.find("body")
            if body:
                parser = body.find("div",class_="mw-parser-output")
                if parser:
                    return parser
                else:
                    print("parser-output not found")
                    return ""
            else:
                print("body not found")
                return ""
    except requests.ConnectionError as conn_ex:
        print("連線錯誤")
        print(str(conn_ex))
    except requests.Timeout as timeout_ex:
        print("請求超時錯誤")
        print(str(timeout_ex))
    except requests.RequestException as request_ex:
        print("請求發生錯誤")
        print(str(request_ex))
    except Exception as e:
        print("發生其它錯誤")
        print(str(e))

def find_stat(parser_output):

    tables=parser_output.find_all("table",style="white-space:nowrap")
    if tables:
        for table in tables:
            print(table.parent.get("title","一般"))
            trs=table.find_all("tr")
            if trs:
                for i in range(2,9):
                    print(trs[i].find("th").text[:-1])
            else:
                print("trs not found")
                exit()
    else:
        print("tables not found")
        exit()
def find_base_point(parser_output):
    try:
        a_tag=parser_output.find("a",href="/wiki/%E5%9F%BA%E7%A1%80%E7%82%B9%E6%95%B0")
        if a_tag:
            tr=a_tag.parent.parent.find("tr")
            if tr:
                print(tr.text)
            else:
                print("tr not found")
                exit()
            # print(a_tag.text)
        else:
            print("a_tag not found")
            exit()
    except AttributeError as ae:
        print("使用不存在的屬性")
        print(str(ae))
    except IndexError as ie:
        print("索引值超過了序列的大小")
        print(str(ie))

if __name__=="__main__":
    # for name in listcopy.allname:
    #     print(name)
    url=query()
    parser_output=get_parser_output(url)
    if parser_output!=None:
        find_stat(parser_output)
        find_base_point(parser_output)
    else:
        print("parser_output is None")