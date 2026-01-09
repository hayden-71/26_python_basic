import streamlit as st
import pandas as pd
import requests

# 1. 페이지 기본 설정
st.set_page_config(page_title="포켓몬 데이터 센터", page_icon="⚡")
st.title("⚡ 포켓몬 능력치 분석기")
st.write("포켓몬의 영문 이름을 입력하면 상세 스탯을 분석해줍니다.")

# 2. 사용자 입력 (포켓몬 이름)
# 기본값으로 'pikachu'를 넣어줍니다.
poke_name = st.sidebar.text_input("포켓몬 영문 이름 입력", value="pikachu").lower()


# 3. PokeAPI 데이터 가져오기 함수
def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


# 4. 버튼 클릭 시 분석 시작
if st.button("데이터 조회"):
    data = get_pokemon_data(poke_name)

    if data:
        # --- [A] 기본 정보 파싱 (JSON 처리) ---
        img_url = data["sprites"]["front_default"]  # 이미지 URL
        height = data["height"] / 10  # 단위 변환
        weight = data["weight"] / 10
        types = [t["type"]["name"] for t in data["types"]]  # 리스트 컴프리헨션

        # --- [B] 화면 구성 (컬럼 나누기) ---
        col1, col2 = st.columns(2)
        with col1:
            st.image(img_url, width=200)
        with col2:
            st.subheader(f"이름: {poke_name.upper()}")
            st.write(f"**키:** {height} m")
            st.write(f"**몸무게:** {weight} kg")
            st.write(f"**속성:** {', '.join(types)}")

        # --- [C] 능력치 데이터 Pandas 변환 (핵심!) ---
        # API의 복잡한 stats 구조를 깔끔한 DataFrame으로 만듭니다.
        stats_list = []
        for s in data["stats"]:
            stats_list.append(
                {
                    "능력": s["stat"]["name"].upper(),  # HP, ATTACK 등
                    "수치": s["base_stat"],
                }
            )

        df_stats = pd.DataFrame(stats_list)

        # --- [D] 분석 결과 시각화 ---
        st.subheader("📊 능력치 상세 분석")

        # 1. 데이터 표 보여주기
        with st.expander("데이터 표로 보기"):
            st.dataframe(df_stats)

        # 2. 막대 그래프 그리기 (Streamlit 내장 함수)
        # 수강생들에게 "숫자로 보는 것보다 그래프가 낫죠?" 강조
        st.bar_chart(df_stats.set_index("능력"))

        # --- [E] (심화) 전설의 포켓몬 'Mewtwo'와 비교하기 ---
        st.markdown("---")
        st.subheader("🆚 'Mewtwo'와의 비교")

        mewtwo_data = get_pokemon_data("mewtwo")
        mewtwo_stats = [s["base_stat"] for s in mewtwo_data["stats"]]

        # 내 포켓몬 스탯에 뮤츠 스탯 컬럼 추가
        df_stats["Mewtwo"] = mewtwo_stats

        # 비교 차트 그리기
        st.line_chart(df_stats.set_index("능력")[["수치", "Mewtwo"]])

    else:
        st.error(
            "포켓몬을 찾을 수 없습니다! 오타를 확인해주세요. (예: charizard, squirtle)"
        )
