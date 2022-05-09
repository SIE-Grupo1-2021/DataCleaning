#Base agregada

import pandas as pd
import numpy as np


cgr = pd.read_excel("/Users/andrecamposreyes/Documents/DataCleaning/data/0-raw_data/municipalities_expenditure/municipalities_expenditure_aggregated.xls", sheet_name="Sheet1")

print(cgr.dtypes) #Variables in a good format 

#Selection of variables 


cgr_v1a = cgr[(cgr['Partida (COG)'] == '0.00.00--REMUNERACIONES')
              | (cgr['Partida (COG)'] == '1.00.00--SERVICIOS')
              | (cgr['Partida (COG)'] == '5.00.00--BIENES DURADEROS') 
              ] 

#Rename Index

cgr_v1b = cgr_v1a.rename(columns ={'Año del presupuesto':'year',
                              'Nombre de la institución':'municipality'})

#Reshape of the dataframe

cgr_v2 = cgr_v1b.pivot_table(values='Gasto Real', 
         index=['year','municipality'], 
         columns=['Partida (COG)'])

#Rename of the variables

cgr_v3 = cgr_v2.rename(columns={'0.00.00--REMUNERACIONES':'remu',
                                '1.00.00--SERVICIOS':'serv',
                                '5.00.00--BIENES DURADEROS':'d_goods'
                                })



cgr_v3.to_csv('cgr_clean.csv (Agregado)')


#Missing Values
print(cgr_v3.isna().sum())


