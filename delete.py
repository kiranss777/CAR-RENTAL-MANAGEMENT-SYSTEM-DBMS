import pandas as pd
import streamlit as st
from database import view_cars_id,view_showroom,view_showroom_name,view_cars_specs,view_cars,view_cars_specs_model,delete_showroom,delete_car,delete_specs,view_cust,view_cust_name,delete_cust
def delete():
    result = view_showroom()
    df = pd.DataFrame(result, columns=['NAME','SID','STATE','CITY','EMAIL','PHNO'])
    new_result = view_cars()
    df2 = pd.DataFrame(new_result, columns=['ID','MAKE','MODEL','YEAR','PRICE','SID'])
    new_result2=view_cars_specs()
    df3 = pd.DataFrame(new_result2, columns=['MAKE','MODEL','YEAR','TYPE','DISP','POWER','FUELTYPE','FUELCONS'])
    new_result3=view_cust()
    df4 = pd.DataFrame(new_result3, columns=['CUSTID','CUSTNAME','CUSTEMAIL','CUSTPHNO','CARBOUGHT','CARBOUGHTID'])
    with st.expander("Current data"):
        st.dataframe(df)
        st.dataframe(df2)
        st.dataframe(df3)
        st.dataframe(df4)

    list_of_names = [i[0] for i in view_showroom_name()]
    selected_name = st.selectbox("Data to Delete", list_of_names)
    st.warning("Do you want to delete ::{}".format(selected_name))
    if st.button("Delete Showroom"):
        delete_showroom(selected_name)
        st.success("Showroom deleted successfully")
    
    
    list_of_names2 = [i[0] for i in view_cars_id()]
    selected_name2 = st.selectbox("Which Data to Delete", list_of_names2)
    st.warning("Do you want to delete ::{}".format(selected_name2))
    if st.button("Delete car"):
        delete_car(selected_name2)
        st.success("Car deleted successfully")
    #with st.expander("Updated data"):
    #    st.dataframe(df2)
    
    list_of_names3 = [i[0] for i in view_cars_specs_model()]
    selected_name3 = st.selectbox("Whose Data to Delete", list_of_names3)
    st.warning("Do you want to delete specs of ::{}".format(selected_name3))
    if st.button("Delete car Specs"):
        delete_specs(selected_name3)
        st.success("Car specs deleted successfully")
    
    list_of_names4 = [i[0] for i in view_cust_name()]
    selected_name4 = st.selectbox("Which Customer Data to Delete", list_of_names4)
    st.warning("Do you want to delete Details of ::{}".format(selected_name4))
    if st.button("Delete Customer Details"):
        delete_cust(selected_name4)
        st.success("Customer deleted successfully")



    with st.expander("Updated data"):
        st.dataframe(df)
        st.dataframe(df2)
        st.dataframe(df3)
        st.dataframe(df4)
