//AddToComparison.js
function addToComparison(productId) {
    // Retrieve the existing comparison array from session storage
    let comparison = JSON.parse(sessionStorage.getItem('comparison')) || [];

    // Add the product ID to the comparison array
    comparison.push(productId);

    // Update the session storage with the updated comparison array
    sessionStorage.setItem('comparison', JSON.stringify(comparison));

    // Optionally, provide visual feedback to the user
    alert('Product added to comparison');
}