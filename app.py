import streamlit as st
from functions.plot_ts import plot

st.title('Histórico de cotações')
st.write('Veja o histórico das cotações das empresas.')

ticker = st.sidebar.text_input('Escolha o ticker:', value = 'AAPL')

fig = plot(ticker)
st.plotly_chart(fig)