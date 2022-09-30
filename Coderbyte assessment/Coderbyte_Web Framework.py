import streamlit as st
import json
number1 = st.number_input('Enter input A')
number2 = st.number_input('Enter input B')
def callback():
         st.session_state.button_clicked =True
if number1!=0 and number2!=0:
    add=number1+number2
    sub=number1-number2
    mul=number1*number2
    div=number1/number2
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
if(st.button('Result' , on_click=callback)or st.session_state.button_clicked):
    obj = {"Addition": add, "Subtraction": sub, "Multiplication": mul,"Division": div}
    st.json({
        'Addition': add,
        'Subtraction': sub,
        'Multiplication': mul,
        'Division':div
        })

