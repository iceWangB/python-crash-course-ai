import requests
from lxml import etree
import json
def Get_Html_Element():
    datas=Get_Json("WebLine.json")
    ''' 关键点说明：
     headers中
     User - Agent: 模拟浏览器标识，避免被服务器识别为爬虫。
     Accept: 指定客户端可以处理的内容类型。
     Accept - Language: 指定客户端接受的语言。
     Referer: 表示请求的来源页面，通常用于反爬虫机制。
     注意事项：
     如果目标网站有反爬虫机制，可能需要动态调整头文件，例如添加Cookie或Authorization字段。
     对于复杂的动态网页（如使用JavaScript渲染的页面），可能需要使用Selenium或Playwright等工具来模拟浏览器行为。'''
    # 发送请求：
    get_it=requests.get(datas["url"],headers=datas["headers"])
    # 客户端获取的编译码
    get_it.encoding="utf-8"
    # 返回了响应文件的Element对象
    e=etree.HTML(get_it.text)
    return e

def Modify_Json_url(url):
    datas = Get_Json("WebLine.json")
    datas["url"]=url
    with open("WebLine.json","w",encoding="utf-8") as f:
        json.dump(datas,f)
    return datas

def Get_Json(json_name):
    try:
        with open(json_name,"r",encoding="utf-8") as f:
            datas=json.load(f)
    except FileNotFoundError:
        print("文件路径输入有误")
    except json.decoder.JSONDecodeError:
        print("JSON文件解析错误，请检查文件格式类型")
    else :
        return datas