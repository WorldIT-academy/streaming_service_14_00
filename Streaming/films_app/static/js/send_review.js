$(document).ready(() => {
    console.log($('#reviewForm'))
    $('#reviewForm').submit(function(event){
        event.preventDefault();
        $.ajax({
            type : 'post',
            data : $(this).serialize(),
            success : function(response){
                if (response.success) {
                    $('#message_success').empty();
                    $('#message_success').html('<p style="color: green">' + response.message +'</p>');
                    $('#reviewForm')[0].reset();
                }
            },
        });
    });
});