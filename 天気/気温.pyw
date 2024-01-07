import kion
import PySimpleGUI as sg
import pyautogui,requests

pyautogui.confirm(text="このアプリは気象庁のAPIを使っています", title="起動するアプリの選択",
                        buttons=["了解"])
area=130000
forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area}.json"
forecast_req = requests.get(forecast_url)
forecast_data = forecast_req.json() # 天気概況
forecast_text = "\n".join(forecast_data["text"].split())
#print(forecast_text)
kikou=[[sg.T("ID",key="textdesu",enable_events=True),
        sg.B("検索",key="btn")],
       [sg.I("",key="textdesuyo")],
       [sg.T("今日の天気予報,東京")],
       [sg.T(forecast_text,size=(50,400))]]
window=sg.Window("気温確認",kikou, resizable=True,font=(["keifont","UD デジタル 教科書体 N-B"][1],10),size=(500, 600))

while True:
    event,hoge=window.read()
    if event==sg.WIN_CLOSED:
            window.close()
            break
    if event=="btn":
        apii=kion.kion(hoge["textdesuyo"])
        window["textdesu"].update(str(apii["気温"])+"度  降水量"+str(apii["降水量(前1時間)"])
                                  +"%"+"  風速"+str(apii["風速"][0]))
