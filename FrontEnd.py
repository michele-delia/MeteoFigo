import BackEnd
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk,ImageDraw
id_citta=""
citta=""
lat=""
lon=""
temperatura_corrente=""
temperatura_massima=""
temperatura_minima=""
umidita=""
ora_locale=""
weather=""
lingua=""

def Reset():
    finestra.labid.config(text="")
    finestra.labnome.config(text="")
    finestra.lablat.config(text="")
    finestra.lablon.config(text="")
    finestra.labtemp.config(text="")
    finestra.labtempmax.config(text="")
    finestra.labtempmin.config(text="")
    finestra.labumidity.config(text="")
    finestra.labtime.config(text="")

def Meteo():
    citta=finestra.insc.get()
    lingua=finestra.insl.get()
    try:
        meteo.meteo_attuale(citta,lingua)
    except IndexError :
        messaggio=citta+" non corrisponde alla ricerca"
        msgbox.showerror("Errore",messaggio)
        return
    id_citta=meteo.id_citta
    finestra.labid.config(text=id_citta)
    citta=meteo.citta
    finestra.labnome.config(text=citta)
    lat=meteo.lat
    finestra.lablat.config(text=lat)
    lon=meteo.lon
    finestra.lablon.config(text=lon)
    temperatura_corrente=meteo.temperatura_corrente
    finestra.labtemp.config(text=temperatura_corrente+"°")
    temperatura_massima=meteo.temperatura_massima
    finestra.labtempmax.config(text=temperatura_massima+"°")
    temperatura_minima=meteo.temperatura_minima
    finestra.labtempmin.config(text=temperatura_minima+"°")
    umidita=meteo.umidita
    finestra.labumidity.config(text=umidita)
    ora_locale=meteo.ora_locale
    finestra.labtime.config(text=ora_locale)
    weather=meteo.weather
    finestra.labmeteo.config(text=weather)
    img = Image.open('Icons/{}@2x.png'.format(meteo.icon))
    finestra.image = ImageTk.PhotoImage(img)
    Label(finestra, image=finestra.image, bg="black").place(relx=0.8, rely=0.83, relwidth=0.10, relheight=0.10)

def configura_finestra():
    finestra.title("Meteo")
    finestra.geometry("1000x800")
    finestra.resizable(True, True)
    finestra.configure(background="gray")
    finestra.grid()

def inserisci_widget():
    ttk.Separator(finestra).place(x=0, y=65, relwidth=1)
    finestra.labc = tk.Label(text="Ricerca città")
    finestra.image = tk.Label()
    finestra.labc.config(font=("Cambria", 16))
    finestra.labc.config(fg="white")
    finestra.labc.config(bg="black")
    finestra.labc.place(x=430, y=0)
    finestra.labl = tk.Label(text="Inserire Lingua")
    finestra.labl.config(font=("Cambria", 16))
    finestra.labl.config(fg="white")
    finestra.labl.config(bg="black")
    finestra.labl.place(x=570, y=0)
    finestra.insl = tk.Entry(bg="salmon")
    finestra.insl.place(x=560, y=20)
    finestra.insc = tk.Entry(bg="salmon")
    finestra.insc.place(x=420, y=20)
    finestra.bottonec = tk.Button(text="Cerca", command=Meteo)
    finestra.bottonec.config(bg="forestgreen")
    finestra.bottonec.place(x=420, y=40)
    finestra.bottoner = tk.Button(text="Azzera", command=Reset)
    finestra.bottoner.config(bg="forestgreen")
    finestra.bottoner.place(x=505, y=40)

    finestra.labid1 = tk.Label(text="ID Citta' :")
    finestra.labid1.config(font=("Cambria", 16))
    finestra.labid1.config(fg="white")
    finestra.labid1.config(bg="black")
    finestra.labid1.place(x=200, y=200)
    finestra.labid = tk.Label()
    finestra.labid.config(font=("Helvetica", 11))
    finestra.labid.config(fg="white")
    finestra.labid.config(bg="black")
    finestra.labid.place(x=200, y=200)

    finestra.labnome1 = tk.Label(text="Nome Citta' :")
    finestra.labnome1.config(font=("Cambria", 16))
    finestra.labnome1.config(fg="white")
    finestra.labnome1.config(bg="black")
    finestra.labnome1.place(x=200, y=200)
    finestra.labnome = tk.Label()
    finestra.labnome.config(font=("Helvetica", 11))
    finestra.labnome.config(fg="white")
    finestra.labnome.config(bg="black")
    finestra.labnome.place(x=200, y=200)

    finestra.lablat1 = tk.Label(text="Latitudine :")
    finestra.lablat1.config(font=("Cambria", 16))
    finestra.lablat1.config(fg="white")
    finestra.lablat1.config(bg="black")
    finestra.lablat1.place(x=200, y=200)
    finestra.lablat = tk.Label()
    finestra.lablat.config(font=("Helvetica", 11))
    finestra.lablat.config(fg="white")
    finestra.lablat.config(bg="black")
    finestra.lablat.place(x=200, y=200)

    finestra.lablon1 = tk.Label(text="Longitudine :")
    finestra.lablon1.config(font=("Cambria", 16))
    finestra.lablon1.config(fg="white")
    finestra.lablon1.config(bg="black")
    finestra.lablon1.place(x=200, y=200)
    finestra.lablon = tk.Label()
    finestra.lablon.config(font=("Helvetica", 11))
    finestra.lablon.config(fg="white")
    finestra.lablon.config(bg="black")
    finestra.lablon.place(x=200, y=200)

    finestra.labtemp1 = tk.Label(text="Temperatura attuale :")
    finestra.labtemp1.config(font=("Cambria", 16))
    finestra.labtemp1.config(fg="white")
    finestra.labtemp1.config(bg="black")
    finestra.labtemp1.place(x=200, y=200)
    finestra.labtemp = tk.Label()
    finestra.labtemp.config(font=("Helvetica", 11))
    finestra.labtemp.config(fg="white")
    finestra.labtemp.config(bg="black")
    finestra.labtemp.place(x=200, y=200)

    finestra.labtempmax1 = tk.Label(text="Temperatura Massima :")
    finestra.labtempmax1.config(font=("Cambria", 16))
    finestra.labtempmax1.config(fg="white")
    finestra.labtempmax1.config(bg="black")
    finestra.labtempmax1.place(x=200, y=200)
    finestra.labtempmax = tk.Label()
    finestra.labtempmax.config(font=("Helvetica", 11))
    finestra.labtempmax.config(fg="white")
    finestra.labtempmax.config(bg="black")
    finestra.labtempmax.place(x=200, y=200)

    finestra.labtempmin1 = tk.Label(text="Temperatura Minima :")
    finestra.labtempmin1.config(font=("Cambria", 16))
    finestra.labtempmin1.config(fg="white")
    finestra.labtempmin1.config(bg="black")
    finestra.labtempmin1.place(x=200, y=200)
    finestra.labtempmin = tk.Label()
    finestra.labtempmin.config(font=("Helvetica", 11))
    finestra.labtempmin.config(fg="white")
    finestra.labtempmin.config(bg="black")
    finestra.labtempmin.place(x=200, y=200)

    finestra.labumidity1 = tk.Label(text="Umidita' :")
    finestra.labumidity1.config(font=("Cambria", 16))
    finestra.labumidity1.config(fg="white")
    finestra.labumidity1.config(bg="black")
    finestra.labumidity1.place(x=200, y=200)
    finestra.labumidity = tk.Label()
    finestra.labumidity.config(font=("Helvetica", 11))
    finestra.labumidity.config(fg="white")
    finestra.labumidity.config(bg="black")
    finestra.labumidity.place(x=200, y=200)

    finestra.labtime1 = tk.Label(text="Data e Ora attuali:")
    finestra.labtime1.config(font=("Cambria", 16))
    finestra.labtime1.config(fg="white")
    finestra.labtime1.config(bg="black")
    finestra.labtime1.place(x=200, y=200)
    finestra.labtime = tk.Label()
    finestra.labtime.config(font=("Helvetica", 11))
    finestra.labtime.config(fg="white")
    finestra.labtime.config(bg="black")
    finestra.labtime.place(x=200, y=200)

    finestra.meteo = tk.Label(text="Meteo :")
    finestra.meteo.config(font=("Cambria", 16))
    finestra.meteo.config(fg="white")
    finestra.meteo.config(bg="black")
    finestra.meteo.place(x=200, y=700)
    finestra.labmeteo = tk.Label()
    finestra.labmeteo.config(font=("Helvetica", 11))
    finestra.labmeteo.config(fg="white")
    finestra.labmeteo.config(bg="black")
    finestra.labmeteo.place(x=300, y=699)
finestra = tk.Tk()
configura_finestra()
inserisci_widget()
meteo=BackEnd.Meteo()
meteo.modules()
meteo.yamlconfig()
finestra.mainloop()

