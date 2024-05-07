import pandas as pd
from typing import Any, Dict


df = pd.read_csv('netflix.csv')

async def get_country() -> Dict[str, Any]:
    df['Country'] = df['Country'].str.split(',').str[0]

    frecuencias = df['Country'].value_counts()
    frecuencias_df = frecuencias.reset_index()
    frecuencias_df.columns = ['xi', 'fi']
    frecuencias_df['Fi'] = frecuencias_df['fi'].cumsum()
    frecuencias_df['ri'] = (frecuencias_df['fi'] / frecuencias_df['fi'].sum())
    frecuencias_df['Ri'] = frecuencias_df['ri'].cumsum()
    frecuencias_df['pi'] = (frecuencias_df['ri'] * 100)
    frecuencias_df['Pi'] = (frecuencias_df['pi'].cumsum())

    # Selecciona las filas donde el porcentaje es menor a 1
    menor_a_uno = frecuencias_df.loc[frecuencias_df['pi'] < 2]

    # Suma los valores de estas filas
    total_fi = menor_a_uno['fi'].sum()
    total_Fi = total_fi + frecuencias_df.loc[frecuencias_df['pi'] >= 1, 'fi'].sum()
    total_ri = total_fi / df['Country'].count()
    total_Ri = total_ri + frecuencias_df.loc[frecuencias_df['pi'] >= 1, 'ri'].sum()
    total_pi = total_ri * 100
    total_Pi = total_Ri * 100

    # Crea una nueva fila con el total
    nueva_fila = {'xi': 'Otros', 'fi': total_fi, 'Fi': total_Fi, 'ri': total_ri, 'Ri': total_Ri, 'pi': total_pi, 'Pi': total_Pi}

    # Añade la nueva fila al DataFrame
    frecuencias_df = frecuencias_df._append(nueva_fila, ignore_index=True)

    # Elimina las filas con porcentaje menor a 1
    frecuencias_df = frecuencias_df.loc[frecuencias_df['pi'] >= 2]
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
    # Convierte la columna 'Realese_Date' a datetime
    df['Realese_Date'] = pd.to_datetime(df['Realese_Date'])
    
    # Extrae el año y crea una nueva columna 'Year'
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

    # Convierte la columna 'Release_Date' a datetime
    df['Release_Date'] = pd.to_datetime(df['Release_Date'])

    # Extrae el año y crea una nueva columna 'Year'
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