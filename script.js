function uploadImage() {
    const imageInput = document.getElementById("imageInput");
    const resultDiv = document.getElementById("result");
    const imagePreview = document.getElementById("uploadedImage");
    
    const file = imageInput.files[0];
    
    if (!file) {
        resultDiv.innerHTML = "Please select an image first.";
        return;
    }
    
    const formData = new FormData();
    formData.append("image", file);

    // Displaying image preview
    const reader = new FileReader();
    reader.onload = function(event) {
        imagePreview.src = event.target.result;
    };
    reader.readAsDataURL(file);
    
    // Send image to backend for classification
    fetch('/classify', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = `Classification Result: ${data.severity}`;
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = "An error occurred. Please try again.";
    });
}
