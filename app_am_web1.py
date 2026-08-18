import streamlit as st

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

iris = load_iris()

X = iris.data
y = iris.target

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, y)

st.title("Classificação/Predição da flor iris")

st.write("Informe as características")
sepal_length = st.number_input("Comprimento da sépala", min_value=0.0, value=5.0)
sepal_width = st.number_input("Largura da sépala", min_value=0.0, value=3.0)
petal_length = st.number_input("Comprimento da pétala", min_value=0.0, value=1.5)
petal_width = st.number_input("Largura da pétala", min_value=0.0, value=0.2)
if st.button("Classificar"):
    dados = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    previsao = modelo.predict(dados)
    nome = iris.target_names[previsao[0]]
    st.success(
        f"A flor foi classificada como: {nome}"
    )

    probabilidades = modelo.predict_proba(dados)
    st.write(probabilidades)

    for i, especie in enumerate(iris.target_names):
        st.write(
            f"{especie}: "
            f"{probabilidades[0][i]:.2%}"
        )


df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
st.line_chart(df)
st.bar_chart(df)