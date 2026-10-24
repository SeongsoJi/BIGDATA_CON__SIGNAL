// Chart.js 시계열 및 레이더 차트 모듈
        // Chart.js 시계열 및 레이더 차트 로드
        const ctxLine = document.getElementById('lineChart').getContext('2d');
        const lineChart = new Chart(ctxLine, {
            type: 'line',
            data: {
                labels: ['1차 면담 (02.09)', '2차 면담 (07.22)', '3차 면담 (09.01)'],
                datasets: [
                    {
                        label: '정신건강',
                        data: [20, 42, 78],
                        borderColor: '#ec4899',
                        backgroundColor: '#ec4899',
                        tension: 0.2,
                        borderWidth: 2
                    },
                    {
                        label: '대인관계',
                        data: [22, 38, 65],
                        borderColor: '#f59e0b',
                        backgroundColor: '#f59e0b',
                        tension: 0.2,
                        borderWidth: 2
                    },
                    {
                        label: '자살/자해위험',
                        data: [10, 15, 85],
                        borderColor: '#a855f7',
                        backgroundColor: '#a855f7',
                        tension: 0.2,
                        borderWidth: 2
                    },
                    {
                        label: '복무적응',
                        data: [30, 50, 70],
                        borderColor: '#10b981',
                        backgroundColor: '#10b981',
                        tension: 0.2,
                        borderWidth: 2
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: { font: { size: 9 }, boxWidth: 10 }
                    }
                },
                scales: {
                    y: { min: 0, max: 100, ticks: { font: { size: 9 } } },
                    x: { ticks: { font: { size: 9 } } }
                }
            }
        });

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
    
