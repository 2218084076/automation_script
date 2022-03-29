import requests
import json
import xlwt
# https://www.qianshanghua.com/home/page/edit/7bd201e476e94bc4a1c3d5529083d8f7
# 2月份商品爬取
excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)
table.write(0,0,"序号")
table.write(0,1,"品牌")
table.write(0,2,"商品名称")
table.write(0,3,"商品编码")
table.write(0,4,"商品价格")
table.write(0,5,"商品促销")
table.write(0,6,"规格")
table.write(0,7,"商品详情数据")


urls=[
    ["1","https://www.qianshanghua.com/api/page/comment/load?chat_id=3c76a693ae2b46e99830558edbfa817b&comment_id="],
    ["2","https://www.qianshanghua.com/api/page/comment/load?chat_id=3c76a693ae2b46e99830558edbfa817b&comment_id=950b1f346aa141069a510581c5a28755"]
]
base_i=1
for url in urls:

    a = requests.get(url[1])
    a = a.text
    b = json.loads(a)
    l=[]9

    for comment in b["comments"]:
        try:
            a_json = json.loads(comment[4])
        except:
            print("error:",url[0],comment[0])
            continue
        l.append(a_json)

    for i in range(0,len(l)):
        table.write(base_i+i,0,i)
        table.write(base_i+i,1,l[i]["detail-box-title"])

        table.write(base_i+i,2,l[i]["product-name"])
        table.write(base_i+i,3,l[i]["product-code-value"])
        table.write(base_i+i,4,l[i]["price-now"])
        table.write(base_i+i,5,l[i]["promotion-item"])
        table.write(base_i+i,6,str(l[i]["property-item"].get("规格","")))
        table.write(base_i+i,7,str(l[i]["property-item"]))
        excel.save("20220228.xls")
        print(i,l[i]["detail-box-title"])
    base_i=base_i+len(l)


