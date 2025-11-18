document.getElementById("sendBtn").addEventListener("click", async () => {
    const inputText = document.getElementById("jsonInput").value;
    const output = document.getElementById("resultOutput");

    if (!inputText) {
        output.textContent = "Debe pegar un JSON válido.";
        return;
    }

    try {
        const jsonBody = JSON.parse(inputText);

        output.textContent = "Procesando...";

        const response = await fetch("/api/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(jsonBody)
        });

        const text = await response.text();
        output.textContent = `Status: ${response.status}\n\n${text}`;

    } catch (error) {
        output.textContent = "Error al procesar el JSON o enviar la solicitud:\n" + error;
    }
});
