import datetime
import pandas as pd
import streamlit as st
from database import view_cars,view_cars_id,view_showroom_name,view_showroom,edit_cars,get_cars,get_details_showroom,edit_showroom,view_cust_id,get_cust,edit_customer,view_cust

def update():
    result = view_showroom()
    resultx = view_cars()
    resulty = view_cust()
    df = pd.DataFrame(result, columns=['NAME','SID','STATE','CITY','EMAIL','PHNO'])
    dfx = pd.DataFrame(resultx, columns=['ID','MAKE','MODEL','YEAR','PRICE','SID'])
    dfy = pd.DataFrame(resulty, columns=['CUSTID','CUSTNAME','CUSTEMAIL','CUSTPHNO','CARBOUGHT','CARBOUGHTID'])

    with st.expander("Current Details"):
        st.subheader("SHOWROOMS")
        st.dataframe(df)
        st.subheader("CARS")
        st.dataframe(dfx)
        st.subheader("CUSTOMERS")
        st.dataframe(dfy)
    list_of_names = [i[0] for i in view_showroom_name()]
    list_of_namesx = [i[0] for i in view_cars_id()]
    list_of_namesy = [i[0] for i in view_cust_id()]


    selected_name = st.selectbox("Showroom to Edit", list_of_names)
    selected_namex = st.selectbox("Which car to Edit", list_of_namesx)
    selected_namey = st.selectbox("Which customer to Edit", list_of_namesy)
    selected_result = get_details_showroom(selected_name)
    selected_resultx = get_cars(selected_namex)
    selected_resulty = get_cust(selected_namey)

    col1, col2,col3 = st.columns(3)
    # st.write(selected_result)'NAME','SID','STATE','CITY','EMAIL','PHNO'
    if selected_result:
        NAME = selected_result[0][0]
        SID = selected_result[0][1]
        STATE = selected_result[0][2]
        CITY = selected_result[0][3]
        EMAIL = selected_result[0][4]
        PHNO = selected_result[0][5]
        # Layout of Create
        with col1:
            st.subheader("Edit Showroom Details:")
            new_name = st.text_input("NAME:", NAME)
            newsid = st.text_input("SID:",SID)
            newstate = st.text_input("STATE:",STATE)
            newcity = st.text_input("CITY:",CITY)
            newemail = st.text_input("EMAIL:",EMAIL)
            newphno = st.text_input("PHNO:",PHNO)
        if st.button("Update Showroom Details"):
            edit_showroom(new_name,newsid,newstate,newcity,newemail,newphno,NAME,SID,STATE,CITY,EMAIL,PHNO)
            st.success("Successfully updated Showroom Details")

    if selected_resultx:
        ID = selected_resultx[0][0]
        MAKE = selected_resultx[0][1]
        MODEL = selected_resultx[0][2]
        YEAR = selected_resultx[0][3]
        PRICE = selected_resultx[0][4]
        SIDD = selected_resultx[0][5]
        # Layout of Create 'ID','MAKE','MODEL','YEAR','PRICE','SID'
        with col2:
            st.subheader("Edit Car Details:")
            new_id = st.text_input("ID:", ID)
            newmake = st.text_input("MAKE:",MAKE)
            newmodel = st.text_input("MODEL:",MODEL)
            newyear = st.text_input("YEAR:",YEAR)
            newprice = st.text_input("PRICE:",PRICE)
            newsidx = st.text_input("SIDD:",SIDD)
        if st.button("Update Car Details"):
            edit_cars(new_id,newmake,newmodel,newyear,newprice,newsidx,ID,MAKE,MODEL,YEAR,PRICE,SIDD)
            st.success("Successfully updated Car Details")
    if selected_resulty:
        #CUSTID ,CUSTNAME, EMAIL, PHNO, CARBOUGHT,CARBOUGHTID
        CUSTID = selected_resulty[0][0]
        CUSTNAME = selected_resulty[0][1]
        CUSTEMAIL = selected_resulty[0][2]
        CUSTPHNO = selected_resulty[0][3]
        CARBOUGHT = selected_resulty[0][4]
        CARBOUGHTID = selected_resulty[0][5]
        # Layout of Create
        with col3:
            st.subheader("Edit Customer Details:")
            newcustid = st.text_input("CUSTID:", CUSTID)
            newcustname = st.text_input("CUSTNAME:",CUSTNAME)
            newcustemail = st.text_input("CUSTEMAIL:",CUSTEMAIL)
            newcustphno = st.text_input("CUSTPHNO:",CUSTPHNO)
            newcarbought = st.text_input("CARBOUGHT:",CARBOUGHT)
            newcarboughtid = st.text_input("CARBOUGHTID:",CARBOUGHTID)
        if st.button("Update Customer Details"):
            edit_customer(newcustid,newcustname,newcustemail,newcustphno,newcarbought,newcarboughtid,CUSTID,CUSTNAME,CUSTEMAIL,CUSTPHNO,CARBOUGHT,CARBOUGHTID)
            st.success("Successfully updated Customer Details")

    with st.expander("Updated data"):
        st.subheader("SHOWROOMS")
        st.dataframe(df)
        st.subheader("CARS")
        st.dataframe(dfx)
        st.subheader("CUSTOMERS")
        st.dataframe(dfy)


    