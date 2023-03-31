import streamlit as st
from PIL import Image
st.title('エイプリルフールです')
st.caption('突貫3時間クオリティ...')

image = Image.open('./data/haxa-.jpg')
st.image(image, width=300)
