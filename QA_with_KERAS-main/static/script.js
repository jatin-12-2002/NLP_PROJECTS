document.getElementById('submitBtn').addEventListener('click', async () => {
    const story = document.getElementById('story').value.trim();
    const query = document.getElementById('query').value.trim();

    if (!story || !query) {
        alert('Please provide both story and query.');
        return;
    }

    const formData = new FormData();
    formData.append('story', story);
    formData.append('query', query);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById('output').innerHTML = `
                <strong>User Story:</strong> ${result.user_story} <br>
                <strong>User Query:</strong> ${result.user_query} <br>
                <strong>Prediction:</strong> ${result.prediction}
            `;
        } else {
            document.getElementById('output').innerHTML = `<span style="color: red;">Error: ${result.error}</span>`;
        }
    } catch (error) {
        document.getElementById('output').innerHTML = `<span style="color: red;">Error: ${error.message}</span>`;
    }
});