$(document).ready(function(){

    // Fade out either tacos or burritos option
    var burritos = $("#burritos");
    var tacos = $("#tacos");
    var ingredients = $('.ingredients1')
    var allergies = $('.allergies')
    ingredients.fadeOut("fast");
    allergies.fadeOut("fast");

    tacos.on('click', function() {
        if (burritos.hasClass("activeChoice")) {
            burritos.removeClass("activeChoice");
        }
        tacos.addClass('activeChoice');
        $('#foodChoice').val("tacos");
        $('.ingredients1').fadeIn();
    });

    burritos.on('click', function() {
        if (tacos.hasClass("activeChoice")) {
            tacos.removeClass("activeChoice");
        }
        $(this).addClass('activeChoice');
        $('#foodChoice').val("burritos");
        $('.ingredients1').fadeIn();
    });


    $(".chosen-select").chosen({max_selected_options: 3});



  });