import streamlit as st #모듈 빌려오기


#질문 디렉토리 생성
questions = {
    "**\U0001F31F1) 평소 본인이 감성적이라고 생각하시나요?**": {"매우 그러함": 7, "조금 그러함": 6, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F2) 계획을 하고 행동하는 편인가요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F3) 과학적 원리를 이해하는 것이 재미있나요?**": {"매우 그러함": 1, "조금 그러함": 2, "보통임": 3, "조금 아님": 6, "매우 아님": 7},
    "**\U0001F31F4) 방 정리하는 것을 즐기는 편인가요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F5) 답이 여러개인 문제를 한개인 문제보다 선호하시나요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F6) 갑자기 생긴 약속을 즐기는 편인가요?**": {"매우 그러함": 1, "조금 그러함": 2, "보통임": 3, "조금 아님": 4, "매우 아님": 5},
    "**\U0001F31F7) 비문학보다 소설을 읽는 것을 더 좋아하시나요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F8) 다이어리를 꾸준히 쓰는 편인가요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F9) 정의가 다음 중 무엇이라고 생각하시나요?**": {"justice": 4, "definition": 2},
    "**\U0001F31F10) 평소 창의적이라는 말을 자주 듣나요?**": {"매우 그러함": 1, "조금 그러함": 2, "보통임": 3, "조금 아님": 4, "매우 아님": 5},
    "**\U0001F31F11) 본인이 논리적이라고 생각하시나요?**": {"매우 그러함": 1, "조금 그러함": 2, "보통임": 3, "조금 아님": 4, "매우 아님": 5},
    "**\U0001F31F12) 일이 계획대로 되지 않으면 큰 불안감을 느끼나요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F13) 평소 수학 문제 푸는 것을 즐기시나요?**": {"매우 그러함": 1, "조금 그러함": 2, "보통임": 3, "조금 아님": 6, "매우 아님": 7},
    "**\U0001F31F14) 공부할 때 본인이 좋아하는 부분부터 하는 경향이 있나요?**": {"매우 그러함": 1, "조금 그러함": 2, "보통임": 3, "조금 아님": 4, "매우 아님": 5},
    "**\U0001F31F15) 5!이 다음 중 무엇이라고 생각하시나요?**": {"오!": 4,"5팩토리얼": 2},
    "**\U0001F31F16) 미래를 통제하고 싶어하나요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F17) 통합사회와 통합과학 중 어떤 과목에 더 자신이 있나요?**": {"통합사회": 5, "통합과학": 1, "둘 다 자신 있음": 3, "둘 다 자신 없음": 3},
    "**\U0001F31F18) 사물함 정리가 잘 되어있는 편인가요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1},
    "**\U0001F31F19) 이육사가 다음 중 무엇이라고 생각하시나요?**": {"시인": 4, "264": 2},
    "**\U0001F31F20) 항상 일정한 시간에 일어나고 잠드는 편인가요?**": {"매우 그러함": 5, "조금 그러함": 4, "보통임": 3, "조금 아님": 2, "매우 아님": 1}
}


#UI꾸미기^^
st.set_page_config(
    page_title="WBTI 테스트",
    page_icon="\U0001F680",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


#제목 생성
st.write("## 당신의 WBTI는 무엇일까요?\U0001F60B")


st.text("")
st.text("")


#질문, 그에 따른 점수 받는 함수 정의
def get_user_answer(question):
    answer = st.radio(question, list(questions[question].keys()))
    score = questions[question][answer]
    return answer, score


#따로 따로(문과/이과, 계획형/즉흥형) 받는 함수
def get_pattern_scores(pattern):
    final_score1 = 0
    final_score2 = 0
    for i, (question_key, answer_dict) in enumerate(questions.items()): #디렉토리의 질문과 응답을 나누어 받음
        if i % 2 == pattern:
            answer, question_score = get_user_answer(question_key)
            final_score1 += question_score
        else:
            answer, question_score = get_user_answer(question_key)
            final_score2 += question_score
    return final_score1, final_score2


#최종 점수(1은 문과/이과, 2는 계획형/즉흥형)
final_score1, final_score2 = get_pattern_scores(0)


#유형별 결과
a1 = "##### \U0001F4D6 당신은 문과(Liberal arts)입니다."
a11 = "국어와 사회에서 돋보이는 재능과 풍부한 문학적 감수성을 지닌 당신은 문과 학생이네요! 언어와 역사에 대한 흥미와 이해력 그리고  문학 작품에 대한 해석과 비평 능력이 뛰어나요. 과학보다는 사회 탐구 과목을 선택하는 것을 추천해요. 학습 전략으로는 독서와 토론, 논쟁에 참여하여 사고력을 향상시키는 것이 좋아요. 다양한 문학 작품을 즐기며 토론에 참여하면서 자신만의 시각을 형성하는 것이 성공적인 고등학교 생활에 도움이 될 거예요. 당신의 많은 발전을 기대합니다~"
a2 = "##### \U0001F4CA 당신은 이과(Natural sciences)입니다."
a22 = "수학과 과학 분야에서 뛰어난 재능을 지니며, 논리적인 사고를 하는 당신은 이과 학생이네요! 특히 수학과 과학에 대한 흥미와 이해가 높아, 문제 해결과 실험적인 활동 즐기는 편이네요. 사회 탐구 과목보다는 과학탐구 과목을 선택하는 것이 유리할 것 같네요. 이과 학생들에게 추천하는 공부 방법은 문제 해결 중심의 학습과 실험 통한 경험을 쌓는 것이에요. 수학과 과학 문제를 해결하는 데에 적극적으로 참여하고, 이론을 실제 상황에 적용하는 능력을 키우기 위해 노력한다면 고등학교 생활에 도움이 될 거예요. 당신의 많은 발전을 기대합니다~"


b1 = "##### \U0001F4DD 당신은 계획형(Judging)입니다."
b11 = "평소 계획을 세우고 그에 따라 움직이는 것을 즐기는 당신은 계획형 학생이네요! 당신은 계획이 어긋나는 상황에서는 쉽게 좌절하는 경향을 지니고 있네요. 추천하는 공부 방법은 목표를 세우고 계획을 세우되, 지나치게 엄격하지 않도록 하는 것입니다. 자신과의 약속을 중요시하지만, 약속을 지키지 못했을 때에 너무 자신을 탓하지 않도록 해요. 모든 사람은 실수를 하고, 그로부터 배우는 것이 중요하니까요!"
b2 = "##### \U0001F4D6 당신은 즉흥형(Perceiving)입니다."
b22 = " 일상적인 일들을 보다 유연하게 다루며, 즉흥적으로 상황을 해결하는 데에 탁월한 능력을 지닌 당신은 즉흥형 학생이네요! 그러나 당신은 종종 과제나 시험 전에 갑자기 벼락치기를 하거나 기간 안에 일을 처리하지 못하는 등의 문제들을 겪을 수 있어요. 추천하는 공부 방법은 즉흥성을 유지하면서도 중요한 일들에는 계획적으로 행동하는 것입니다. 중요한 마감일과 시험 날짜를 미리 기록하고, 계획을 세워 일정을 따라가도록 노력해보세요! 유연성과 계획성을 적절히 조화시키면 더욱 효율적으로 고등학교 생활을 할 수 있을 거예요!"

image_LJ = "https://raw.githubusercontent.com/heeonme/streamlit1/main/LJ.jpg"
image_LP = "https://raw.githubusercontent.com/heeonme/streamlit1/main/LP.jpg"
image_NJ = "https://raw.githubusercontent.com/heeonme/streamlit1/main/NJ.jpg"
image_NP = "https://raw.githubusercontent.com/heeonme/streamlit1/main/NP.jpg"


st.text("")
st.text("")
st.text("")

#결과 확인
st.markdown("<div style='text-align: center;'>당신의 WBTI는 무엇일까요?\U0001F308\u2728</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>당신의 유형을 확인해봅시다!</div>", unsafe_allow_html=True)


st.text("")


if st.button("결과 확인하기"):


    st.text("")


    if final_score1 > 32: #점수에 따라서 유형 나누기
        result = 'L'
    else:
        result = 'N'
    st.text("")
    st.text("")

    if final_score2 > 30:
        result += 'J'
    else:
        result += 'P'

    st.title('\U0001F389 당신은 ' + result + '유형입니다 \U0001F389')  # 유형 보여주기
    if result == 'LJ':
        st.image(image_LJ, use_column_width=True)
    elif result == 'LP':
        st.image(image_LP, use_column_width=True)
    elif result == 'NJ':
        st.image(image_NJ, use_column_width=True)
    else:
        st.image(image_NP, use_column_width=True)

    st.text("")
    st.text("")
    st.text("")

    if final_score1 > 32:
        st.success(a1)  # 문과
        st.success(a11)
    else:
        st.success(a2)  # 이과
        st.success(a22)

    st.text("")
    st.text("")

    if final_score2 > 30:
        st.success(b1)  # 계획형
        st.success(b11)
    else:
        st.success(b2)  # 즉흥형
        st.success(b22)



#꾸미기^^
st.markdown(
    """
    <style>
        div.stButton > button {
            display: block;
            margin: 0 auto;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        div.stMarkdown {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        .result-box {
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
            margin-top: 20px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)