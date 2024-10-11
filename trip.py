import streamlit as st

st.set_page_config(
    page_title="수학여행 안내 사항",
    page_icon="\U0001F680",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("수학여행 안내사항")

if st.button("수학여행", icon="😃"):
    st.balloons()

image1 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5203.jpg"
image2 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5204.jpg"
image3 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5205.jpg"
image4 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5206.jpg"
image5 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5207.jpg"
image6 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5208.jpg"
image7 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5209.jpg"
image8 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5210.jpg"
image9 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5211.jpg"
image10 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5212.jpg"
image11 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5213.jpg"
image12 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5214.jpg"
image13 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5191.jpg"


col1, col2 = st.columns(2)


with col1:
    st.image(image13)
    st.image(image2)
    st.image(image4)
    st.image(image6)
    st.image(image8)
    st.image(image10)
    st.image(image12)

with col2:
    st.image(image1)
    st.image(image3)
    st.image(image5)
    st.image(image7)
    st.image(image9)
    st.image(image11)

