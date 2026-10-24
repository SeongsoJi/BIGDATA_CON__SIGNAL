# main.py
from kiwipiepy import Kiwi
from risk_detection import RiskScorer

def run_pipeline(text: str):
    # 1. Kiwi 초기화 및 단어 추가
    kiwi = Kiwi()
    custom_words = [
        ("현부심", "NNG"), ("신체화", "NNG"), ("성희롱", "NNG"),
        ("따돌림", "NNG"), ("비인격적", "NNG"), ("임무스트레스", "NNG"),
        ("기수열외", "NNG"), ("가스라이팅", "NNG"), ("갈굼", "NNG")
    ]
    for word, pos in custom_words:
        kiwi.add_user_word(word, pos)

    # 2. 띄어쓰기 보정 및 토큰화
    spaced_text = kiwi.space(text)
    tokens = kiwi.tokenize(spaced_text)

    # 3. 4대 위험 영역 식별
    scorer = RiskScorer()
    risk_results = scorer.evaluate(text, spaced_text, tokens)

    # 4. 출력 리포트
    print("\n" + "=" * 60)
    print("=== [Stage 1] 4대 위험 영역 분석 리포트 ===")
    print("=" * 60)
    
    for category, result in risk_results.items():
        evidence_list = result.get("evidence", [])
        is_detected = result.get("detected", False)
        
        evidence_str = ", ".join(evidence_list) if is_detected else "없음"
        status = "⚠️ 위험 요인 감지" if is_detected else "✅ 특이사항 없음"

        print(f"[{category}]")
        print(f"  - 상태: {status}")
        print(f"  - 검출 근거 키워드: {evidence_str}")
        print("-" * 40)

    return risk_results


def get_multiline_input():
    print("=" * 60)
    print("분석할 면담기록을 입력하세요.")
    print("(입력을 모두 마친 후 빈 줄에서 'ENTER'를 한번 더 눌러주세요)")
    print("=" * 60)
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                if lines:
                    break
                else:
                    continue
            lines.append(line)
        except (EOFError, KeyboardInterrupt):
            break
            
    return "\n".join(lines)


if __name__ == "__main__":
    user_interview_text = get_multiline_input()
    if user_interview_text.strip():
        run_pipeline(user_interview_text)
    else:
        print("입력된 내용이 없습니다.")