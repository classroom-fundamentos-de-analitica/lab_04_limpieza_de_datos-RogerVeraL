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

    def monto_del_credito(df):
        df["monto_del_credito"] = (
            df["monto_del_credito"].str.strip().str.replace("[,$]|(\\.00$)", "", regex=True).astype(float)
        )
        return df
    def fecha_de_beneficio(df):
        df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y")
        return df
        

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df = df.replace("-", " ", regex=True).replace("_", " ", regex=True)
    df["sexo"] = df["sexo"].str.lower()
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df = df.drop_duplicates().dropna()
    df = monto_del_credito(df)

    return df


cleaned_data = clean_data()
print(cleaned_data.head())