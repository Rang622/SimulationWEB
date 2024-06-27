document.addEventListener("DOMContentLoaded", function() {
    const startButton = document.querySelector('.actions.special a.button');
    const inputs = document.querySelectorAll('input[type="text"], input[type="number"]');
    
    function checkInputs() {
        const allFilled = Array.from(inputs).every(input => input.value.trim() !== '');
        if (allFilled) {
            startButton.classList.remove('disabled');
        } else {
            startButton.classList.add('disabled');
        }
    }
    
    inputs.forEach(input => {
        input.addEventListener('input', checkInputs);
    });

    // 시작 버튼 클릭 시, 비활성화 상태면 동작하지 않음
    startButton.addEventListener('click', function(event) {
        if (this.classList.contains('disabled')) {
            event.preventDefault();
        }
    });

    checkInputs(); // 페이지 로드 시 검사 실행
});

