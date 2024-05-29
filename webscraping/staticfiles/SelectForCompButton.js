function selectProduct(productId, productNumber) {
    console.log('Selected product:', productId, 'for comparison with product', productNumber);

    // Make AJAX requests to retrieve the product details for both products
    $.ajax({
        url: '/get_product_details/',
        method: 'GET',
        data: {'product_id': productId},
        success: function(response) {
            // Update the compare2 section with the received product details for the first product
            $('#compare2-section-' + productNumber).html(response);
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}
