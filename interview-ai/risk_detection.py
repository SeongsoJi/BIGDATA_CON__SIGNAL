# risk_scorer.py

class RiskScorer:
    def __init__(self):
        # 4대 영역별 핵심 탐색 단어 DB (어근 및 주요 단어 패턴)
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

    def evaluate(self, raw_text: str, spaced_text: str, tokens: list) -> dict:
        assessment = {}

        # 1. Kiwi 토큰화 형태소 원형 수집
        token_forms = [t.form for t in tokens]
        token_str = " ".join(token_forms)

        # 2. 검색 대상 전체 텍스트 병합 (원문 + 보정문 + 토큰원형문)
        full_target_text = f"{raw_text} {spaced_text} {token_str}"

        for category, kw_list in self.keywords.items():
            found_evidence = set()

            for kw in kw_list:
                if kw in full_target_text:
                    found_evidence.add(kw)

            evidence_list = sorted(list(found_evidence))
            
            assessment[category] = {
                "detected": len(evidence_list) > 0,
                "evidence": evidence_list
            }

        return assessment