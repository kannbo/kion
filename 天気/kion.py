import requests
import datetime
import sys


def kion(x):
    # 現在の時刻を取得
    now_raw = datetime.datetime.now()
    now = now_raw.strftime('%Y%m%d%H')


    url = "https://www.jma.go.jp/bosai/amedas/data/map/" + now + "0000.json"
    header = {"content-type": "application/json"}
    try:
        response = requests.get(url, headers=header)
        data = response.json()
        return {"気温":data[str(x)]["temp"][0],"降水量(前1時間)":data[str(x)]["precipitation1h"][0],"風速":data[str(x)]["wind"]}
    except:
        return {"気温":"error","湿度":"error","風速":"error"}
      

if __name__ == '__main__':
   print(kion("45061"))

