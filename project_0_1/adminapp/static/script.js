    // Get the alert element
    var alertElement = document.getElementById("myAlert");

    // Function to hide the alert
    function hideAlert() {
        alertElement.style.display = "none";
    }

    // Set a timeout to call the hideAlert function after 5000 milliseconds (5 seconds)
    setTimeout(hideAlert, 2000);

