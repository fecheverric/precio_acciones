import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
    # Aplicación simple de precio de acciones

    Acá se puede ver el precio de cierre y el volumen de la acción de Google
""")

#Definir el ticker
tickerSymbol = 'GOOGL'

#Conseguir los datos en este ticker
tickerData = yf.Ticker(tickerSymbol)

#Conseguir los precios históricos para la temporalidad deseada en este ticker
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2021-5-31')

#Graficar
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

#Se ejecuta correctamente con el comando streamlit run codigo.py
#Outdated en Python 3.10

#Como obtener datos de acciones en Python
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75