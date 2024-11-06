document.getElementById("prediction-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = {
        TEMP: parseFloat(document.getElementById("temp").value),
        PULSE: parseFloat(document.getElementById("pulse").value),
        RESP: parseFloat(document.getElementById("resp").value),
        BPSYS: parseFloat(document.getElementById("bpsys").value),
        BPDIAS: parseFloat(document.getElementById("bpdias").value), // Corrected key name
        POPCT: parseFloat(document.getElementById("popct").value),
    };

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        const result = await response.json();
        document.getElementById("result").textContent = `Vorhersage: ${result.Prediction}`;
    } catch (error) {
        document.getElementById("result").textContent = `Error: ${error.message}`;
    }
});
