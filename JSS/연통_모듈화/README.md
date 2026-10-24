# 연통 HTML 모듈화 결과

## 실행
`index.html`을 브라우저에서 열어 확인합니다. Chart.js는 CDN을 사용하므로 차트 표시에는 인터넷 연결이 필요합니다.

## 구조
- `index.html`: 페이지 마크업
- `css/style.css`: 기존 스타일
- `js/counseling-data.js`: 면담/관찰기록 데이터
- `js/common.js`: 인증 타이머 및 공통 알림 모달
- `js/counseling.js`: 면담 목록, 페이지네이션, 상세보기
- `js/charts.js`: Chart.js 시계열/레이더 차트

기존 화면과 동작을 최대한 유지하는 방식으로 CSS와 JavaScript를 파일별로 분리했습니다. HTML 안의 개별 `style` 속성은 이번 분리 범위에서 그대로 유지했습니다.
