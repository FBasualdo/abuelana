import streamlit as st
import pandas as pd
import threading
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

from program_functions import browser

st.set_page_config(layout="wide")
container = st.container()
container.header("Abuela Ana Tienda Natural 👩‍🌾")

price_weight_list = pd.read_csv('Granel.csv')
price_weight_list.columns = ['Lista de Productos', 'Peso', 'Precio']

price_products_list = pd.read_csv('Productos.csv')
price_products_list.columns = ['Lista de Productos', 'Marca', 'Precio']


query = container.text_input(placeholder="Ingrese el producto que quiera buscar 🔎",label="Buscador🔎", label_visibility= 'hidden')

if query:
    browser(price_products_list, price_weight_list, container, query)


tab1, tab2 = container.tabs(["Productos Empaquetados", "Productos a Granel"])  # Dividir en dos columnas

with st.sidebar:
    side_container = st.container()
    side_container.title("Sector de ventas 💰")




with tab1:
    container1 = st.container()
    container1.subheader("Productos Empaquetados 🍬")
    container1.dataframe(data=price_products_list, use_container_width=True, hide_index=True)

with tab2:
    container2 = st.container()
    container2.subheader("Productos a Granel 🌾")
    container2.dataframe(data=price_weight_list, use_container_width=True, hide_index=True)
