import tkinter as tk
from tkinter import font
from turtle import width
from PIL import Image,ImageTk
import requests
#ecdb150e304df0d7ba0e419b9ca4020c
#api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}


root=tk.Tk()

root.title("Whether App")
root.geometry("600x500")


def formate_response(weather):
    try:
       city=weather['name']
       Condition=weather['weather'][0]['description']
       Temp=weather['main']['temp']
       final_str='City:%s\nCondition:%s\nTemp:%s'%(city,Condition,Temp)
    except:
        final_str='There was a problem retrieving that information'
    return final_str



def get_weather(city):
    weather_key='ecdb150e304df0d7ba0e419b9ca4020c'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    #print(response.json)
    weather=response.json()
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

    result['text']=formate_response(response.json())
    icon_name=weather['weather'[0]['icon']]
    open_image(icon_name)

def open_image(icon_name):
    size=int()


img=Image.open('C:\\Users\\JK\\Pictures\\bg.jpg')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text='Earth including over 200,000 cities!',fg='red',bg='sky blue',font=('times new roman',18,'bold'))
heading_title.place(x=80,y=18)

frame_one=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text='get wether',fg='black',font=('times new roman',16,'bold'),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

frame_two=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)


root.mainloop()