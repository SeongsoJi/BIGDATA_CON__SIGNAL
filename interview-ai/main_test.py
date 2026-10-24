# main_test.py
import re
import unicodedata
from kiwipiepy import Kiwi

class DirectRiskScorer:
    def __init__(self):
        # 4대 영역 탐색 단어 DB
        self.keywords = {
            "자살_자해위험": [
                "자살", "자해", "극단적", "유서", "신변", "죽고", "죽을", "죽었으면", "죽음",
                "상처", "끝내", "버티기", "버티는"
            ],
            "정신건강": [
                "불안", "우울", "절망", "무력", "스트레스", "답답", "숨막힘", "두통", "어지러",
                "분노", "화가", "공격", "충동", "환청", "환각", "망상", "의심",
                "불면", "수면", "잠", "트라우마", "외상", "자기비하", "무능", "쓸모", "자책"
            ],
            "대인관계": [
                "따돌림", "왕따", "은따", "기수열외", "고립",
                "비인격", "폭행", "폭언", "갈굼", "갈구", "가스라이팅", "괴롭",
                "시비", "놀리", "욕설", "마찰", "갈등", "성희롱", "성적", "부당"
            ],
            "복무적응": [
                "임무", "일과", "훈련", "업무", "총기", "폭발물", "공포",
                "가족", "집안", "경제", "빚", "돈",
                "이성", "애인", "실연", "현부심", "현역복무부적합", "전출", "보직"
            ]
        }

    def evaluate(self, full_text: str) -> dict:
        assessment = {}

        for category, kw_list in self.keywords.items():
            found_evidence = set()
            for kw in kw_list:
                if kw in full_text:
                    found_evidence.add(kw)

            evidence_list = sorted(list(found_evidence))
            assessment[category] = {
                "detected": len(evidence_list) > 0,
                "evidence": evidence_list
            }

        return assessment


def run_test():
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
            
    raw_input_text = "\n".join(lines)

    if not raw_input_text.strip():
        print("입력된 내용이 없습니다.")
        return

    # 1. 특수 공백(NBSP \xa0 등) 및 유니코드 문자 정규화 (핵심 원인 제거)
    cleaned_text = unicodedata.normalize('NFKC', raw_input_text)
    cleaned_text = cleaned_text.replace('\xa0', ' ')

    # 2. Kiwi 전처리
    kiwi = Kiwi()
    spaced_text = kiwi.space(cleaned_text)
    tokens = kiwi.tokenize(spaced_text)
    token_str = " ".join([t.form for t in tokens])

    # 3. 전체 텍스트 병합
    full_target_text = f"{cleaned_text} {spaced_text} {token_str}"

    # 4. 위험성 분석
    scorer = DirectRiskScorer()
    results = scorer.evaluate(full_target_text)

    # 5. 출력 리포트
    print("\n" + "=" * 60)
    print("=== [통합 검증] 4대 위험 영역 분석 리포트 ===")
    print("=" * 60)
    
    for category, result in results.items():
        is_detected = result["detected"]
        evidence_str = ", ".join(result["evidence"]) if is_detected else "없음"
        status = "⚠️ 위험 요인 감지" if is_detected else "✅ 특이사항 없음"

        print(f"[{category}]")
        print(f"  - 상태: {status}")
        print(f"  - 검출 근거 키워드: {evidence_str}")
        print("-" * 40)

if __name__ == "__main__":
    run_test()