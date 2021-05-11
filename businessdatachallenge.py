
##Dependencies
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-muted')
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

df = pd.read_csv('Challenge Data.csv',sep = ";" )
df['Stars'] = df['Stars'].str.split().str[0]
df['Stars']= df['Stars'].astype(str).astype(int)


st.set_page_config(page_title='BDC 2021', layout="wide")

st.title('Business Data Challenge')
st.subheader('Challenge from VVA')
st.markdown('Group H')
image = Image.open('banner.jpg')
st.image(image)
st.markdown('**Data Explorer**')
st.sidebar.markdown("**Stars**")
stars = st.sidebar.slider("", value=0, min_value=1, max_value=5, step=1)
st.sidebar.markdown("**Name**")
names = st.sidebar.text_input('')
st.sidebar.markdown("**Word in Review**")
reviews_op = st.sidebar.text_input(' ')
if (stars == 0) & (names == '') & (reviews_op == ''):
    st.write(df)
elif (stars == 0) & (names != '') or (reviews_op != ''):
    st.write(df[( df.Name.str.contains(names)) & ( df.Review.str.contains(reviews_op))])
else:
    st.write(df[(df.Stars==stars) & ( df.Name.str.contains(names)) & ( df.Review.str.contains(reviews_op))])
