/* timer/static/timer/script.js */

let startTime;
let elapsedTime = 0;
let timerInterval;
let isRunning = false;

// HTMLの要素を取得
const display = document.getElementById('timer-display');
const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const statusMsg = document.getElementById('status-msg');

// 保存先URLをHTMLのdata属性から取得するための要素
const timerData = document.getElementById('timer-data');

// 時間を表示用にフォーマットする関数 (HH:MM:SS)
function formatTime(ms) {
    let totalSeconds = Math.floor(ms / 1000);
    let hours = Math.floor(totalSeconds / 3600);
    let minutes = Math.floor((totalSeconds % 3600) / 60);
    let seconds = totalSeconds % 60;

    return String(hours).padStart(2, '0') + ':' + 
           String(minutes).padStart(2, '0') + ':' + 
           String(seconds).padStart(2, '0');
}

function startTimer() {
    if (isRunning) return;
    
    isRunning = true;
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        display.textContent = formatTime(elapsedTime);
    }, 100); // 100msごとに更新

    // ボタンの表示切替
    startBtn.style.display = 'none';
    stopBtn.style.display = 'inline-block';
    statusMsg.textContent = '計測中... 頑張ってください！';

    console.log("WebSocket: Start notification sent (Not implemented yet)");
}



function saveRecord(minutes) {
    const saveUrl = timerData.dataset.saveUrl;
    
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(saveUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ minutes: minutes })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('サーバーエラーが発生しました');
        }
        return response.json();
    })
    .then(data => {
        if (data.status === 'ok') {
            console.log("Saved:", data);
            statusMsg.textContent = `${minutes}分記録しました！更新します...`;
            statusMsg.style.color = "green";
            setTimeout(() => {
                location.reload();
            }, 1500);
        } else {
            statusMsg.textContent = `エラー: ${data.message}`;
            statusMsg.style.color = "red";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        statusMsg.textContent = "保存に失敗しました。";
        statusMsg.style.color = "red";
    });
}

