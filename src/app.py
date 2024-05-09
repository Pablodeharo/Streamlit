import streamlit as st
from joblib import load

# Cargar el modelo entrenado
modelo = load("C:/Users/lenovo/Desktop/Proyectos Machine Learning/Bootcamp/Streamlit/models/modelo_regresion_lineal.joblib")

# Título de la aplicación
st.title("Predicción de Sueldo")

# Descripción
st.write("""
Esta aplicación predice el sueldo en base a los años de experiencia.
""")

# Interfaz de usuario para ingresar los años de experiencia
años_de_experiencia = st.slider('Años de Experiencia', 0, 20, 5)

# Predecir el sueldo
sueldo_predicho = modelo.predict([[años_de_experiencia]])

# Mostrar el sueldo predicho
st.subheader('Sueldo Predicho')
st.write(f'El sueldo predicho para {años_de_experiencia} años de experiencia es: ${sueldo_predicho[0]:,.2f}')