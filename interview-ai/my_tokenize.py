from kiwipiepy import Kiwi

# Kiwi 객체 생성
kiwi = Kiwi()

text = "선임이 지속적으로 갈궈서 잠을 못 자겠습니다."

# 형태소 분석 실행
tokens = kiwi.tokenize(text)

for token in tokens:
    # token.form: 형태소 원형, token.tag: 품사 태그, token.start: 시작 위치, token.len: 길이
    print(f"{token.form}\t[{token.tag}]")