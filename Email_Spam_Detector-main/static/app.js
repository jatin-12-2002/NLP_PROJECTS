document.getElementById('predictBtn').addEventListener('click', async function() {
    const message = document.getElementById('message').value;

    if (message.trim() === "") {
        alert("Please enter a message!");
        return;
    }

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: [message] }),
    });

    const result = await response.json();
    document.getElementById('result').innerText = "Prediction: " + result.Result;
});
