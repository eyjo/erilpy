import requests
from lxml import etree
from tkinter import *

URL = "https://xmlweather.vedur.is"

def get_vedur():
    payload = {
        "op_w": "xml",
        "type": "obs",
        "lang": "is",
        "view": "xml",
        "ids": "1", #;422;2738;1473",
    }
    response = requests.get(
        url=URL, 
        params=payload)
    tree = etree.fromstring(response.content)
    weather = []
    for station in tree.findall('station'):
        weather.append({
            observation.tag: observation.text
            for observation in station
        })
    return weather

def takka_click():
    w = get_vedur()
    lbl.configure(text=w[0]['T'])

window = Tk()

window.title('Veðurstöðin')

lbl = Label(window, text="Veðurstöðin")
bnt = Button(window, text="Sækja veðurmælingu", bg="lightgreen", fg="black", command=takka_click)

lbl.grid(column=0, row=0)
bnt.grid(column=0, row=1)

window.mainloop()



