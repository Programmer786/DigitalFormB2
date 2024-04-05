// Get the preview container and input field
var previewContainer = document.getElementById('croppedPreview');
var input = document.getElementById('imageUpload');
var cropButton = document.getElementById('cropButton'); // Add a button element with id="cropButton" in your HTML

// Initialize Cropper.js
var cropper;

// When a new image is selected
input.addEventListener('change', function(e) {
  var file = e.target.files[0];

  // Check if the file is an image
  if (file && file.type.includes('image')) {
    // Create a FileReader to read the file
    var reader = new FileReader();

    // When the FileReader finishes loading
    reader.onload = function(event) {
      var dataURL = event.target.result;

      // Destroy the previous Cropper instance, if any
      if (cropper) {
        cropper.destroy();
      }

      // Create a new image element
      var img = document.createElement('img');

      // Set the source of the image to the uploaded file
      img.src = dataURL;

      // Append the image to the preview container
      previewContainer.innerHTML = '';
      previewContainer.appendChild(img);

      // Initialize Cropper.js on the image
      cropper = new Cropper(img, {
        aspectRatio: 1,  // Set the desired aspect ratio for cropping (e.g., 1 for square)
        viewMode: 1,     // Set the desired view mode (e.g., 1 for restricted crop area)
        crop: function(event) {
          // Do something with the cropped data if needed
          var croppedData = cropper.getData();
          console.log(croppedData);
        }
      });
    };

    // Read the uploaded file as a data URL
    reader.readAsDataURL(file);
  }
});

// Trigger image cropping when the button is clicked
cropButton.addEventListener('click', function() {
  cropImage();
});

// Function to perform image cropping
function cropImage() {
  if (cropper) {
    var croppedCanvas = cropper.getCroppedCanvas();
    var croppedDataURL = croppedCanvas.toDataURL();

    // Do something with the cropped image data
    console.log(croppedDataURL);
  }
}


























// // Get the input field and the preview container
// var input = document.getElementById('imageUpload');
// var previewContainer = document.getElementById('croppedPreview');

// // Initialize Cropper.js
// var cropper;

// // When a new image is selected
// input.addEventListener('change', function(e) {
//   var file = e.target.files[0];
  
//   // Check if the file is an image
//   if (file && file.type.includes('image')) {
//     // Create a FileReader to read the file
//     var reader = new FileReader();
    
//     // When the FileReader finishes loading
//     reader.onload = function(event) {
//       var dataURL = event.target.result;
      
//       // Destroy the previous Cropper instance, if any
//       if (cropper) {
//         cropper.destroy();
//       }
      
//       // Create a new image element
//       var img = document.createElement('img');
      
//       // Set the source of the image to the uploaded file
//       img.src = dataURL;
      
//       // Append the image to the preview container
//       previewContainer.innerHTML = '';
//       previewContainer.appendChild(img);
      
//       // Initialize Cropper.js on the image
//       cropper = new Cropper(img, {
//         aspectRatio: 1,  // Set the desired aspect ratio for cropping (e.g., 1 for square)
//         viewMode: 1,     // Set the desired view mode (e.g., 1 for restricted crop area)
//         crop: function(event) {
//           // Do something with the cropped data if needed
//           var croppedData = cropper.getData();
//           console.log(croppedData);
//         }
//       });
//     };
    
//     // Read the uploaded file as a data URL
//     reader.readAsDataURL(file);
//   }
// });
