import pandas as pd
import numpy as np


cgr = pd.read_excel("/Users/andrecamposreyes/Documents/DataCleaning/data/0-raw_data/municipalities_expenditure/municipalities_expenditure_2.xlsx", sheet_name="Sheet1")


#Selection of variables

cgr_v1 = cgr[#Remuneraciones
              (cgr['Subpartida (COG)'] == '0.01.01--Sueldos para cargos fijos')
              | (cgr['Subpartida (COG)'] == '0.02.01--Tiempo extraordinario') 
              | (cgr['Subpartida (COG)'] == '0.02.05--Dietas') 
              #Servicios 
              | (cgr['Subpartida (COG)'] == '1.01.01--Alquiler de edificios, locales y terrenos') 
              | (cgr['Subpartida (COG)'] == '1.01.02--Alquiler de maquinaria, equipo y mobiliario') 
              | (cgr['Subpartida (COG)'] == '1.03.02--Publicidad y propaganda') 
              | (cgr['Subpartida (COG)'] == '1.07.02--Actividades protocolarias y sociales') 
              | (cgr['Subpartida (COG)'] == '1.08.01--Mantenimiento de edificios, locales y terrenos') 
              | (cgr['Subpartida (COG)'] == '1.08.02--Mantenimiento de vías de comunicación') 
              | (cgr['Subpartida (COG)'] == '1.08.03--Mantenimiento de instalaciones y otras obras')  
              #Bienes duraderos
              | (cgr['Subpartida (COG)'] == '5.01.01--Maquinaria y equipo para la producción') 
              | (cgr['Subpartida (COG)'] == '5.01.02--Equipo de transporte') 
              | (cgr['Subpartida (COG)'] == '5.02.01--Edificios') 
              | (cgr['Subpartida (COG)'] == '5.02.02--Vías de comunicación terrestre') 
              | (cgr['Subpartida (COG)'] == '5.02.07--Instalaciones') 
              | (cgr['Subpartida (COG)'] == '5.03.01--Terrenos') 
              | (cgr['Subpartida (COG)'] == '5.03.02--Edificios preexistentes') 
              ] 

#Reshape of the dataframe

cgr_v2 = cgr_v1.pivot(index=('Año del presupuesto','Nombre de la institución'), columns=['Subpartida (COG)'], values=['Ejecución Aprob.'])

#Rename of the variables

cgr_v3 = cgr_v2.rename(columns={'0.01.01--Sueldos para cargos fijos':'salaries',
                                    '0.02.01--Tiempo extraordinario':'ext_time',
                                    '0.02.05--Dietas':'sub_all',
                                    '1.01.01--Alquiler de edificios, locales y terrenos':'rent_bcl',
                                    '1.01.02--Alquiler de maquinaria, equipo y mobiliario':'rent_mef',
                                    '1.03.02--Publicidad y propaganda':'publicity',
                                    '1.07.02--Actividades protocolarias y sociales':'activities',
                                    '1.08.01--Mantenimiento de edificios, locales y terrenos':'main_bcl',
                                    '1.08.02--Mantenimiento de vías de comunicación':"main_roads",
                                    '1.08.03--Mantenimiento de instalaciones y otras obras':'main_other',
                                    '5.01.01--Maquinaria y equipo para la producción':'cap_me',
                                    '5.01.02--Equipo de transporte':'cap_trans',
                                    '5.02.01--Edificios':'cap_build',
                                    '5.02.02--Vías de comunicación terrestre':'cap_roads',
                                    '5.02.07--Instalaciones':'cap_install',
                                    '5.03.01--Terrenos':'pe_land',
                                    '5.03.02--Edificios preexistentes':'pe_build'
                                    })


cgr_v3.to_csv('cgr_clean.csv')


