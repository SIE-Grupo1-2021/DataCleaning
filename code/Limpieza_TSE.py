# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:00:34 2022

@author: augusto.solar
"""

#Importamos paquetes necesarios

import numpy as np
import pandas as pd

#Importamos bases 

elec_2006 = pd.read_excel (r"C:\Users\augusto.solar\Desktop\TSE_2006.xlsx")
elec_2010 = pd.read_excel (r"C:\Users\augusto.solar\Desktop\TSE_2010.xlsx")
elec_2016 = pd.read_excel (r"C:\Users\augusto.solar\Desktop\TSE_2016.xlsx")

#Agrupamos cada base por codigo de distrito para tener los votos totales por 
#canton

elec_2006=elec_2006.groupby(['Provincia','Canton','Partido', 'Año'])['Votos'].sum().reset_index()
elec_2010=elec_2010.groupby(['Provincia','Canton','Partido', 'Año'])['Votos'].sum().reset_index()
elec_2016=elec_2016.groupby(['Provincia','Canton','Partido', 'Año'])['Votos'].sum().reset_index()

#Agregamos una columna del peso relativo por cada opcion de voto

elec_2006["Total_Canton"] = elec_2006['Votos'].groupby(elec_2006['Canton']).transform('sum')
elec_2006["Peso"]=elec_2006['Votos']/elec_2006["Total_Canton"]*100
elec_2006.pop("Total_Canton")

elec_2010["Total_Canton"] = elec_2010['Votos'].groupby(elec_2010['Canton']).transform('sum')
elec_2010["Peso"]=elec_2010['Votos']/elec_2010["Total_Canton"]*100
elec_2010.pop("Total_Canton")

elec_2016["Total_Canton"] = elec_2016['Votos'].groupby(elec_2016['Canton']).transform('sum')
elec_2016["Peso"]=elec_2016['Votos']/elec_2016["Total_Canton"]*100
elec_2016.pop("Total_Canton")

#-------Panel con variable de abstencionismo-------

#Extraemos la variable de abstencionismo unicamente

elec_2006_abs = elec_2006[elec_2006.Partido == "Abstencionismo"]
elec_2006_abs = elec_2006_abs.drop('Votos',axis = 1)
elec_2006_abs = elec_2006_abs.drop('Partido',axis = 1)
elec_2006_abs = elec_2006_abs.rename(columns={"Peso":"Abstencionismo"})

elec_2010_abs = elec_2010[elec_2010.Partido == "Abstencionismo"]
elec_2010_abs = elec_2010_abs.drop('Votos',axis = 1)
elec_2010_abs = elec_2010_abs.drop('Partido',axis = 1)
elec_2010_abs = elec_2010_abs.rename(columns={"Peso":"Abstencionismo"})

elec_2016_abs = elec_2016[elec_2016.Partido == "Abstencionismo"]
elec_2016_abs = elec_2016_abs.drop('Votos',axis = 1)
elec_2016_abs = elec_2016_abs.drop('Partido',axis = 1)
elec_2016_abs = elec_2016_abs.rename(columns={"Peso":"Abstencionismo"})

#Se unen las bases

frames_abs = [elec_2010_abs, elec_2016_abs, elec_2006_abs]

panel_abs = pd.concat(frames_abs)

#Borramos dfs intermedios

del elec_2010_abs, elec_2016_abs, elec_2006_abs, frames_abs

#-------Panel con variable de margen de ganancia-------

#Se elimina la opcion de abstencionismo, blanco y nulo, para ver el ranking. 

abn = ["Abstencionismo", "Votos en blanco", "Votos nulos"]
elec_2006_mar = elec_2006[elec_2006.Partido.isin(abn) == False]
elec_2010_mar = elec_2010[elec_2010.Partido.isin(abn) == False]
elec_2016_mar = elec_2016[elec_2016.Partido.isin(abn) == False]

#Asignamos un puesto a cada partido en cada canton por el peso de votos relativo

elec_2006_mar["Puesto"] = elec_2006_mar.groupby("Canton")["Peso"].rank("dense", ascending=False)
elec_2010_mar["Puesto"] = elec_2010_mar.groupby("Canton")["Peso"].rank("dense", ascending=False)
elec_2016_mar["Puesto"] = elec_2016_mar.groupby("Canton")["Peso"].rank("dense", ascending=False)

#Eliminamos todos aquellos puestos que no sean el 1 o el 2. 

elec_2006_mar1 = elec_2006_mar.drop(elec_2006_mar.index[elec_2006_mar['Puesto'] > 2])
elec_2010_mar1 = elec_2010_mar.drop(elec_2010_mar.index[elec_2010_mar['Puesto'] > 2])
elec_2016_mar1 = elec_2016_mar.drop(elec_2016_mar.index[elec_2016_mar['Puesto'] > 2])

#Determinamos el margen de victoria como la diff de pp entre primer y segundo lugar

elec_2006_mar1["Margen_vic"]= elec_2006_mar1["Peso"].shift(1)-elec_2006_mar1["Peso"]
elec_2006_mar1 = elec_2006_mar1.iloc[1: , :]
elec_2006_mar1=elec_2006_mar1.iloc[::2]
elec_2006_mar1["Margen_vic"] = elec_2006_mar1["Margen_vic"].abs()

elec_2010_mar1["Margen_vic"]= elec_2010_mar1["Peso"].shift(1)-elec_2010_mar1["Peso"]
elec_2010_mar1 = elec_2010_mar1.iloc[1: , :]
elec_2010_mar1=elec_2010_mar1.iloc[::2]
elec_2010_mar1["Margen_vic"] = elec_2010_mar1["Margen_vic"].abs()

elec_2016_mar1["Margen_vic"]= elec_2016_mar1["Peso"].shift(1)-elec_2016_mar1["Peso"]
elec_2016_mar1 = elec_2016_mar1.iloc[1: , :]
elec_2016_mar1=elec_2016_mar1.iloc[::2]
elec_2016_mar1["Margen_vic"] = elec_2016_mar1["Margen_vic"].abs()

#Se unen las bases

frames_mar1 = [elec_2010_mar1, elec_2016_mar1, elec_2006_mar1]

panel_mar = pd.concat(frames_mar1)

panel_mar = panel_mar.drop(panel_mar.columns[[2, 4, 5, 6]], axis=1)

#Borramos dfs intermedios

del frames_mar1, elec_2010_mar1, elec_2016_mar1, elec_2006_mar1, abn

#-----------------------------------------------------------------------------

#Unimos ambos paneles

panel_abs_mar = pd.merge(panel_mar, panel_abs, on=["Provincia", "Canton", "Año"])









