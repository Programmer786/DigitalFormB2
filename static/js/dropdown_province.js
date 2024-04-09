  // Function to fetch districts based on selected province
  function getDistrictsByProvince(provinceName) {
      $.ajax({
        url: "/get-districts",
        data: { province_name: provinceName },
        success: function (districts) {
          var districtDropdown = $("#district-dropdown");
          districtDropdown.empty();
          districtDropdown.append("<option value=''>Select District</option>");
          $.each(districts, function (key, value) {
            districtDropdown.append("<option value='" + value.id + "'>" + value.name + "</option>"); // date sent to html
          });
        },
        error: function (xhr, status, error) {
          console.error(error);
        },
      });
    }


  // Event listener for province dropdown change for first
  $("#province-dropdown").change(function () {
    //var province_name = $(this).find("option:selected").text(); //this for using str value
    var province_name = $(this).val();  //this for using int value
    if (province_name && province_name !== "None") {
      getDistrictsByProvince(province_name);
    } else {
      // If no province is selected, clear the districts and tehsils dropdowns
      $("#district-dropdown").empty();
      $("#district-dropdown").append("<option value=''>Select District</option>");
    }
  });
