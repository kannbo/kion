import urllib.request as req

code="120000"
#URLを変数urlに保存
url="https://www.jma.go.jp/bosai/forecast/data/forecast/"+code+".json"

#保存ファイル名を指定する
filename='tenki.json'

#ダウンロード
req.urlretrieve(url,filename)
import json
b = json.load(open("tenki.json",'r',encoding="utf-8"))

data=b[1]["timeSeries"][0]["areas"]
idlist=""
#print(b)
for idlist in data:
    print(idlist)
