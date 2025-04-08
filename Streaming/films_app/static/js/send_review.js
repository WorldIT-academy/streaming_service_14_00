$(document).ready(() => {
    console.log($('#reviewForm'))
    $('#reviewForm').submit((event) => {
        event.preventDefault();
        $.ajax({
            type : 'post',
            data : $(this).serialize(),
            // beforeSend: (xhr) => {
            //     xhr.setRequestHeader("X-CSRFToken", csrftoken);
            // },
            // 
            // headers: {
            //     "X-CSRFToken": $(this).find('input[name="csrfmiddlewaretoken"]').val()
            // },
            success : (response) => {
                if (response.success) {
                    $('#message_success').empty();
                    $('#message_success').html('<p style="color: green">' + response.message +'</p>');
                    $('#reviewForm')[0].reset();
                }
            },
            // 
            
        });
    });
});