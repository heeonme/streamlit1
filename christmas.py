import streamlit as st

class SessionState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = ""
        self.is_croffle = False
        self.selected_menus1_1 = {}
        self.is_drink1 = False
        self.is_drink2 = False
        self.total_cost = 0

def calculate_total_cost(selected_menus1_1, is_croffle, is_drink1, is_drink2):
    menu_prices = {"시럽": 10, "스프링클": 10, "휘핑크림": 10, "아이스크림": 10, "마시멜로우": 10, "블루베리": 10,
                   "크로플": 20, "음료수1": 15, "음료수2": 18}

    total_cost = 0

    if is_croffle:
        total_cost += sum(menu_prices[menu] for menu, is_selected in selected_menus1_1.items() if is_selected)

    if is_drink1:
        total_cost += menu_prices["음료수1"]

    if is_drink2:
        total_cost += menu_prices["음료수2"]

    return total_cost

def main():
    session_state = SessionState()

    st.title("키오스크 메뉴")

    if not session_state.name:
        # 이름 입력
        session_state.name = st.text_input("이름을 입력하세요:", key="name_input")

    if session_state.name:
        # "결정" 버튼을 누르면 초기화하고 페이지를 리다이렉트
        if st.button("결정"):
            session_state.reset()
            st.markdown(
                f'<meta http-equiv="refresh" content="0;URL=\'https://share.streamlit.io/{heeonme}/{christmas}\'" />',
                unsafe_allow_html=True
            )
        else:
            st.text("크로플")
            # "크로플" 체크 박스
            session_state.is_croffle = st.checkbox("크로플")

            # "크로플" 체크 박스가 선택된 경우에만 메뉴를 보여줌
            if session_state.is_croffle:
                # 메뉴 다중 선택
                with st.expander("크로플 토핑"):
                    menu_options1_1 = ["시럽", "스프링클", "휘핑크림", "아이스크림", "마시멜로우", "블루베리"]
                    # "시럽"과 "스프링클"을 True로 설정
                    session_state.selected_menus1_1 = {menu: st.checkbox(f"{menu}", value=menu in ["시럽", "스프링클"], key=f"{menu}_1_1") for menu in menu_options1_1}

            st.text("음료수")

            session_state.is_drink1 = st.checkbox("음료수1")
            session_state.is_drink2 = st.checkbox("음료수2")

            # 총 금액 계산 및 결과 표시
            total_cost = calculate_total_cost(session_state.selected_menus1_1, session_state.is_croffle, session_state.is_drink1, session_state.is_drink2)
            st.text(f"총 금액: {total_cost} 원")

if __name__ == "__main__":
    main()
