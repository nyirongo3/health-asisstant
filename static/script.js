document.getElementById("healthForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const age = document.getElementById("age").value;
    const bmi = document.getElementById("bmi").value;
    const bloodPressure = document.getElementById("blood_pressure").value;
    const cholesterol = document.getElementById("cholesterol").value;

    const formData = new FormData();
    formData.append('age', age);
    formData.append('bmi', bmi);
    formData.append('blood_pressure', bloodPressure);
    formData.append('cholesterol', cholesterol);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("predictionOutput").textContent =  `Predicted Health Risk: ${parseFloat(data.prediction).toFixed(2)}`;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
