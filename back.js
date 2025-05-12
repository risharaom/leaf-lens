async function showTree() {
    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    // Check if a file is selected
    if (!file) {
        alert("Please select an image first.");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    // Send the image to the Flask server
    const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    });

    const result = await response.json();
    alert("Greenery Detected: " + result.green_coverage_percent + "%");
}
function checkFileUpload() {
    const fileInput = document.getElementById('fileInput');
    const uploadStatus = document.getElementById('uploadStatus');
    const uploadError = document.getElementById('uploadError');
    
    if (fileInput.files.length > 0) {
        uploadStatus.style.display = 'block'; // Show upload success message
        uploadError.style.display = 'none';   // Hide error message
    } else {
        uploadError.style.display = 'block';  // Show error message
        uploadStatus.style.display = 'none';  // Hide success message
    }
}