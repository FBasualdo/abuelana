import streamlit as st
import pandas as pd

def browser(price_products_list, price_weight_list, container, query):
    filtered_data1 = price_products_list[price_products_list['Lista de Productos'].str.contains(query, case=False)]
    filtered_data2 = price_weight_list[price_weight_list['Lista de Productos'].str.contains(query, case=False)]

    combined_results = pd.concat([filtered_data1,filtered_data2])
    combined_results.rename(columns={'Marca' : 'Marca/Peso'}, inplace=True)
    if not combined_results.empty:
        combined_results['Marca/Peso'].fillna(combined_results['Peso'], inplace=True)
        combined_results.drop(columns=['Peso'], inplace=True)
        container.dataframe(combined_results, use_container_width=True, hide_index=True)