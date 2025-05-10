import streamlit as st
st.write("hello World")
x=st.text_input("Favourite Movie?")
st.write(f" Your favourite movie is {x}")
import pandas as pd
df=pd.read_csv('train.csv')
st.write(df)
df1=pd.read_csv('iris.csv')
st.write(df1)
st.bar_chart(df1)
st.line_chart(df1)