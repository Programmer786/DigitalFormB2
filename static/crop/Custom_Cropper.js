document.addEventListener('DOMContentLoaded', function() {
  const uploadInput = document.getElementById('uploadInput');
  const uploadedImage = document.getElementById('uploadedImage');
  const cropButton = document.getElementById('cropButton');
  let cropper;

  // Event listener for file upload
  uploadInput.addEventListener('change', function(e) {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = function(event) {
      // Update the source of the uploaded image
      uploadedImage.src = event.target.result;

      // Initialize Cropper.js with the uploaded image
      cropper = new Cropper(uploadedImage, {
        aspectRatio: 1, // Set the aspect ratio for the crop box
        viewMode: 2 // Enable the "crop" view mode
      });

      // Enable the crop button
      cropButton.disabled = false;
    };

    reader.readAsDataURL(file);
  });

  // Event listener for crop button
  cropButton.addEventListener('click', function() {
    // Get the cropped image data
    const croppedImageData = cropper.getCroppedCanvas().toDataURL('image/jpeg');

    // Do something with the cropped image data (e.g., upload to server)

    // Reset the UI
    uploadedImage.src = '';
    uploadInput.value = '';
    cropper.destroy();
    cropper = null;
    cropButton.disabled = true;
  });
});
