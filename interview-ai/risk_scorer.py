# risk_scorer.py
import re

class RiskScorer:
    def __init__(self):
        # 4대 위험 영역별 감지 패턴 및 기본 가중치 정의
        self.rules = {
            "자살_자해위험": {
                "patterns": [
                    r"(죽|자살|자해|극단적\s*선택|유서|신변\s*정리)",
                    r"(세상|삶|인생)\s*(을|를)?\s*(등지도|끝내|하직)",
                    r"(더\s*이상)\s*(버티|견디)\s*기\s*힘들"
                ],
                "weight": 40  # 직속 위험 키워드는 높은 점수 부여
            },
            "정신건강": {
                "patterns": [
                    r"(우울|불안|환청|환각|조울|공황|스트레스)",
                    r"(잠|수면)\s*(을|를)?\s*(못\s*자|설치|이루지\s*못)",
                    r"(두통|무력감|의욕\s*이?\s*없|답답)"
                ],
                "weight": 25
            },
            "대인관계": {
                "patterns": [
                    r"(갈굼|부조리|폭행|폭언|욕설|기수\s*열외|왕따|은따|가스라이팅)",
                    r"(선임|후임|간부|동기)\s*(과|와|한테|에게)?\s*(마찰|갈등|싸움)",
                    r"(지속적|매일)\s*(괴롭히|시비)"
                ],
                "weight": 25
            },
            "복무적응": {
                "patterns": [
                    r"(탈영|복무\s*회피|병가|군대\s*체질\s*아님)",
                    r"(현부심|현역\s*복무\s*부적합|전출|보직\s*변경)",
                    r"(훈련|근무|일과)\s*(가|이)?\s*(너무\s*힘들|적응\s*안\s*됨)"
                ],
                "weight": 20
            }
        }

    def evaluate(self, raw_text: str, spaced_text: str, tokens: list) -> dict:
        """Kiwi 분석 결과를 바탕으로 4대 영역 점수 및 근거 키워드 산출"""
        # 형태소 분해 텍스트 재구성 (예: "잠/NNG 을/JKO 못/MAG 자/VV")
        token_str = " ".join([f"{t.form}/{t.tag}" for t in tokens])
        
        assessment = {}

        for category, config in self.rules.items():
            found_evidence = set()

            for pattern in config["patterns"]:
                # 1. 보정된 문장(spaced_text) 매칭
                for match in re.finditer(pattern, spaced_text):
                    found_evidence.add(match.group())

            evidence_list = list(found_evidence)
            match_count = len(evidence_list)
            
            # 위험 점수 계산 (최대 100점 캡핑)
            score = min(match_count * config["weight"], 100)

            assessment[category] = {
                "score": score,
                "matched_count": match_count,
                "evidence": evidence_list
            }

        return assessment