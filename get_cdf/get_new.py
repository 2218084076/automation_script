import pyautogui
import time
import pyperclip

# 打开审查元素位置 921.6
# 2022/01/15
urls=["C050137","C050551","C050554","C052043","C053263","C053586","C054264","C054895","C055901","C055903","C000277","C000278","C000569","C010461","C010514","C010627","C015874","C015947",]
u2=["C018863","C019986","C026594","C026741","C027725","C033525","C034714","C034756","C037234","C039090","C039398/C054897","C040267","C040268","C040269","C040270","C040275","C040308","C041295","C043950","C043952","C043952","C043953","C043953","C043954","C043954","C043955","C043955","C044264","C044292","C044695","C044761","C045059","C045061","C045062","C045281","C045470","C046455","C046457","C046904","C046905","C049105","C049544","C049545","C049546","C049693","C049703","C049704","C049909","C051159","C051160","C051161","C051162","C051443","C051620","C051622","C051665","C051666","C051667","C052195","C053307","C053314","C053316","C053752","C054759","C054897","C055022","C055158","C055158","C055937","C055938","C055939","C055940","C055941","C055942","C055943","C055944","C055947","C056395","C100560","C100563","C008124","C008193","C008212","C008213","C008214","C008245","C010374","C010572","C021127","C024395","C051503","C052672","C052862","C052882","C053368","C053369","C053481","C053929","C054245","C054248","C054249","C054570","C101100","C052638","C052639","C052640","C052641","C052643","C052644","C052908","C052909","C052910","C052911","C052912","C052913","C052914","C052916","C053703","C053704","C053777","C054005","C054006","C054322","C054987","C055081","C055649","C055650","C017924","C021953","C021954","C021955","C022455","C024387","C025188","C025219","C026592","C028072","C028155","C028489","C029241","C029242","C029243","C029245","C029246","C033541","C037328","C041703","C041704","C046756","C046757","C046759","C046762","C046763","C046782","C046790","C046847","C046853","C046863","C046864","C046865","C046867","C048505","C048883","C051680","C051888","C052002","C052004","C052038","C053783","C053784","C053998","C053999","C054001","C054747","C054748","C054750","C054751","C054752","C054753","C054754","C054755","C054757","C054758","C055280","C055282","C055878","C055879","C055880","C055881","C055882","C055883","C055884","C055885","C055886","C055887","C055888","C055889","C055890","C055891","C055892","C055893","C055894","C055895","C055896","C055897","C055898","C055899","C056064","C056065","C057132","C057133","C057581","C057582","C101385","C101387","C101388","C101389","C101390","C101391","C048262","C048263","C048264","C048265","C048266","C048267","C048268","C048270","C048271","C049063","C049064","C049065","C049066","C053972","C054257","C054258","C056453","C056454","C057651","C027389","C027398","C029509","C039976","C041442","C043422","C046459","C046461","C047868","C049091","C050550","C051214","C053318","C054262","C054263","C055962","C003102","C024680","C024684","C024712","C024714","C024718","C026531","C026536","C026537","C028835","C028836","C029467","C030269","C030425","C035233","C035234","C036268","C036278","C037663","C037664","C037666","C037667","C037668","C040904","C041054","C042834","C042836","C042840","C042844","C043585","C043587","C043607","C043616","C044425","C046485","C046496","C047854","C047855","C047856","C047857","C047858","C047859","C048644","C048645","C048874","C048875","C048876","C048877","C048878","C048879","C048880","C049145","C049146","C049535","C050070","C050071","C050075","C050076","C050077","C050078","C050081","C050083","C050084","C050085","C050086","C050087","C050090","C050429","C051887","C052074","C052075","C052079","C052652","C052907","C053754","C053755","C053781","C053785","C053786","C054746","C055154","C055156","C055489","C055490","C055491","C055492","C055493","C100192","C101686","C101687","C101693","C101694"]

def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
    elif action["name"] in ["select_all_and_write"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        write_content = action.get("content","")
        pyautogui.typewrite(write_content)
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_js_latest"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press('backspace')
        pyautogui.press('up')
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_copy"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "x")
    elif action["name"] in ["select_all_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")
    elif action["name"] in ["select_item_and_close_tab"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "w")
    elif action["name"] in ["select_all_and_copy_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        write_content = action.get("content","")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
    elif action["name"] in ["open_console"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("f12")
    elif action["name"] in ["url_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        write_content = action.get("content","")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)

for u in urls:
    print(u)
    page={
        "x":943,
        "y":200,
        "sleep":5,
        "name":"url_paste",
        "content":u,
        "action_name":"访问链接",
    }
    pyautogui_action(page)
    action_item_click_list = [
        {
            "x": 365,
            "y": 954,
            "sleep": 2,
            "name": "move_to_click",
            "content": "",
            "action_name": "点击商品",
        },
        {
            "x": 454,
            "y": 20,
            "sleep": 0.5,
            "name": "open_console",
            "content": "",
            "action_name": "打开控制台",
        },
        {
            "x": 1230,
            "y": 178,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "清空console",
        },
        {
            "x": 1188,
            "y": 926,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content":
                r'''
result=[]
try{result.push(document.getElementsByClassName("detail-box-title")[0].innerText)}
catch{result.push(document.getElementsByClassName("product-info-title")[0].innerText)}
try{result.push(document.getElementsByClassName("product-name")[0].innerText)}
catch{result.push(document.getElementsByClassName("product-info-title")[0].innerText)}
try{result.push(document.getElementsByClassName("product-code-value")[0].innerText)}
catch{result.push(document.getElementsByClassName("product-info-code")[0].innerText)}
try{result.push(document.getElementsByClassName("price-now")[0].innerText)}
catch{result.push(document.getElementsByClassName("cm-price-type-sales")[0].innerText)}
cxs=document.getElementsByClassName("product-rules")
if(cxs.length==0){
    cxs=document.getElementsByClassName("promotion-item")
}
cxs_info = []
for (i=0;i<cxs.length;i++){
    cxs_info.push(cxs[i].innerText)
}
ths=document.getElementsByClassName("property-item-title")
tds=document.getElementsByClassName("property-item-value")
kv={}
for (i=0;i<ths.length;i++){
    kv[ths[i].innerText]=tds[i].innerText
}

result_info = {
    "detail-box-title":result[0],
    "product-name":result[1],
    "product-code-value":result[2],
    "price-now":result[3],
    "promotion-item":cxs_info,
    "property-item":kv,
}
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"
document.body.append(dom)

                ''',
            "action_name": "get店铺信息",
        },
        {
            "x": 1037,
            "y": 108,
            "sleep": 0.5,
            "name": "select_all_and_copy",
            "content": "",
            "action_name": "copy"
        },
        {
            "x": 454,
            "y": 20,
            "sleep": 0.5,
            "name": "select_item_and_close_tab",
            "content": "",
            "action_name": "关闭选项卡",
        },
        {
            "x": 431,
            "y": 20,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "点击选项卡_pages",
        },
        {
            "x": 474,
            "y": 158,
            "sleep": 0.5,
            "name": "select_all_and_paste",
            "content": "",
            "action_name": "提交",
        },
        {
            "x": 403,
            "y": 256,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "submit",
        },
        {
            "x": 137,
            "y": 24,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "切换pgy页面",
        },

    ]

    for action_item_click in action_item_click_list:

        pyautogui_action(action_item_click)



'''

result=[]
result.push(document.getElementsByClassName("shop-name")[0].innerText.split("\n")[0])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1])
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText)
result.push(document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText)
result.push(document.getElementsByClassName("tel")[0].innerText)
result.push(document.getElementsByClassName("address")[0].innerText)

result_info = {
    "shop-name":result[0],
    "star":result[1]*0.1,
    "comment":result[2],
    "consume":result[3],
    "tel":result[4],
    "address":result[5]
}

dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"

document.body.append(dom)


shop-name = document.getElementsByClassName("shop-name")[0].innerText.split("\n")[0]
star = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[0].getAttribute("class").split("mid-str")[1]
comment = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[1].innerText
consume = document.getElementsByClassName("brief-info")[0].getElementsByTagName("span")[2].innerText
tel = document.getElementsByClassName("tel")[0].innerText
address = document.getElementsByClassName("address")[0].innerText


'''
