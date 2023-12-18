import streamlit as st
view = [100,150,30]
st.write('# 조희원')
st.write('## 박지성')
view
st.write('## 바 차트입니다')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview