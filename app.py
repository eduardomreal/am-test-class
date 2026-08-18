import streamlit as st
import pandas as pd
dados = {
    "Nome": ["Guilherme", "Natieli", "Eduardo", "Nicóle"],
    "Nota": [8.5, 9.0, 8.0, 8.8]
}
df = pd.DataFrame(dados)
st.dataframe(df)

dataset = st.file_uploader("Envie um arquivo CSV", type=["csv"])
if dataset is not None:
    df = pd.read_csv(dataset)
    st.write("Dados carregados:")
    st.dataframe(df)