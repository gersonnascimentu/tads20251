plot_ts.py:
def plot(ticker:str):
    data = yf.download(ticker, period='max', multi_level_index = False)
    df= data.reset_index()(['Date', 'Close'])

    fig= px.line(df,
        x= 'Date',
        y= 'Close',
        )



app.py:
import streamlit as st
#essa ferramenta vai criar o applicativo com a interface
from functions.plot_ts import plot

st.title('Histórico de cotações')
st.write('Veja o histórico das cotações das empresas')

ticker = st.sidebar.text_input('Escolha o ticker: ', value='AAPL')

fig = plot(ticker)
st.plotly_chart(fig)

# streamlit run app.py (serve para abrir o navegador na nova guia)
# yahoo finanças (acessar site para verificar os dados da api)

# git checkout -b build/app (serve ára blindar o app)



draft.py:

from functions.plot_ts import plot

plot(ticker = 'TAE4.SA')



requeriments.txt:

streamlit==1.48.1
yfinance==0.2.65
plotly==6.3.0


