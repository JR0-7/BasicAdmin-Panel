
    // // Get the alert element
    // var alertElement = document.getElementById("myAlert");

    // // Function to hide the alert
    // function hideAlert() {
    //     alertElement.style.display = "none";
    // }

    // // Set a timeout to call the hideAlert function after 5000 milliseconds (5 seconds)
    // setTimeout(hideAlert, 2000);

    // $(document).ready(function() {
    //     $("#myAlert").click(() => {
    //       console.log('hi');
    //     });
    //   });


    document.addEventListener('DOMContentLoaded', function() {
        var alertElement = document.getElementById("myAlert");
        if (alertElement !== null) {
            function hideAlert() {
                alertElement.style.display = "none";
            }
            setTimeout(hideAlert, 2000);
        } else {
            console.error("Element with ID 'myAlert' not found in the document.");
        }
    });
    