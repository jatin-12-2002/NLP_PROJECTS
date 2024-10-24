document.getElementById("fileUploadForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const fileInput = document.getElementById("file");
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const statusDiv = document.getElementById("status");
    statusDiv.textContent = "Uploading file...";

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.outputError) {
            statusDiv.textContent = `Error: ${data.outputError}`;
            return;
        }
        statusDiv.textContent = "File uploaded successfully. Starting processing...";
        processAudio(); // Start processing after successful upload
    })
    .catch(error => {
        statusDiv.textContent = `Error: ${error}`;
    });
});

function processAudio() {
    fetch("/startprocessing", {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("status").textContent = "Processing complete!";
        
        // Update content of each pre element without changing the structure
        document.getElementById("transcript").textContent = JSON.stringify(data.inputFileTranscriptedOp, null, 2);
        document.getElementById("spellCorrected").textContent = JSON.stringify(data.spellCorrectedOpMap, null, 2);
        document.getElementById("extractedKeywords").textContent = JSON.stringify(data.extractedKeywors, null, 2);
        
        // Scroll to the results section after processing
        document.getElementById("transcriptResults").scrollIntoView({ behavior: "smooth" });
    })
    .catch(error => {
        document.getElementById("status").textContent = `Processing Error: ${error}`;
    });
}
