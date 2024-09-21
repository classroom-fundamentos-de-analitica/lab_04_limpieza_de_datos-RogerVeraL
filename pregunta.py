"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    #
    # Inserte su código aquí
    #

    def limpiar_caracteres(df):
        return df.replace("-", " ", regex=True).replace("_", " ", regex=True)

    def normalizar_cadenas(df):
        return df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    
    def limpiar_monto(df):
        df["monto_del_credito"] = (
            df["monto_del_credito"].str.strip().str.replace("[,$]|(\\.00$)", "", regex=True).astype(float)
        )
        return df
    
    def clean_date(date):
        parts = date.split('/')
        if len(parts[2]) == 4:  
            return pd.to_datetime(date, dayfirst=True).strftime('%Y-%m-%d')
        else: 
            return pd.to_datetime(date, format='%Y/%m/%d').strftime('%Y-%m-%d')

    def limpiar_fechas(df):
        df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(clean_date)
        return df

    def convertir_comuna(df):
        df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
        return df
    
    data = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = data.copy()
    df = limpiar_caracteres(df)
    df = normalizar_cadenas(df)
    df = limpiar_monto(df)
    df = limpiar_fechas(df)
    df = convertir_comuna(df)
    df = df.drop_duplicates().dropna() # Eliminar duplicados y datos faltantes

    return df


clean_data()
#print(clean_data().sexo.value_counts().to_list())
#print(clean_data().tipo_de_emprendimiento.value_counts().to_list())
#print(clean_data().idea_negocio.value_counts().to_list())
#print(clean_data().línea_credito.value_counts().to_list() )

