import streamlit as st 
import numpy as np
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# 기본 텍스트 출력
st.title("Hello Streamlit!")
st.header("헤더")
st.write("st.write() 기본 텍스트 출력")

# 사용자 입력 받기
name = st.text_input("이름을 입력하세요:")
print(f"안녕하세요, {name}님")
st.write(f"안녕하세요, {name}님")

# 숫자 입력 받기
age = st.number_input("나이를 입력하세요", 
min_value=0, max_value=120)
print(f"나이: {age}")
st.write(f"나이: {age}")

# 사이드바 메뉴
menus = ["A", "B", "C"]
options = st.sidebar.selectbox("메뉴 선택", menus)
print("선택한 메뉴:", options)
st.write("선택한 메뉴:", options)

# 버튼 클릭 이벤트
if st.button('버튼클릭'):
    st.success('버튼이 눌렸습니다')
    st.write('클릭 이후 코드를 실행하세요')
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print('num1 + num2 =', num1+num2)
    st.write(num1+num2)

#체크박스 옵션 제어
checked = st.checkbox('옵션 활성화')
print('checked:', checked)
if checked:
    st.write('옵션코드를 실행하세요!')


# 데이터 프레임 표시
tips = sns.load_dataset('tips')
print(tips)
st.dataframe(tips)


#matplotlib 그래프 출력
# 객체 지향으로 출력
fig, ax= plt.subplots()
ax.plot([1,2,3],[10,20,30])
st.pyplot(fig)


df= px.data.tips()

fig = px.scatter(
df,
 x='total_bill',
y='tip',
color='sex',
hover_data=['day','time','size'],
title='금액vs팁')

st.plotly_chart(fig)

#이미지, 동영상
imgUrl ='https://ichef.bbci.co.uk/ace/ws/800/cpsprodpb/c82c/live/d2c695c0-8408-11f0-84c8-99de564f0440.jpg'
st.image(imgUrl)

videourl='https://www.youtube.com/watch?v=dw7WtthpqhY&list=RDdw7WtthpqhY&start_radio=1'
st.video(videourl)

#progress bar
import time
#progress =st.progress(0)
#for i in range(100):
#    progress.progress(i+1)
#   time.sleep(0.01)

#with st.spinner('처리중...'):
#    time.sleep(2)
#st.success('완료')


#layout
col1, col2 = st.columns(2)
#col1.write('왼쪽컬럼')
#col2.write('오른쪽컬럼')

with col1:
	st.subheader('설정매뉴')
	min_val = st.number_input('최솟값', value =1)
	max_val = st.number_input('최댓값', value =1)

	count = st.slider('생성할 난수 갯수',1,10,5)
	st.write(count)

	run_btn = st.button('난수 생성 및 시각화')
	st.write(min_val, max_val, count, run_btn)


with col2:
	if run_btn:
		st.subheader('결과시각화')

		#난수생성
		numbers = [random.randint(min_val, max_val) for _ in range(count)]
		random_df = pd.DataFrame({"index": list(range(1, count+1)), "value": numbers})
		#st.dataframe(df)
		st.write('생성된 난수:', numbers)

		#시각화 코드
		fig = px.bar(df, x=df.index, y="total_bill", title="난수 Bar Chart", text="total_bill")
		fig.update_traces(textposition="outside")
		fig.update_layout(yaxis_range=[0, max(numbers) + 5])
		st.plotly_chart(fig, use_container_width=True)


#tabs 구성
tab1, tab2, tab3 = st.tabs(['탭1','탭2','탭3'])
with tab1:
	st.write('탭1 코드 실행')
with tab2:
	st.write('탭2 코드 실행')
with tab3:
	st.write('탭3 코드 실행')

#세션 증가
if 'count' not in st.session_state:
	st.session_state.count = 0
#st.write('현재 세션 카운트:', st.session_state.count)

if st.button('증가'):
	st.session_state.count += 1

st.write('현재 세션카운트:', st.session_state.count)

#날짜
date=st.date_input('날짜선택')
st.write('선택한 날짜:', date)

#expander UI(자세히보기)

with st.expander('자세히보기'):
	st.write('이 영역은 클릭 시 잘 펼쳐집니다.')


#색상선택으로 배경색 바꾸기
#st.markdown(), HTML CSS코드 작성
bg_color = st.color_picker('배경색선택', "#FFFFFF")
st.write('색상선택:', bg_color)
st.markdown(f"""
    <div style="padding:20px; background-color:{bg_color};">
        선택된 배경색: {bg_color}
    </div>
""", unsafe_allow_html=True)


# 사용자 선택으로 plotly 그래프 색상 변경
graph_color = st.color_picker('그래프 색상 선택:','#FFFFFF')
temp_df = pd.DataFrame({'s':[1,2,3], 'y':[10,20,30]})
print(temp_df)

fig = px.bar(temp_df, x='s', y='y', color_discrete_sequence=[graph_color])
st.plotly_chart(fig, use_container_width=True)









