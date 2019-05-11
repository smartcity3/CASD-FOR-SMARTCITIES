#Imports
import time
import datetime
import random
import requests
import pyautogui
from PIL import ImageTk, Image
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

#Variables
width, height = pyautogui.size()

master = Tk()
master.title('Control Panel')
master.geometry('{}x{}'.format(width, height))


city = simpledialog.askstring('City', 'City Name: ')

weather_api = api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='


try:
    url = weather_api + city
    json_data = requests.get(url).json()
    weather = json_data['weather'] [0]['description']
except Exception:
    messagebox.showerror('Wrong Input', 'Wrong City Name')
    url = weather_api + city
    json_data = requests.get(url).json()
    weather = json_data['weather'] [0]['description']

max_dist = 90

def randomCm(state = 0):
    if state == 0:
        randomNum = random.randint(30, 76) + 1
        return randomNum
    else:
        randomNum = random.randint(0, 45) + 1
    return randomNum

#Random API Sensor Generator
if weather == 'clear sky' or weather == 'broken clouds' or weather == 'sunny' or weather == 'few clouds':


    api = [
        ['sensor1', randomCm(1)],
        ['sensor2', randomCm(1)],
        ['sensor3', randomCm(1)],
        ['sensor4', randomCm(1)],
        ['sensor5', randomCm(1)],
        ['sensor6', randomCm(1)],
        ['sensor7', randomCm(1)],
        ['sensor8', randomCm(1)]
    ]

else:
    api = [
        ['sensor1', randomCm()],
        ['sensor2', randomCm()],
        ['sensor3', randomCm()],
        ['sensor4', randomCm()],
        ['sensor5', randomCm()],
        ['sensor6', randomCm()],
        ['sensor7', randomCm()],
        ['sensor8', randomCm()]
    ]

lbl_width = 20
margin_height = 0
path = 'C:\\Users\\STAYROS AGELIDAKIS\\Pictures\\london_map.png'

online_list = []
warning_list = []
error_list = []
risk_list = []

#StringVars
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()

var1.set('online')
var2.set('online')
var3.set('online')
var4.set('online')
var5.set('online')
var6.set('online')
var7.set('online')
var8.set('online')

#Slot Development
slot1 = Label(master, text=api[0][0], width=lbl_width, height=4).pack()
status1 = Label(textvariable=var1, fg='green', anchor='e').pack()
margin = Label(text='', height=margin_height).pack()

slot2 = Label(master, text=api[1][0], width=lbl_width, height=4).pack()
status2 = Label(textvariable=var2, fg='green', anchor='e').pack()
margin = Label(text='', height=margin_height).pack()

slot3 = Label(master, text=api[2][0], width=lbl_width, height=4).pack()
status3 = Label(textvariable=var3, fg='green', anchor='e').pack()
margin = Label(text='', height=margin_height).pack()

slot4 = Label(master, text=api[3][0], width=lbl_width, height=4).pack()
status4 = Label(textvariable=var4, fg='green', anchor='e').pack()
margin = Label(text='', height=margin_height).pack()

slot5 = Label(master, text=api[4][0], width=lbl_width, height=4).pack()
status5 = Label(textvariable=var5, fg='green', anchor='e').pack()
margin = Label(text='', height=margin_height).pack()

slot6 = Label(master, text=api[5][0], width=lbl_width, height=4).pack()
status6 = Label(textvariable=var6, fg='green', anchor='e').pack()
margin = Label(text='', height=margin_height).pack()

slot7 = Label(master, text=api[6][0], width=lbl_width, height=4).pack()
status7 = Label(textvariable=var7, fg='green', anchor='e').pack()
margin = Label(text='', height=margin_height).pack()

slot8 = Label(master, text=api[7][0], width=lbl_width, height=4).pack()
status8 = Label(textvariable=var8, fg='green', anchor='e').pack()
margin = Label(text='', height=margin_height).pack()

def statusChanger(status_list):

    if status_list == online_list:
        text = 'online'
    elif status_list == warning_list:
        text = 'Warning'
    elif status_list == error_list:
        text = 'Fatal Error'
    
    if 'sensor1' in status_list:
        var1.set(text)
    elif 'sensor2' in status_list:
        var2.set(text)
    elif 'sensor3' in status_list:
        var3.set(text)
    elif 'sensor4' in status_list:
        var4.set(text)
    elif 'sensor5' in status_list:
        var5.set(text)
    elif 'sensor6' in status_list:
        var6.set(text)
    elif 'sensor7' in status_list:
        var7.set(text)   
    elif 'sensor8' in status_list:
        var8.set(text)   
        

        

while True: 
    for sensor in api:
        sensor_id = sensor[0]
        cm = sensor[1]
    
        if float(sensor[1]) >= 60 * max_dist / 100:
            if float(cm > 80 * max_dist / 100):
                error_list.append(sensor_id)
                for idx in range(0,len(warning_list)-1):
                    if warning_list[idx-1] == sensor_id:
                        warning_list.pop(idx)
                for idx in range(0,len(online_list)-1):
                    if online_list[idx-1] == sensor_id:
                        online_list.pop(idx)


            else:
                warning_list.append(sensor_id)
                for idx in range(0,len(error_list)-1):
                    if warning_list[idx-1] == sensor_id:
                        warning_list.pop(idx)
                for idx in range(0,len(online_list)-1):
                    if online_list[idx-1] == sensor_id:
                        online_list.pop(idx)

       

        if cm < 45 * max_dist / 100:
            online_list.append(sensor_id)
            for idx in range(0,len(warning_list)-1):
                if warning_list[idx-1] == sensor_id:
                    warning_list.pop(idx)
            for idx in range(0,len(error_list)-1):
                if online_list[idx-1] == sensor_id:
                    online_list.pop(idx)


        statusChanger(online_list)
        statusChanger(warning_list)
        statusChanger(error_list)

        print(error_list)
        print(warning_list)
        print(online_list)

        
    '''___________________________weather check________________________________'''


    if weather == 'sunny' or weather == 'broken clouds' or weather == 'clear sky' or weather == 'overcast clouds':
        if cm <= 30:
            time.sleep(8)
        else:
            risk_list.append(sensor_id)
            time.sleep(4)
    
    elif weather == 'few clouds':
        time.sleep(4)

    elif weather == 'light rain' or weather == 'moderate rain' or weather == 'mist' or weather == 'haze':
        time.sleep(3)

    elif weather == 'rainy':
        time.sleep(1)

    if weather == 'clear sky' or weather == 'broken clouds' or weather == 'sunny' or weather == 'few clouds':

    
        api = [
            ['sensor1', randomCm(1)],
            ['sensor2', randomCm(1)],
            ['sensor3', randomCm(1)],
            ['sensor4', randomCm(1)],
            ['sensor5', randomCm(1)],
            ['sensor6', randomCm(1)],
            ['sensor7', randomCm(1)],
            ['sensor8', randomCm(1)]
        ]

    else:
        api = [
            ['sensor1', randomCm()],
            ['sensor2', randomCm()],
            ['sensor3', randomCm()],
            ['sensor4', randomCm()],
            ['sensor5', randomCm()],
            ['sensor6', randomCm()],
            ['sensor7', randomCm()],
            ['sensor8', randomCm()]
        ]
    master.mainloop()