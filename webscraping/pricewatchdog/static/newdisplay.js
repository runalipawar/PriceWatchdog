document.addEventListener('DOMContentLoaded', function() {
    // Your JavaScript code here

console.log('Executing new display.js');

var comparison = JSON.parse(sessionStorage.getItem('comparison'));

// Check if the comparison array is present and has at least one product ID
if (comparison && comparison.length >= 1) {
    // Extract the first product ID for comparison
    var productId1 = comparison[0];
    console.log('productId1:', productId1);

    // Construct the URL for the compare2 page with the extracted product ID as a URL parameter
    var compare2URL = '/compare2/' + productId1;
    console.log('compare2URL:', compare2URL);

    // Handle click event on the compare button
    document.getElementById('compareButton').addEventListener('click', function() {
        // Redirect the user to the compare2 page
        window.location.href = compare2URL;
    });
} else {
    // Handle the case where no product IDs are present in session storage
    alert('No product IDs available for comparison.');
}
});