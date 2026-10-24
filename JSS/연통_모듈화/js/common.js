
        // 상단 인증 시간 타이머
        let totalSeconds = 29 * 60 + 30;
        setInterval(() => {
            if (totalSeconds > 0) {
                totalSeconds--;
                const m = String(Math.floor(totalSeconds / 60)).padStart(2, '0');
                const s = String(totalSeconds % 60).padStart(2, '0');
                document.getElementById('timer').textContent = `${m}:${s}`;
            }
        }, 1000);

        // 커스텀 모달 알림 함수 (alert 대용)
        function showMsg(msg) {
            document.getElementById('armyModalMsg').textContent = msg;
            document.getElementById('armyModal').style.display = 'flex';
        }

        function closeMsg() {
            document.getElementById('armyModal').style.display = 'none';
        }

