// 면담 및 관찰기록 목록, 페이징, 상세보기 모듈
const counselingList = window.COUNSELING_LIST;
        // [요청사항 2] 3개 단위 페이징 설정
        const itemsPerPage = 3;
        let currentPage = 1;

        function renderCounselingTable(page) {
            currentPage = page;
            const tbody = document.getElementById('counselingTbody');
            tbody.innerHTML = '';

            const startIdx = (page - 1) * itemsPerPage;
            const endIdx = Math.min(startIdx + itemsPerPage, counselingList.length);

            for (let i = startIdx; i < endIdx; i++) {
                const item = counselingList[i];
                const tr = document.createElement('tr');
                tr.className = 'clickable-row';
                tr.onclick = function() { showCounselingDetail(item.id); };

                tr.innerHTML = `
                    <td>${i + 1}</td>
                    <td>${item.date}</td>
                    <td>${item.type}</td>
                    <td>${item.file1}</td>
                    <td>${item.file2}</td>
                    <td>${item.file3}</td>
                    <td>${item.category}</td>
                    <td>${item.writer}</td>
                    <td>${item.firstTime}</td>
                    <td class="left">${item.summary}</td>
                `;
                tbody.appendChild(tr);
            }

            renderPagination();
        }

        function renderPagination() {
            const container = document.getElementById('paginationControls');
            container.innerHTML = '';

            const totalPages = Math.ceil(counselingList.length / itemsPerPage);

            const prevBtn = document.createElement('button');
            prevBtn.className = 'pagination-btn';
            prevBtn.innerHTML = '◀';
            prevBtn.onclick = () => { if (currentPage > 1) renderCounselingTable(currentPage - 1); };
            container.appendChild(prevBtn);

            for (let p = 1; p <= totalPages; p++) {
                const btn = document.createElement('button');
                btn.className = `pagination-btn ${p === currentPage ? 'active' : ''}`;
                btn.textContent = `[${p}]`;
                btn.onclick = () => renderCounselingTable(p);
                container.appendChild(btn);
            }

            const nextBtn = document.createElement('button');
            nextBtn.className = 'pagination-btn';
            nextBtn.innerHTML = '▶';
            nextBtn.onclick = () => { if (currentPage < totalPages) renderCounselingTable(currentPage + 1); };
            container.appendChild(nextBtn);
        }

        // [요청사항 1] 상세보기 화면 조회 (면담자 백희민 고정)
        function showCounselingDetail(recId) {
            const data = counselingList.find(item => item.id === recId) || counselingList[0];

            document.getElementById('dtlInterviewer').textContent = '백희민';
            document.getElementById('dtlDate').textContent = data.date;
            document.getElementById('dtlCategory').textContent = data.category;
            document.getElementById('dtlType').textContent = data.type;
            document.getElementById('dtlContent').textContent = data.content;
            document.getElementById('dtlWriter').textContent = data.writer;
            document.getElementById('dtlFirstTime').textContent = data.firstTime;
            document.getElementById('dtlLastTime').textContent = data.lastTime;
            document.getElementById('dtlAction').textContent = data.action;
            document.getElementById('dtlFile1').textContent = data.file1;
            document.getElementById('dtlFile2').textContent = data.file2;
            document.getElementById('dtlFile3').textContent = data.file3;

            if (data.showButtons) {
                document.getElementById('btnModify').style.display = 'inline-block';
                document.getElementById('btnDelete').style.display = 'inline-block';
            } else {
                document.getElementById('btnModify').style.display = 'none';
                document.getElementById('btnDelete').style.display = 'none';
            }

            document.getElementById('counselingListView').style.display = 'none';
            document.getElementById('counselingDetailView').style.display = 'block';

            document.getElementById('counselingDetailView').scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        function hideCounselingDetail() {
            document.getElementById('counselingDetailView').style.display = 'none';
            document.getElementById('counselingListView').style.display = 'block';
            document.getElementById('counselingListView').scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        window.onload = function() {
            renderCounselingTable(1);
        };

