#Base agregada media

import pandas as pd
import numpy as np

cgr = pd.read_excel("/Users/andrecamposreyes/Documents/DataCleaning/data/0-raw_data/municipalities_expenditure/municipalities_expenditure_1.xlsx", sheet_name="Sheet1")

#From object to numeric: 
cgr['Ejecución Aprob.'] = cgr['Ejecución Aprob.'].str.replace('.','')
cgr['Ejecución Aprob.'] = cgr['Ejecución Aprob.'].str.replace(',','.')
cgr['Ejecución Aprob.'] = cgr['Ejecución Aprob.'].astype(float, errors = 'raise')

print(cgr.dtypes)


#Selection of variables

cgr_v1a = cgr[#Remuneraciones
              (cgr['Grupo Subpartida (COG)'] == '0.01.00--REMUNERACIONES BÁSICAS')
              | (cgr['Grupo Subpartida (COG)'] == '0.02.00--REMUNERACIONES EVENTUALES')
              #Servicios
              | (cgr['Grupo Subpartida (COG)'] == '1.01.00--ALQUILERES') 
              | (cgr['Grupo Subpartida (COG)'] == '1.03.00--SERVICIOS COMERCIALES Y FINANCIEROS') 
              | (cgr['Grupo Subpartida (COG)'] == '1.07.00--CAPACITACIÓN Y PROTOCOLO') 
              | (cgr['Grupo Subpartida (COG)'] == '1.08.00--MANTENIMIENTO Y REPARACIÓN') 
              #Bienes duraderos
              | (cgr['Grupo Subpartida (COG)'] == '5.01.00--MAQUINARIA, EQUIPO Y MOBILIARIO') 
              | (cgr['Grupo Subpartida (COG)'] == '5.02.00--CONSTRUCCIONES, ADICIONES Y MEJORAS') 
              | (cgr['Grupo Subpartida (COG)'] == '5.03.00--BIENES PREEXISTENTES') 
              ] 

#Index Names

cgr_v1b = cgr_v1a.rename(columns ={'Año del presupuesto':'year',
                              'Nombre de la institución':'municipality'})

#Reshape

cgr_v2 = cgr_v1b.pivot_table(values='Ejecución Aprob.', 
        index=['year','municipality'], 
        columns='Grupo Subpartida (COG)', 
        aggfunc=np.sum)
               
#Rename of variables 

cgr_v3 = cgr_v2.rename(columns={'0.01.00--REMUNERACIONES BÁSICAS':'remu_bas',
                                '0.02.00--REMUNERACIONES EVENTUALES':'remu_ev',
                                '1.01.00--ALQUILERES':'rentals',
                                '1.03.00--SERVICIOS COMERCIALES Y FINANCIEROS':'serv_cf',
                                '1.07.00--CAPACITACIÓN Y PROTOCOLO':'cap_prot',
                                '1.08.00--MANTENIMIENTO Y REPARACIÓN':'maintenance',
                                '5.01.00--MAQUINARIA, EQUIPO Y MOBILIARIO':'cap_mef',
                                '5.02.00--CONSTRUCCIONES, ADICIONES Y MEJORAS':'cap_cai', 
                                '5.03.00--BIENES PREEXISTENTES':'pe_goods' 
                                })

cgr_v3.to_csv('cgr_clean.csv (Agregado Medio)')


#Missing Values 

print(cgr_v3.isna().sum())
