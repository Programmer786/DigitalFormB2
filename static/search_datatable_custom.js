$(document).ready(function() {
    // this is for total table_EXPANSE
    $('#dataTable').DataTable( {
       responsive: true, 
       lengthChange: false, 
       autoWidth: false,
       dom: 'Bfrtip',
       buttons: [
             { extend: 'excelHtml5', footer: true }
       ]
    } );

    // this is for total table_ASSETS
    $('#table_ASSETS').DataTable( {
       responsive: true, 
       lengthChange: false, 
       autoWidth: false,
       dom: 'Bfrtip',
       buttons: [
             { extend: 'excelHtml5', footer: true }
       ]
    } );


    // this is for total one_project_EXPANSE
    $('#one_project_EXPANSE').DataTable( {
        responsive: true, 
        lengthChange: false, 
        autoWidth: false,
        dom: 'Bfrtip',
        buttons: [
              { extend: 'excelHtml5', footer: true }
        ]
     } );


    // this is for total one_project_ASSETS
    $('#one_project_ASSETS').DataTable( {
        responsive: true, 
        lengthChange: false, 
        autoWidth: false,
        dom: 'Bfrtip',
        buttons: [
              { extend: 'excelHtml5', footer: true }
        ]
     } );


     // this is for total one_project_EMPLOYEE 
    $('#one_project_EMPLOYEE').DataTable( {
        responsive: true, 
        lengthChange: false, 
        autoWidth: false,
        dom: 'Bfrtip',
        buttons: [
              { extend: 'excelHtml5', footer: true }
        ]
     } );


     // this is for total all_Employee_Details
    $('#all_Employee_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );


   // this is for total all_Bank_Details
   $('#all_Bank_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );


   // this is for total all_District_Details
   $('#all_District_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );


   // this is for total all_Category_Details
   $('#all_Category_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );

   // this is for total all_Document_Name_Details
   $('#all_Document_Name_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );


   // this is for total all_Tender_Details
   $('#all_Tender_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );


   // this is for total all_Projects_Details
   $('#all_Projects_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );

   // this is for total all_Expense_Details
   $('#all_Expense_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );

   // this is for total all_Asset_Details
   $('#all_Asset_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );

   // this is for total all_Designation_Details
   $('#all_Designation_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );

   // this is for total all_Employee_Details_For_Salary_Details
   $('#all_Employee_Details_For_Salary_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );

   // this is for total all_One_Employee_Details_For_Salary_Details
   $('#all_One_Employee_Details_For_Salary_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );

   // this is for total all_Full_Report_Details_For_Reports_Details
   $('#all_Full_Report_Details_For_Reports_Details').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );

   // this is for total all_Full_Invoices_Details_About_One_Project
   $('#all_Full_Invoices_Details_About_One_Project').DataTable( {
      responsive: true, 
      lengthChange: false, 
      autoWidth: false,
      dom: 'Bfrtip',
      buttons: [
            { extend: 'excelHtml5', footer: true }
      ]
   } );








 } );


// start  this is use for other add_employee salary
  document.addEventListener("DOMContentLoaded", function () {

      // Attach the updateNetSalary function to input events for all input fields
      var inputElements = document.querySelectorAll('.form-control');
      inputElements.forEach(function (input) {
          input.addEventListener('input', updateNetSalary);
      });
  
      // Function to calculate and update net salary
      function updateNetSalary() {
          // Extract the employee ID from the dynamic ID of the input field
          var employeeId = this.id.split("_")[1];
  
          var basicSalary = parseFloat(document.getElementById("EmployeesSalary_" + employeeId).value) || 0;
          var getRemainingAmount = parseFloat(document.getElementById("GetRemainingAmount_" + employeeId).value) || 0;
          var advanceAmount = parseFloat(document.getElementById("AdvanceAmount_" + employeeId).value) || 0;
          var internetPackage = parseFloat(document.getElementById("InternetPackage_" + employeeId).value) || 0;
          var transportation = parseFloat(document.getElementById("Transportation_" + employeeId).value) || 0;
          var overtime = parseFloat(document.getElementById("OverTime_" + employeeId).value) || 0;
          var advanceAmountDeduction = parseFloat(document.getElementById("AdvanceAmountDeduction_" + employeeId).value) || 0;
          var remainingAmountBasicSalary = parseFloat(document.getElementById("RemainingAmountBasicSalary_" + employeeId).value) || 0;
          var incomeTax = parseFloat(document.getElementById("IncomeTax_" + employeeId).value) || 0;
          var eobi = parseFloat(document.getElementById("EOBI_" + employeeId).value) || 0;
          var socialSecurity = parseFloat(document.getElementById("SocialSecurity_" + employeeId).value) || 0;
          var absentees = parseFloat(document.getElementById("Absentees_" + employeeId).value) || 0;
          var otherDeduction = parseFloat(document.getElementById("OtherDeduction_" + employeeId).value) || 0;
  
          // Check for NaN or invalid values
          if (isNaN(basicSalary) || isNaN(getRemainingAmount) || isNaN(advanceAmount) || isNaN(internetPackage) || isNaN(transportation) || isNaN(overtime) || isNaN(advanceAmountDeduction) || isNaN(remainingAmountBasicSalary) || isNaN(incomeTax) || isNaN(eobi) || isNaN(socialSecurity) || isNaN(absentees) || isNaN(otherDeduction)) {
              // Handle the error or provide feedback to the user
              return;
          }
  
          // Calculate gross salary
          var grossSalary = basicSalary + internetPackage + transportation + overtime + advanceAmount + getRemainingAmount;
  
          // Calculate total deduction
          var totalDeduction = advanceAmountDeduction + incomeTax + eobi + socialSecurity + absentees + otherDeduction + remainingAmountBasicSalary;
  
          // Calculate net salary
          var netSalary = grossSalary - totalDeduction;
  
          // Update the calculated values in the UI
          document.getElementById("grossSalary_" + employeeId).innerText = grossSalary.toFixed(2);
          document.getElementById("totalDeduction_" + employeeId).innerText = totalDeduction.toFixed(2);
          document.getElementById("netSalary_" + employeeId).innerText = netSalary.toFixed(2);
      }
  
  });

  document.addEventListener("DOMContentLoaded", function () {
      // Get all elements with class 'advance-amount' and 'remaining-amount-basic-salary'
      var advanceAmountInputs = document.querySelectorAll('.advance-amount');
      var remainingAmountInputs = document.querySelectorAll('.remaining-amount-basic-salary');
  
      // Attach the event listener to each advanceAmountInput
      advanceAmountInputs.forEach(function (advanceAmountInput) {
          advanceAmountInput.addEventListener("input", function () {

            updateRemainingAmountReadOnly(advanceAmountInput);
          });
      });

      // Attach the event listener to each remainingAmountInput
      remainingAmountInputs.forEach(function (remainingAmountInput) {
            remainingAmountInput.addEventListener("input", function () {
                  updateAdvanceAmount(remainingAmountInput);
            });
      });
  
      function updateRemainingAmountReadOnly(advanceAmountInput) {
          var employeeId = advanceAmountInput.getAttribute('data-employee-id');
          var remainingAmountInput = document.getElementById("RemainingAmountBasicSalary_" + employeeId);
          
          var advanceAmount = parseFloat(advanceAmountInput.value) || 0;
  
          // Set readonly attribute based on the value of Advance Amount
          remainingAmountInput.readOnly = advanceAmount > 0;
          if(advanceAmount > 0){
            remainingAmountInput.value=0.0;
          }
      }

      function updateAdvanceAmount(remainingAmountInput) {
            var employeeId = remainingAmountInput.getAttribute('data-employee-id');
            var advanceAmountInput = document.getElementById("AdvanceAmount_" + employeeId);
    
            var remainingAmount = parseFloat(remainingAmountInput.value) || 0;
    
            // Set the value and readonly attribute of Advance Amount based on the value of Remaining Amount
            advanceAmountInput.readOnly = remainingAmount > 0;
            if(remainingAmount > 0){
                  advanceAmountInput.value=0.0;
            }
      }



  });
// End  this is use for other add_employee salary


// start  this is use for other main_add_employee for only Head salary

//   document.addEventListener("DOMContentLoaded", function () {

//       // Attach the updateNetSalary function to input events for all input fields
//       var inputElements = document.querySelectorAll('.form-control');
//       inputElements.forEach(function (input) {
//           input.addEventListener('input', updateNetSalary);
//       });
  
//       // Function to calculate and update net salary
//       function updateNetSalary() {
//           // Extract the employee ID from the dynamic ID of the input field
//           var employeeId = this.id.split("_")[1];
  
//           var basicSalary = parseFloat(document.getElementById("AdminEmployeesSalary_" + employeeId).value) || 0;
//           var getRemainingAmount = parseFloat(document.getElementById("AdminGetRemainingAmount_" + employeeId).value) || 0;
//           var advanceAmount = parseFloat(document.getElementById("AdminAdvanceAmount_" + employeeId).value) || 0;
//           var internetPackage = parseFloat(document.getElementById("AdminInternetPackage_" + employeeId).value) || 0;
//           var transportation = parseFloat(document.getElementById("AdminTransportation_" + employeeId).value) || 0;
//           var overtime = parseFloat(document.getElementById("OverTime_" + employeeId).value) || 0;
//           var advanceAmountDeduction = parseFloat(document.getElementById("AdminAdvanceAmountDeduction_" + employeeId).value) || 0;
//           var remainingAmountBasicSalary = parseFloat(document.getElementById("AdminRemainingAmountBasicSalary_" + employeeId).value) || 0;
//           var incomeTax = parseFloat(document.getElementById("AdminIncomeTax_" + employeeId).value) || 0;
//           var eobi = parseFloat(document.getElementById("AdminEOBI_" + employeeId).value) || 0;
//           var socialSecurity = parseFloat(document.getElementById("AdminSocialSecurity_" + employeeId).value) || 0;
//           var absentees = parseFloat(document.getElementById("AdminAbsentees_" + employeeId).value) || 0;
//           var otherDeduction = parseFloat(document.getElementById("AdminOtherDeduction_" + employeeId).value) || 0;
  
//           // Check for NaN or invalid values
//           if (isNaN(basicSalary) || isNaN(getRemainingAmount) || isNaN(advanceAmount) || isNaN(internetPackage) || isNaN(transportation) || isNaN(overtime) || isNaN(advanceAmountDeduction) || isNaN(remainingAmountBasicSalary) || isNaN(incomeTax) || isNaN(eobi) || isNaN(socialSecurity) || isNaN(absentees) || isNaN(otherDeduction)) {
//               // Handle the error or provide feedback to the user
//               return;
//           }
  
//           // Calculate gross salary
//           var grossSalary = basicSalary + internetPackage + transportation + overtime + advanceAmount + getRemainingAmount;
  
//           // Calculate total deduction
//           var totalDeduction = advanceAmountDeduction + incomeTax + eobi + socialSecurity + absentees + otherDeduction + remainingAmountBasicSalary;
  
//           // Calculate net salary
//           var netSalary = grossSalary - totalDeduction;
  
//           // Update the calculated values in the UI
//           document.getElementById("AdminGrossSalary_" + employeeId).innerText = grossSalary.toFixed(2);
//           document.getElementById("AdminTotalDeduction_" + employeeId).innerText = totalDeduction.toFixed(2);
//           document.getElementById("AdminNetSalary_" + employeeId).innerText = netSalary.toFixed(2);
//       }
  
//   });

//   document.addEventListener("DOMContentLoaded", function () {
//       // Get all elements with class 'advance-amount' and 'remaining-amount-basic-salary'
//       var advanceAmountInputs = document.querySelectorAll('.advance-amount');
//       var remainingAmountInputs = document.querySelectorAll('.remaining-amount-basic-salary');
  
//       // Attach the event listener to each advanceAmountInput
//       advanceAmountInputs.forEach(function (advanceAmountInput) {
//           advanceAmountInput.addEventListener("input", function () {

//             updateRemainingAmountReadOnly(advanceAmountInput);
//           });
//       });

//       // Attach the event listener to each remainingAmountInput
//       remainingAmountInputs.forEach(function (remainingAmountInput) {
//             remainingAmountInput.addEventListener("input", function () {
//                   updateAdvanceAmount(remainingAmountInput);
//             });
//       });
  
//       function updateRemainingAmountReadOnly(advanceAmountInput) {
//           var employeeId = advanceAmountInput.getAttribute('data-employee-id');
//           var remainingAmountInput = document.getElementById("RemainingAmountBasicSalary_" + employeeId);
          
//           var advanceAmount = parseFloat(advanceAmountInput.value) || 0;
  
//           // Set readonly attribute based on the value of Advance Amount
//           remainingAmountInput.readOnly = advanceAmount > 0;
//           if(advanceAmount > 0){
//             remainingAmountInput.value=0.0;
//           }
//       }

//       function updateAdvanceAmount(remainingAmountInput) {
//             var employeeId = remainingAmountInput.getAttribute('data-employee-id');
//             var advanceAmountInput = document.getElementById("AdvanceAmount_" + employeeId);
    
//             var remainingAmount = parseFloat(remainingAmountInput.value) || 0;
    
//             // Set the value and readonly attribute of Advance Amount based on the value of Remaining Amount
//             advanceAmountInput.readOnly = remainingAmount > 0;
//             if(remainingAmount > 0){
//                   advanceAmountInput.value=0.0;
//             }
//       }



//   });

// End  this is use for other main_add_employee for only Head salary


//   this is for all_Full_Report_Details_For_Reports_Details
  document.addEventListener("DOMContentLoaded", function () {
      // Calculate and set the sum for each column
      calculateColumnSum("totalInvoiceNetAmountReceived", 4);
      calculateColumnSum("totalNetSalary", 5);
      calculateColumnSum("totalExpanse", 6);
      calculateColumnSum("totalAssets", 7);
      calculateColumnSum("totalInvest", 8);
      calculateColumnSum("totalProfit", 9);
  });

  function calculateColumnSum(spanId, columnIndex) {
      var total = 0;
      var table = document.getElementById("all_Full_Report_Details_For_Reports_Details");
      for (var i = 0; i < table.rows.length - 1; i++) { // Exclude the last row (tfoot)
          var cell = table.rows[i].cells[columnIndex];
          var value = parseFloat(cell.innerText.replace(',', '')) || 0;
          total += value;
      }
      // .toFixed(1) is used for point like 5000.34 .toFixed(1) for 5000.3
      document.getElementById(spanId).innerText = total.toFixed(1); 
  }



// "Net Received" For Invoice Received
  document.addEventListener("DOMContentLoaded", function () {
      // Attach the updateReceivedAmount function to input events for all input fields
      var inputElements = document.querySelectorAll('.form-control');
      inputElements.forEach(function (input) {
          input.addEventListener('input', updateReceivedAmount);
      });
  
      // Function to calculate and update net received
      function updateReceivedAmount() {
          // Get the parent element (row) of the input that triggered the event
          var row = this.closest('.modal-body');
  
          // Find input elements within the current row
          var TotalRemainingAmount = parseFloat(row.querySelector('.total-remaining-amount').value) || 0;
          var invoiceSubmittedAmount = parseFloat(row.querySelector('.invoice-submitted-amount').value) || 0;
          var invoiceReceivedAmount = parseFloat(row.querySelector('.invoice-received-amount').value) || 0;
          var ReceivedRemainingAmount = parseFloat(row.querySelector('.received-remaining-amount').value) || 0;
          var incomeTaxesAmount = parseFloat(row.querySelector('.income-taxes-amount').value) || 0;
          var gstAmount = parseFloat(row.querySelector('.gst-amount').value) || 0;
          var deductionAmount = parseFloat(row.querySelector('.deduction-amount').value) || 0;
  
          // Check for NaN or invalid values
          if (isNaN(TotalRemainingAmount) || isNaN(invoiceSubmittedAmount) || isNaN(invoiceReceivedAmount) || isNaN(ReceivedRemainingAmount) || isNaN(incomeTaxesAmount) || isNaN(gstAmount) || isNaN(deductionAmount)) {
              // Handle the error or provide feedback to the user
              return;
          }
  
          // Calculate net received amount for the current row
          var netReceivedAmount = invoiceReceivedAmount + incomeTaxesAmount + gstAmount + deductionAmount;
          // Update the net received amount in the UI for the current row
          row.querySelector('.net-received-amount').innerText = netReceivedAmount.toFixed(2);

          // Calculate received remaining amount for the current row
          var TotalRemainingAmount = TotalRemainingAmount - ReceivedRemainingAmount;
          // Calculate received amount for the current row
          var RemainingAmount = invoiceSubmittedAmount + TotalRemainingAmount - netReceivedAmount;
          // Update the received-with-remaining-amount in the UI for the current row
          row.querySelector('.remaining-amount').innerText = RemainingAmount.toFixed(2);
      }
  });



  // This code calculates and updates the "Net Received" amount for each row in the Invoice Received modal
  document.addEventListener("DOMContentLoaded", () => {
      // Get all input fields and attach the updateReceivedAmount function to their input events
      const inputFields = document.querySelectorAll('.form-control');
      inputFields.forEach(input => input.addEventListener('input', updateReceivedAmount));
  }); 
    // Function to calculate and update the net received amount for a row
    function updateReceivedAmount(event) {
      // Get the row that contains the input field that triggered the event
      const row = event.target.closest('.modal-body');
    
      // Find the input fields and calculate the net received amount
      const invoiceSubmittedAmount = parseFloat(row.querySelector('.update-invoice-submitted-amount').value.trim()) || 0;
      const incomeTaxesAmount = parseFloat(row.querySelector('.update-income-taxes-amount').value.trim()) || 0;
      const gstAmount = parseFloat(row.querySelector('.update-gst-amount').value.trim()) || 0;
      const deductionAmount = parseFloat(row.querySelector('.update-deduction-amount').value.trim()) || 0;
    
      // Check for invalid or negative values
      if (isNaN(invoiceSubmittedAmount) || isNaN(incomeTaxesAmount) || isNaN(gstAmount) || isNaN(deductionAmount) ||
          invoiceSubmittedAmount < 0 || incomeTaxesAmount < 0 || gstAmount < 0 || deductionAmount < 0) {
        // Handle the error or provide feedback to the user
        return;
      }
    
      // Calculate the net received amount
      const netReceivedAmount = invoiceSubmittedAmount - incomeTaxesAmount - gstAmount - deductionAmount;
    
      // Update the net received amount in the UI
      row.querySelector('.update-net-received-amount').textContent = netReceivedAmount.toFixed(2);
    
      // Add a class to the row to highlight it
      row.classList.add('updated');
    
      // Remove the class after a short delay
      setTimeout(() => row.classList.remove('updated'), 500);
    }
  
  
