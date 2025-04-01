console.log("Запит")
$(document).ready(function (){
    let amountFilms = $('.amount-favourite-films');
    let countFilms;

    $('.add-to-favorite').each(function(){
        $(this).on('click', function(){
            $.ajax({
                url : $(this).val(),
                type : 'get',
                success : function(response){
                    countFilms = amountFilms.text();
                    +countFilms++;
                    amountFilms.text(countFilms);
                }  
            });
        });
    });
});