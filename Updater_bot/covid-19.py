import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json() # convert into jason format
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates", text, duration=20)
        time.sleep(60) # units are seconds

update()