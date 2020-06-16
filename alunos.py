import streamlit as st
import pandas as pd


def main():
    st.title("AceleraDev Data Science")
    st.image("logo.png")

    # Carregando DataFrame
    # Mostrar os registros dinamicamente, de acordo com o valor escolhido no slider
    slider = st.slider("Values: ", 0, 100)
    st.markdown("Função Dataframe")
    df = pd.read_csv("IRIS.csv")
    st.dataframe(df.head(slider))

    st.markdown("Função Table")
    st.table(df.head(slider))  # Plotando Dataframe de outra forma

    st.write(df.columns)
    # Retorna as medias dos tamanhos das petalas, agrupadas pelas especies
    st.table(df.groupby("species")["petal_width"].mean())

    # Carregando DataFrame com o file uploader
    # file = st.file_uploader("Upload your Dataframe: ", type="csv")
    # if file is not None:
    #    df = pd.read_csv(file)
    #    st.dataframe(df.head())


if __name__ == '__main__':
    main()
