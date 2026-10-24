// Chart.js 시계열 매트릭스 및 레이더 차트 모듈

// 1. 시계열 위험 탐지 매트릭스 렌더링
(function renderTimeSeriesMatrix() {
    const container = document.getElementById('lineChart');
    if (!container) return;

    // 회차/월별 라벨
    const timelineLabels = ['1월', '2월', '3월', '4월', '5월', '6월'];

    // 영역별 탐지 데이터 (true: 탐지/채워진 원, false: 미탐지/빈 원)
    const matrixData = [
        {
            category: '정신건강·정서',
            status: [false, true, true, true, true, true]
        },
        {
            category: '자살위험·자살생각',
            status: [false, false, false, false, false, true]
        },
        {
            category: '추가확인·불면',
            status: [false, false, true, true, true, true]
        },
        {
            category: '추가확인·이성문제',
            status: [false, false, false, false, true, true]
        }
    ];

    // HTML 구조 생성
    let html = `
        <div class="matrix-container">
            <div class="matrix-legend">
                <span class="legend-item"><span class="matrix-dot dot-detected"></span> 탐지</span>
                <span class="legend-sep">·</span>
                <span class="legend-item"><span class="matrix-dot dot-undetected"></span> 미탐지</span>
            </div>
            
            <table class="matrix-table">
                <thead>
                    <tr>
                        <th class="col-category"></th>
                        ${timelineLabels.map(label => `<th>${label}</th>`).join('')}
                    </tr>
                </thead>
                <tbody>
                    ${matrixData.map(row => `
                        <tr>
                            <td class="row-label">${row.category}</td>
                            ${row.status.map(isDetected => `
                                <td>
                                    <span class="matrix-dot ${isDetected ? 'dot-detected' : 'dot-undetected'}"></span>
                                </td>
                            `).join('')}
                        </tr>
                    `).join('')}
                </tbody>
            </table>
            
            <div class="matrix-caption">4개 영역에서 시점이 다른 탐지가 누적된다</div>
        </div>
    `;

    container.innerHTML = html;
})();

// 2. Radar 차트
const ctxRadar = document.getElementById('radarChart').getContext('2d');
const radarChart = new Chart(ctxRadar, {
    type: 'radar',
    data: {
        labels: ['정신건강', '대인관계', '자살/자해위험', '복무적응'],
        datasets: [{
            label: '위험 수치',
            data: [78, 65, 85, 70],
            backgroundColor: 'rgba(16, 185, 129, 0.25)',
            borderColor: '#10b981',
            borderWidth: 2,
            pointBackgroundColor: '#10b981'
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
            r: {
                angleLines: { color: '#e2e8f0' },
                grid: { color: '#e2e8f0' },
                suggestedMin: 0,
                suggestedMax: 100,
                ticks: { display: false }
            }
        }
    }
});