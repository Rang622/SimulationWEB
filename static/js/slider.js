
const slider = document.getElementById('Humidity');
const output = document.getElementById('HumidityValue');

function updateSliderGradient(value) {
    slider.style.setProperty('--value', value);
}

slider.oninput = function() {
    output.innerHTML = this.value + '%';
    updateSliderGradient(this.value);
}

// Initialize slider position
updateSliderGradient(slider.value);
