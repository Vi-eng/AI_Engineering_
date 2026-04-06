async function sendToAPI() {
    const userInput = document.getElementById("userInput").value;
    const pdfFile = document.getElementById("pdfFile").files[0];
    const output = document.getElementById("responseOutput");

    const formData = new FormData();
    if (userInput) formData.append("user_input", userInput);
    if (pdfFile) formData.append("pdf_file", pdfFile);

    output.textContent = "Processing...";

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        output.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        output.textContent = `⚠️ Error: ${error}`;
    }
}