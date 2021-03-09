import os
import tkinter as tk
from xml.dom import minidom
import yaml
import requests
import datetime
class Meteo():
    id_citta=""
    citta=""
    lat=""
    lon=""
    temperatura_corrente=""
    temperatura_massima=""
    temperatura_minima=""
    umidita=""
    ora_locale=""
    def _init_(self,id_citta,citta,lat,lon,temperatura_corrente,temperatura_massima,temperatura_minima,umimdita,ora_locale):
        self.id_citta=""
        self.citta=""
        self.lat=""
        self.lon=""
        self.temperatura_corrente=""
        self.temperatura_massima=""
        self.temperatura_minima=""
        self.umidita=""
        self.ora_locale=""
    def modules(self):
        try:
            import requests
            import yaml
        except:
            print(
            "Installando librerie...")
            os.system('pip install -r requirements.txt')
            import requests
            import yaml
    def yamlconfig(self):
        with open('Config.yaml', 'r') as ymlconfig:
            config = yaml.load(ymlconfig, Loader=yaml.FullLoader)
        return config["api"]
    def meteo_attuale(self,citta,lingua):
        api = self.yamlconfig()
        url = api % (citta,lingua)
        try:
            xmldata = requests.get(url)
        except: print("Città non esistente si prega di riprovare.")
        xdp = minidom.parseString(xmldata.text)
        self.id_citta = xdp.getElementsByTagName("city")[0].getAttribute("id")
        self.citta = xdp.getElementsByTagName("city")[0].getAttribute("name")
        self.lat = xdp.getElementsByTagName("coord")[0].getAttribute("lat")
        self.lon = xdp.getElementsByTagName("coord")[0].getAttribute("lon")
        self.temperatura_corrente = xdp.getElementsByTagName("temperature")[0].getAttribute("value")
        self.temperatura_massima = xdp.getElementsByTagName("temperature")[0].getAttribute("max")
        self.temperatura_minima = xdp.getElementsByTagName("temperature")[0].getAttribute("min")
        self.umidita = xdp.getElementsByTagName("humidity")[0].getAttribute("value") + xdp.getElementsByTagName("humidity")[
        0].getAttribute("unit")
        timezone = xdp.getElementsByTagName("timezone")[0].firstChild.nodeValue
        self.ora_locale = str(datetime.datetime.utcnow() + datetime.timedelta(seconds=int(timezone)))
        self.icon = xdp.getElementsByTagName("weather")[0].getAttribute("icon")
        self.weather = xdp.getElementsByTagName("weather")[0].getAttribute("value")