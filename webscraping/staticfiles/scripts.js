// scripts.js



jQuery(document).ready(function($)
{

    // AJAX code for autocomplete search functionality
    $(document).ready(function()
    {
        $('#search-input').keyup(function()
        {
            var query = $(this).val();
            if (query.length >= 3)
            {
                $.ajax({
                    url: '/search/',
                    data: {'query': query},
                    success: function(response)
                    {   console.log(query)
                        $('#search-results').empty();
                        console.log(query)
                        $.each(response.products, function(index, product)
                        {
                            $('#search-results').append('<div>' + product + '</div>');
                        });
                        console.log(query)
                    }
                });
            }
        });
    });
});
