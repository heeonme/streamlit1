#모듈 빌려오기
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf



data = pd.read_csv(r'/Downloads/reponse1.csv')

y1 = data['이과 1 문과 0'].values
x1 = []

for i, rows in data.iterrows():
    x1.append([ rows["매우 그러함 5, 조금그러함 4, 보통임3, 조금 아님2, 매우 아님1"], rows['과학적 원리를 이해하는 것이 재미있나요?'], rows['답이 여러개인 문제를 한개인 문제보다 선호하시나요?'], rows['비문학보다 소설을 읽는 것을 더 좋아하시나요?'], rows['definition 1 justice 0'], rows['본인이 논리적이라고 생각하시나요?'], rows['평소 수학 문제 푸는 것을 즐기시나요?'], rows['5팩토리얼 1, 오! 0'], rows['둘다 잇음4, 통과3, 통사2, 둘다 업음1'], rows['264 1, 시인0']])

import tensorflow as tf

model1 = tf.keras.models.Sequential([
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(32, activation = 'relu'),
        tf.keras.layers.Dense(1, activation = 'sigmoid'),
    ])

model1.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model1.fit(np.array(x1), np.array(y1), epochs=1000)


y2 = data['J 1, P 0'].values
x2 = []

for i, rows in data.iterrows():
    x2.append([ rows["계획을 하고 행동하는 편인가요?"], rows['방 정리하는 것을 즐기는 편인가요?'], rows['갑자기 생긴 약속을 즐기는 편인가요?'], rows['다이어리를 꾸준히 쓰는 편인가요?'], rows['평소 창의적이라는 말을 자주 듣나요?'], rows['일이 계획대로 되지 않으면 큰 불안감을 느끼나요?'], rows['공부할 때 본인이 좋아하는 부분부터 하는 경향이 있나요?'], rows['미래를 통제하고 싶어하나요?'], rows['사물함 정리가 잘 되어있는 편인가요?'], rows['항상 일정한 시간에 일어나고 잠드는 편인가요?']])

model2 = tf.keras.models.Sequential([
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(8, activation = 'relu'),
        tf.keras.layers.Dense(1, activation = 'sigmoid'),
    ])

model2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model2.fit(np.array(x2), np.array(y2), epochs=1000)




#UI 꾸미기
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



#유형별 결과
a1 = "##### \U0001F4D6 당신은 문과(Liberal arts)입니다."
a11 = "국어와 사회에서 돋보이는 재능과 풍부한 문학적 감수성을 지닌 당신은 문과 학생이네요! 언어와 역사에 대한 흥미와 이해력 그리고 문학 작품에 대한 해석과 비평 능력이 뛰어나요. 국어 과목에 뛰어난 재능을 보이고 사회문화, 생활과 윤리, 정치와 법, 동아시아사, 세계지리, 한국사, 경제와 같은 과목들을 선택과목으로 정하는 것이 유리한 학생이네요."

a1_1 = '언어에 대해 뛰어난 이해력을 지니고 있네요. 다만 논리적 사고를 요구하는 문법에 대한 내용을 공부하는 데에 어려움을 겪을 수 있어요. 문법적 개념들은 효과적인 의사소통과 글쓰기의 핵심이 되며, 이를 통해 더 정확하고 명료한 표현이 가능해집니다. 문장 구조와 논리적 흐름을 주의 깊게 살펴보고, 그에 따른 문법 구조를 이해할 수 있도록 노력한다면 언어 능력이 훨씬 향상될 것 같아요.'
a1_2 = '문과인 당신은 수학에 대한 이해가 조금 부족할 수도 있어요. 그래서 다양한 수학 분야의 문제를 가능한 한 많이 풀어보는 것을 추천해요!  다양한 수학 분야의 문제에 도전하며 논리적인 접근법을 익히고, 개념을 명확히 이해할 수 있도록 노력해보세요. 여러 문제를 접하는 것은 수학적 사고 능력을 키우고 성적 올리는 데 도움이 될 거예요.'
a1_3 = '언어 능력이 뛰어난 당신은 영어 단어와 문법 구조를 정확하게 파악하고 있다면 영어를 공부하는 데에는 큰 어려움이 없을 거예요. 영어 단어를 외우고 문장을 직접 적어보며 어휘력과 구조에 대한 지식을 늘리는 걸 추천해요!'
a1_4 = '역사, 정치, 법, 경제, 철학과 같은 주제에 큰 흥미를 가지고 있고 재미를 느끼는 당신은 사회탐구 과목을 공부하는 데에 큰 어려움을 겪을 것 같진 않네요.'
a1_5 = '문과인 당신은 과학적 원리를 이해하고 문제를 해결하는 데 어려움을 겪을 수 있을 것 같아요. 선택과목을 선택할 때에는 생명과학이나 지구과학과 같이 문제 해결 능력을 적게 필요로하는 과목을 택하는 것을 추천해요. 만약 물리학이나 화학에 대해서 공부하게 된다면 원리와 개념을 정확하게 이해하고 다양한 문제들을 접하며 문제해결 능력을 키우는 것을 추천해요!'

a2 = "##### \U0001F4CA 당신은 이과(Natural sciences)입니다."
a22 = "수학과 과학 분야에서 뛰어난 재능을 지니며, 논리적인 사고를 하는 당신은 이과 학생이네요! 특히 수학과 과학에 대한 흥미와 이해가 높아, 문제 해결과 실험적인 활동 즐기는 편이네요. 수학 과목에 뛰어난 재능을 보이고 물리학, 화학, 생명과학, 지구과학, 기하, 미적분과 같은 과목을 선택과목으로 정하는 것이 유리하겠네요."

a2_1 = '이과인 당신은 언어에 대한 조금 부족한 경향이 있을 수도 있겠네요. 다만 논리적 사고를 요구하는 문법이나 독서 분야에서는 뛰어난 문제해결 능력을 보여줄 것 같아요. 문학적 용어들을 정확하게 이해하고 이에 맞춰서 많은 문제를 풀어보는 것을 추천해요! 문학적 개념들을 이해할 수 있도록 노력한다면 언어 능력이 훨씬 향상될 것 같아요.'
a2_2 = '수학적 문제해결에 뛰어난 능력을 지니고 있네요. 다만 ‘경우의 수’처럼 언어적 능력을 필요로하는 문제에서 어려움을 겪을 수 있어요. 이런 문제를 겪을 때에는 수학적 능력을 의심하기 보다는 언어적 능력을 키우기 위해서 노력해야할 것 같아요. 또 어려운 문제보다 쉬운 문제에서 더 높은 오답률을 보인다면 쉬운 문제를 지속적으로 풀어보며 실수를 줄이는 것도 수학 성적을 향상시키는 데 좋은 방법이 될 것 같아요.'
a2_3 = '논리적 사고 능력이 뛰어난 당신은 영어의 단어를 정확하게 파악하고 있다면 영어를 공부하는 데에는 큰 어려움이 없을 거예요. 영어 성적을 향상시키는 데 가장 중요한 능력 중 하나가 어휘력이기 때문에 어휘력을 늘리는 데 많을 시간을 투자하는 것을 추천해요!'
a2_4 = '역사, 정치, 법, 경제, 철학과 같은 주제에 큰 흥미를 가지고 있지 않은 당신은 공부하는 데에 약간의 어려움을 겪을 수 있을 같아요. 역사, 문화, 지리와 같은 분야를 공부할 때에는 여러 요인들 간의 인과 관계를 중심으로 이해하는 것을 추천해요. 그리고 법, 철학과 같은 분야를 공부할 때에는 간단한 인포그래픽으로 본인의 생각을 시각화하며 암기하는 것을 추천해요. 암기하는 데 어려움을 겪겠지만 사회탐구 과목에서의 암기는 불가피한 것입니다.'
a2_5 = '이과인 당신은 과학적 원리 이해하고 문제를 해결하는 데 큰 어려움을 겪을 것 같진 않네요. 선택과목을 선택할 때 과학탐구 과목 위조로 선택하는 것을 추천해요! 당신을 잘 해낼 수 있을 것이라 믿습니다.'

b1 = "##### \U0001F4DD 당신은 계획형(Judging)입니다."
b11 = "평소 계획을 세우고 그에 따라 움직이는 것을 즐기는 당신은 계획형 학생이네요! 계획이 틀어지면 지나친 불안감을 느끼는 경향이 있고, 항상 모든 일에 다방면을 계획을 세우고 실천하는 특징을 지니고 있네요."
b111 = "당신은 계획이 어긋나는 상황에서는 쉽게 좌절하고 불안해하는 경향을 지니고 있네요. 구체적인 공부 방법과 목표를 세우고 지키는 것은 매우 바람직하지만, 스스로에게 지나치게 엄격해지지 않도록 하는 게 중요할 것 같아요. 자신과의 약속도 중요하지만, 약속을 지키지 못했을 때에 너무 자신을 탓하지 않도록 해요! 모든 사람은 실수를 하고, 그로부터 배우는 것이 중요하니까요~"
b2 = "##### \U0001F4D6 당신은 즉흥형(Perceiving)입니다."
b22 = " 일상적인 일들을 보다 유연하게 다루며, 즉흥적으로 상황을 해결하는 데에 탁월한 능력을 지닌 당신은 즉흥형 학생이네요! 계획을 사전에 세우지 않고 즉흥적으로 일을 처리하는 특징을 지니고 있네요."
b222 = "종종 시험 전에 갑자기 벼락치기를 하거나 기간 안에 과제들을 제출하지 못하는 등의 문제들을 겪어본 경험이 있지 않나요? 즉흥성을 유지하며 유연하게 행동하는 것도 효과적인 공부를 돕는 하나의 방법이 될 수 있지만 중요한 일들에는 계획적으로 행동하는 것도 필요할 것 같아요. 중요한 일정의 마감일과 시험 날짜를 미리 기록하고, 계획을 세워 일정을 따라가도록 노력해보세요! 유연성과 계획성을 적절히 조화시키면 더욱 효율적으로 고등학교 생활을 할 수 있을 거예요!"

image_LJ = "https://raw.githubusercontent.com/heeonme/streamlit1/main/LJ.jpg"
image_LP = "https://raw.githubusercontent.com/heeonme/streamlit1/main/LP.jpg"
image_NJ = "https://raw.githubusercontent.com/heeonme/streamlit1/main/NJ.jpg"
image_NP = "https://raw.githubusercontent.com/heeonme/streamlit1/main/NP.jpg"



def get_user_answer(question_key, answer_dict):
    options = list(answer_dict.keys())
    answer = st.radio(question_key, options, index=None)
    return answer, question_key

def get_pattern_scores(pattern):
    final_score1 = []
    final_score2 = []
    user_responses = []

    for i, (question_key, answer_dict) in enumerate(questions.items()):
        if i % 2 == pattern:
            answer, question_key = get_user_answer(question_key, answer_dict)
            if answer in answer_dict:
                question_score = answer_dict[answer]
                final_score1.append(question_score)
                user_responses.append(question_key)
        else:
            answer, question_key = get_user_answer(question_key, answer_dict)
            if answer in answer_dict:
                question_score = answer_dict[answer]
                final_score2.append(question_score)
                user_responses.append(question_key)

    return final_score1, final_score2, user_responses



#제목 생성
st.write("## 당신의 WBTI는 무엇일까요?\U0001F60B")


st.text("")
st.text("")


#최종 점수(1은 문과/이과, 2는 계획형/즉흥형)
final_score1, final_score2, user_responses = get_pattern_scores(0)


st.text("")
st.text("")
st.text("")


if st.button("결과 확인하기"):

    all_questions_answered = all(question_key in user_responses for question_key in questions)

    if all_questions_answered == False:
        st.markdown("<div style='text-align: center;'>Error: 모든 질문에 답변해주세요.</div>", unsafe_allow_html=True)

    else:

        st.text("")
        st.text("")
        st.text("")

        with st.expander('**WBTI 결과**'):

            tab1, tab2 = st.tabs(["유형", "공부전략"])

            with tab1:
                model1.predict(final_score1)
                final_score1 = final_score1[0]
                if  round(final_score1, 1) != 1: #점수에 따라서 유형 나누기
                    result = 'L'
                else:
                    result = 'N'

                model2.predict(final_score2)
                final_score2 = final_score2[0]
                if round(final_score2, 1) == 1:  # 점수에 따라서 유형 나누기
                    result += 'J'
                else:
                    result += 'P'

                st.text("")
                st.text("")

                st.title('\U0001F389 당신은 ' + result + '유형입니다 \U0001F389')  #유형 보여주기
                if result == 'LJ':
                    st.image(image_LJ, use_column_width=True)
                elif result == 'LP':
                    st.image(image_LP, use_column_width=True)
                elif result == 'NJ':
                    st.image(image_NJ, use_column_width=True)
                else:
                    st.image(image_NP, use_column_width=True)

                if round(final_score1, 1) != 1:
                    st.success(a1)  # 문과
                    st.success(a11)
                else:
                    st.success(a2)  # 이과
                    st.success(a22)

                st.text("")
                st.text("")
                st.text("")

                if round(final_score2, 1) == 1:
                    st.success(b1)  # 계획형
                    st.success(b11)
                else:
                    st.success(b2)  # 즉흥형
                    st.success(b22)

            with tab2:

                st.text("")
                st.text("")
                st.text("")

                st.title('\U0001F389 당신을 위한 공부전략입니다 \U0001F389')

                st.text("")
                st.text("")
                st.text("")
                st.text("")
                st.text("")

                st.success("### \U0001F4D6 과목별 공부전략")
                if round(final_score1, 1) != 1:
                    st.success("##### \u2606 국어")
                    st.success(a1_1)
                    st.text("")
                    st.success("##### \u2606 수학")
                    st.success(a1_2)
                    st.text("")
                    st.success("##### \u2606 영어")
                    st.success(a1_3)
                    st.text("")
                    st.success("##### \u2606 사회탐구")
                    st.success(a1_4)
                    st.text("")
                    st.success("##### \u2606 과학탐구")
                    st.success(a1_5)

                else:
                    st.success("##### \u2606 국어")
                    st.success(a2_1)
                    st.text("")
                    st.success("##### \u2606 수학")
                    st.success(a2_2)
                    st.text("")
                    st.success("##### \u2606 영어")
                    st.success(a2_3)
                    st.text("")
                    st.success("##### \u2606 사회탐구")
                    st.success(a2_4)
                    st.text("")
                    st.success("##### \u2606 과학탐구")
                    st.success(a2_5)

                st.text("")
                st.text("")
                st.text("")
                st.text("")

                st.success("### \U0001F4D6 효율적인 공부를 위한 조언")

                if round(final_score2, 1) == 1:
                    st.success(b111)
                else:
                    st.success(b222)