import interface_auto

formdata = {
    "type": "AUTO",
    "i": "i love python",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_ENTER",
    "typoResult": "true"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

response = interface_auto.post(url, data=formdata, headers=headers)

print(response.text)

# 如果是json文件可以直接显示
print(response.json())
