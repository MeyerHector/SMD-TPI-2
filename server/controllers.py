import pandas as pd
from typing import Any, Dict


df = pd.read_csv('netflix.csv')

# funcion asincrona que devuelve un diccionario que puede tener strings o any
async def get_country() -> Dict[str, Any]:

    # el formato original es mes dia, año (June 5, 2005), elimino el mes y dia y me quedo con el año
    df['Country'] = df['Country'].str.split(',').str[0]

    frecuencias = df['Country'].value_counts()
    frecuencias_df = frecuencias.reset_index()
    frecuencias_df.columns = ['xi', 'fi']
    frecuencias_df['Fi'] = frecuencias_df['fi'].cumsum()
    frecuencias_df['ri'] = (frecuencias_df['fi'] / frecuencias_df['fi'].sum())
    frecuencias_df['Ri'] = frecuencias_df['ri'].cumsum()
    frecuencias_df['pi'] = (frecuencias_df['ri'] * 100)
    frecuencias_df['Pi'] = (frecuencias_df['pi'].cumsum())

    # selecciona las filas donde el porcentaje es menor a 2
    menor_a_uno = frecuencias_df.loc[frecuencias_df['pi'] < 2]

    # suma los valores de estas filas
    total_fi = menor_a_uno['fi'].sum()
    total_Fi = total_fi + frecuencias_df.loc[frecuencias_df['pi'] >= 1, 'fi'].sum()
    total_ri = total_fi / df['Country'].count()
    total_Ri = total_ri + frecuencias_df.loc[frecuencias_df['pi'] >= 1, 'ri'].sum()
    total_pi = total_ri * 100
    total_Pi = total_Ri * 100

    # crea una nueva fila con el total
    nueva_fila = {'xi': 'Otros', 'fi': total_fi, 'Fi': total_Fi, 'ri': total_ri, 'Ri': total_Ri, 'pi': total_pi, 'Pi': total_Pi}

    # añade la nueva fila al df
    frecuencias_df = frecuencias_df._append(nueva_fila, ignore_index=True)

    # elimina las filas con porcentaje menor a 2
    frecuencias_df = frecuencias_df.loc[frecuencias_df['pi'] >= 2]

    # retorno como diccionario 
    return frecuencias_df.to_dict(orient="records")
    

async def get_rating() -> Dict[str, Any]:
    frecuencias = df['Rating'].value_counts()
    frecuencias_df = frecuencias.reset_index()
    frecuencias_df.columns = ['xi', 'fi']
    frecuencias_df['Fi'] = frecuencias_df['fi'].cumsum()
    frecuencias_df['ri'] = (frecuencias_df['fi'] / frecuencias_df['fi'].sum())
    frecuencias_df['Ri'] = frecuencias_df['ri'].cumsum()
    frecuencias_df['pi'] = (frecuencias_df['ri'] * 100)
    frecuencias_df['Pi'] = (frecuencias_df['pi'].cumsum())
    return frecuencias_df.to_dict(orient="records")
    


async def get_category() -> Dict[str, Any]:
    frecuencias = df['Category'].value_counts()
    frecuencias_df = frecuencias.reset_index()
    frecuencias_df.columns = ['xi', 'fi']
    frecuencias_df['Fi'] = frecuencias_df['fi'].cumsum()
    frecuencias_df['ri'] = (frecuencias_df['fi'] / frecuencias_df['fi'].sum())
    frecuencias_df['Ri'] = frecuencias_df['ri'].cumsum()
    frecuencias_df['pi'] = (frecuencias_df['ri'] * 100)
    frecuencias_df['Pi'] = (frecuencias_df['pi'].cumsum())
    return frecuencias_df.to_dict(orient="records")

async def get_realese() -> Dict[str, Any]:
    # convierte la columna 'Realese_Date' a datetime de pandas
    df['Realese_Date'] = pd.to_datetime(df['Realese_Date'])
    
    # extrae el año y crea una nueva columna 'Year'
    df['Year'] = df['Realese_Date'].dt.year

    frecuencias = df['Year'].value_counts()
    frecuencias_df = frecuencias.reset_index()
    frecuencias_df.columns = ['xi', 'fi']
    frecuencias_df['Fi'] = frecuencias_df['fi'].cumsum()
    frecuencias_df['ri'] = (frecuencias_df['fi'] / frecuencias_df['fi'].sum())
    frecuencias_df['Ri'] = frecuencias_df['ri'].cumsum()
    frecuencias_df['pi'] = (frecuencias_df['ri'] * 100)
    frecuencias_df['Pi'] = (frecuencias_df['pi'].cumsum())
    return frecuencias_df.to_dict(orient="records")


async def get_realese() -> Dict[str, Any]:
    df['Release_Date'] = df['Release_Date'].str.strip()

    # convierte la columna 'Release_Date' a datetime
    df['Release_Date'] = pd.to_datetime(df['Release_Date'])

    # extrae el año y crea una nueva columna 'Year'
    df['Year'] = df['Release_Date'].dt.year


    frecuencias = df['Year'].value_counts()
    frecuencias_df = frecuencias.reset_index()
    frecuencias_df.columns = ['xi', 'fi']
    frecuencias_df['Fi'] = frecuencias_df['fi'].cumsum()
    frecuencias_df['ri'] = (frecuencias_df['fi'] / frecuencias_df['fi'].sum())
    frecuencias_df['Ri'] = frecuencias_df['ri'].cumsum()
    frecuencias_df['pi'] = (frecuencias_df['ri'] * 100)
    frecuencias_df['Pi'] = (frecuencias_df['pi'].cumsum())
    frecuencias_df = frecuencias_df.sort_values('xi')
    return frecuencias_df.to_dict(orient="records")