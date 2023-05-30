import yfinance as yf
import streamlit as st

# Отображаем заголовок приложения с помощью функции st.write()
st.write("""
# Котировки компании Apple за последние 10 лет
Показать цену **открытия** и цену **закрытия** акций Apple, а также **объем торгов**
""")

tikerSymbol = 'AAPL'

# Получаем данные по акции Apple с помощью метода yf.Ticker()
tickerData = yf.Ticker(tikerSymbol)

# Создаем таблицу, содержащую историю цен на акции Apple за период одного дня, начиная с 31 мая 2010 года до 31 мая 2020 года
tikerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.snow()
# Отображаем график цен на открытие акций с помощью функции st.line_chart()
st.write("## Цена открытия")
st.area_chart(tikerDf.Open.rename("Цена открытия"))


# Отображаем график цен на закрытие акций с помощью функции st.line_chart()
st.write("## Цена закрытия")
st.line_chart(tikerDf.Close.rename("Цена закрытия"))

# Отображаем график объема торгов с помощью функции st.line_chart()
st.write("## Объем торгов")
st.bar_chart(tikerDf.Volume.rename("Объем торгов"))
