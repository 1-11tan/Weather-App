from tkinter import *
import tkinter as tk
from geopy.geocoder import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500")
root.resizable(False,False)

Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,font=("poppins",25,"bold"),width=17)
textfield.place(x=50,y=40)
textfield.focus()



root.mainloop()


