async function sendPrediction() {

    const jsonData = document.getElementById("jsonInput").value;

    const response = await fetch("/api/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: jsonData
    });

    const result = await response.json();
    document.getElementById("result").innerText = JSON.stringify(result, null, 2);
}
