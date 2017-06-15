$('#search').on('keyup', function() {
    var value = $(this).val();
    var payload = {}

    payload[$('#attribute_selector').val()] =  value;
    console.log(payload)

    $.ajax({
        url: "http://localhost:8000/contacts",
        data: JSON.stringify(payload),
        processData: false,
        type: 'POST',
        contentType: 'application/json',
        success: function(data) {
            var pretty = JSON.stringify(JSON.parse(data), null, 2);
            $( "#output" ).html( pretty );
        }
    });
})
