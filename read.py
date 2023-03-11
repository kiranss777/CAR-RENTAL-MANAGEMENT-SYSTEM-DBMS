import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_cars,view_showroom,view_cars_specs,view_cust


def read():
    result2 = view_cars()
    result = view_showroom()
    result3=view_cars_specs()
    result4=view_cust()

    #st.write(result)
    df = pd.DataFrame(result, columns=['NAME','SID','STATE','CITY','EMAIL','PHNO'])
    df2 = pd.DataFrame(result2, columns=['ID','MAKE','MODEL','YEAR','PRICE','SID'])
    df3 = pd.DataFrame(result3, columns=['MAKE','MODEL','YEAR','TYPE','DISP','POWER','FUELTYPE','FUELCONS'])
    df4 = pd.DataFrame(result4, columns=['CUSTID','CUSTNAME','CUSTEMAIL','CUSTPHNO','CARBOUGHT','CARBOUGHTID'])

    with st.expander("View Details"):
        st.subheader("SHOWROOMS")
        st.dataframe(df)
        st.subheader("CARS AVAILABLE")
        st.dataframe(df2)
        st.subheader("CAR SPECS")
        st.dataframe(df3)
        st.subheader("CUSTOMER DETAILS")
        st.dataframe(df4)
