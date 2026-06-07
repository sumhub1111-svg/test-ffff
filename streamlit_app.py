import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="텍스트 키워드 분석기")
st.title("📝 텍스트 키워드 분석기")
st.markdown("자연어 처리(NLP) 기초: 리스트와 반복문, 조건문을 이용한 단어 빈도 분석")

# 1. 사용자로부터 텍스트 입력 받기
user_text = st.text_area("분석할 긴 글(뉴스 기사, 소설 등)을 입력하세요:", height=200)

if user_text:
    # 파이썬 내장 함수 split()으로 띄어쓰기 기준 리스트 생성
    words = user_text.split()
    
    # 데이터를 저장할 두 개의 빈 리스트 준비
    unique_words = []
    word_counts = []
    
    # 2. 반복문(for)을 이용한 데이터 탐색
    for word in words:
        # 특수기호 대략적 제거 (선택사항)
        word = word.replace(".", "").replace(",", "").replace("?", "").replace("!", "")
        
        # 3. 조건문(if): 2글자 이상인 단어만 취급 (1글자 조사 제외)
        if len(word) >= 2:
            # 만약 이미 고유 단어 리스트에 등록된 단어라면?
            if word in unique_words:
                # 그 단어의 위치(인덱스)를 찾아서
                index = unique_words.index(word)
                # 개수 리스트의 같은 위치 숫자를 1 증가 (조건문 로직)
                word_counts[index] += 1
            # 처음 보는 새로운 단어라면?
            else:
                # 리스트 맨 끝에 새로운 단어와 개수(1)를 각각 추가
                unique_words.append(word)
                word_counts.append(1)
                
    st.success("텍스트 분석이 완료되었습니다!")
    
    # 분석된 결과가 있을 때만 화면에 출력
    if len(unique_words) > 0:
        st.subheader("📊 가장 많이 나온 키워드 TOP 5")
        
        # 임시로 가장 많이 나온 단어 5개를 찾기 위한 간단한 로직
        # (원래는 정렬 알고리즘을 쓰지만, 심플하게 구현)
        for i in range(min(5, len(unique_words))):
            # 가장 큰 숫자의 위치를 찾음
            max_count = max(word_counts)
            max_index = word_counts.index(max_count)
            
            # 결과 출력
            st.write(f"**{i+1}위:** {unique_words[max_index]} ({max_count}회)")
            
            # 찾은 최댓값은 다음 순위 검색을 위해 -1로 없애버림
            word_counts[max_index] = -1
    else:
        st.warning("분석할 수 있는 2글자 이상의 단어가 없습니다.")