# main.py
from kiwipiepy import Kiwi
from risk_scorer import RiskScorer

def run_pipeline(text: str):
    # 1. Kiwi 초기화 및 사용자 사전 추가
    kiwi = Kiwi()
    custom_words = [
        ("현부심", "NNG"), ("기수열외", "NNG"), ("퐁당근무", "NNG"),
        ("갈굼", "NNG"), ("가스라이팅", "NNG")
    ]
    for word, pos in custom_words:
        kiwi.add_user_word(word, pos)

    # 2. 띄어쓰기 보정
    spaced_text = kiwi.space(text)

    # 3. 형태소 분석
    tokens = kiwi.tokenize(spaced_text)

    # 4. 4대 위험 영역 스코어링 평가
    scorer = RiskScorer()
    risk_results = scorer.evaluate(text, spaced_text, tokens)

    # 5. 결과 리포트 출력 (점수 및 등급 제외)
    print("=" * 60)
    print(f"[원문 텍스트]: {text}")
    print(f"[보정 텍스트]: {spaced_text}")
    print("=" * 60)
    print("=== [Stage 1] Rule-based 4대 위험 영역 분석 리포트 ===")
    
    for category, result in risk_results.items():
        evidence_list = result["evidence"]
        has_risk = len(evidence_list) > 0
        evidence_str = ", ".join(evidence_list) if has_risk else "없음"
        
        status = "⚠️ 위험 요인 감지" if has_risk else "✅ 특이사항 없음"

        print(f"[{category}]")
        print(f"  - 상태: {status}")
        print(f"  - 검출 근거 키워드: {evidence_str}")
        print("-" * 40)

    return {
        "text": spaced_text,
        "risk_results": risk_results
    }


if __name__ == "__main__":
    # 실행 테스트
    sample = "선임이갈궈서밤에잠을못자겠고현부심신청하고싶습니다"
    run_pipeline(sample)