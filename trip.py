import streamlit as st

st.set_page_config(
    page_title="수학여행 안내 사항",
    page_icon="\U0001F680",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("수학여행 안내사항")


image1 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5190.jpg"
image2 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5191.jpg"
image3 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5192.jpg"
image4 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5193.jpg"
image5 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5194.jpg"
image6 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5195.jpg"
image7 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5196.jpg"
image8 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5197.jpg"
image9 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5198.jpg"
image10 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5199.jpg"
image11 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5200.jpg"
image12 = "https://raw.githubusercontent.com/heeonme/streamlit1/main/IMG_5201.jpg"


col1, col2 = st.columns(2)

with col1:
    st.image(image2)
    st.image(image4)
    st.image(image6)
    st.image(image8)
    st.image(image10)
    st.image(image12)

with col2:
    st.image(image3)
    st.image(image5)
    st.image(image7)
    st.image(image9)
    st.image(image11)
    st.image(image1)

