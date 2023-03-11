import streamlit as st
from database import add_data_to_showroom,add_data_to_cars,add_data_to_car_details,add_data_to_customer

def create():
    col1, col2, col3,col4 = st.columns(4)
    with col1:
            st.header("SHOW ROOM")
            NAME=st.text_input("NAME:")
            SID=st.text_input("SID:")
            STATE=st.text_input("STATE:")
            CITY=st.text_input("CITY:")
            EMAIL=st.text_input("EMAIL:")
            PHNO=st.text_input("PHNO:")
    if st.button("Add SHOWROOM"):
            add_data_to_showroom(NAME,SID,STATE,CITY,EMAIL,PHNO)
            st.success("Successfully added SHOWROOM: ")

    with col2:
            st.header("  CARS")
            ID=st.text_input("ID:")
            MAKE=st.text_input("MAKE:")
            MODEL=st.text_input("MODEL:")
            YEAR=st.text_input("YEAR:")
            PRICE=st.text_input("PRICE:")
            SIDD=st.text_input("SIDD:")
    if st.button("Add CAR"):
            add_data_to_cars(ID,MAKE,MODEL,YEAR,PRICE,SIDD)
            st.success("Successfully added CAR: ")      

    with col3:
            st.header("CAR DETAILS")
            MAKEOFCAR=st.text_input("MAKEOFCAR:")
            MODELOFCAR=st.text_input("MODELOFCAR:")
            YEAROFCAR=st.text_input("YEAROFCAR:")
            TYPE=st.text_input("TYPE:")
            DISP=st.text_input("DISP:")
            POWER=st.text_input("POWER:")
            FUELTYPE = st.radio("FUELTYPE",["PETROL", "DIESEL","ELECTRIC"])
            FUELCONS=st.text_input("FUELCONS:")
    if st.button("Add CAR DETAILS"):
            add_data_to_car_details(MAKEOFCAR,MODELOFCAR,YEAROFCAR,TYPE,DISP,POWER,FUELTYPE,FUELCONS)
            st.success("Successfully added CAR SPEC: ")
    with col4:
            #CUSTID ,CUSTNAME, EMAIL, PHNO, CARBOUGHT,CARBOUGHTID
            st.header("CUSTOMER DETAILS")
            CUSTID=st.text_input("CUSTID:")
            CUSTNAME=st.text_input("CUSTNAME:")
            CUSTEMAIL=st.text_input("CSUTEMAIL:")
            CUSTPHNO=st.text_input("CUSTPHNO:")
            CARBOUGHT=st.text_input("CARBOUGHT:")
            CARBOUGHTID=st.text_input("CARBOUGHTID:")
    if st.button("Add CUSTOMER DETAILS"):
            add_data_to_customer(CUSTID,CUSTNAME,CUSTEMAIL,CUSTPHNO,CARBOUGHT,CARBOUGHTID)
            st.success("Successfully added CUSTOMER Details: ")
        

            
