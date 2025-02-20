#请求工具库
from lxml import etree
import html
import Function

datas=Function.Get_Json("WebLine.json")
#获取当前页面url以免无法判断一直卡循环
page_url=datas["url"].split("/")[-1]

while page_url != "96104776630142037":
# for i in range(0,10):
    # 筛选获取响应文件中的某段需要内容
    info = Function.Get_Html_Element()
    info_content = info.xpath('//div[@class="ywskythunderfont"]/p')[:-1]
    #获取元素对象的某个想要标签 xpath内容可在浏览器xpath插件辅助获取
    #这里的最后一个元素不是我想要的元素所以给裁掉了
    next_url=info.xpath("//*[@id='j_chapterNext']/@href")[0]
    next_page="https://www.xs8.cn" +  next_url#获取a标签的href内容并拼在服务器地址上
    code_content_simple="" #储存每一个p标签元素的内容然后拼接
    #info=e.xpath('//div[@class="ywskythunderfont"]/p/text()')[:-2] #这里加/text（）将会直接将结果返回为可视汉字，不用多次转码
    for i in info_content:
        get_HTML=etree.tostring(i,pretty_print=True).decode()
        #将 Element 对象转换为字符串 pretty_print参数将格式化输出数据 decode（）将会使用‘utf-8’解码，转换成了可见的字符串
        decode_HTML=html.unescape(get_HTML)
        #HTML 实体编码未被解码所以要解码，相当于二次解码，将字符串中的一些实体编码（eg &xxxx）转换成汉字等
        code_content_simple+=decode_HTML
    code_content=code_content_simple.replace("<p>","")
    code_content=code_content.replace("</p>","").rstrip()
    # print(code_content)

    #用同样的方法获取标题
    info_title=info.xpath("//div/h1")#/text() 可直接加该函数免去下面两步,且不会多出<p>等标签
    get_title_Html=etree.tostring(info_title[0],pretty_print=True).decode()
    decode_title=html.unescape(get_title_Html)
    code_title=decode_title.replace('<h1 class="j_chapterName">','')
    code_title=code_title.replace("</h1>",'').strip()
    # print(code_title)
    Function.Modify_Json_url(next_page)
    #为了不覆盖之前扒的数据
    try :
        with open("庆余年.txt","r+",encoding="utf-8") as f:
            page_content=f.read()
            all_content=code_title + "\n\n" + code_content + "\n\n"
            print(all_content+'\n\n')
            f.write(all_content)
    except FileNotFoundError:
        print("庆余年.txt 不存在")


