$(document).ready(function(){

    // Fade out either tacos or burritos option
    var burritos = $("#burritos");
    var tacos = $("#tacos");
    var ingredients = $('.ingredients1');
    var allergies = $('.allergies');
    var zipCode = $('.zipCode');
    var button = $('.submitBtn');
    ingredients.fadeOut("fast");
    allergies.fadeOut("fast");
    zipCode.fadeOut("fast");
    button.fadeOut("fast");

    tacos.on('click', function() {
        if (burritos.hasClass("activeChoice")) {
            burritos.removeClass("activeChoice");
        }
        tacos.addClass('activeChoice');
        $('#foodChoice').val("tacos");
        ingredients.fadeIn();
        window.scrollTo(0,document.querySelector(".container").scrollHeight);
    });

    burritos.on('click', function() {
        if (tacos.hasClass("activeChoice")) {
            tacos.removeClass("activeChoice");
        }
        $(this).addClass('activeChoice');
        $('#foodChoice').val("burritos");
        ingredients.fadeIn();
    });

    ingredients.on('click', function() {
        window.scrollTo(0,document.querySelector(".container").scrollHeight);
    });

    ingredients.on('change', function() {
        allergies.fadeIn();
    });

    allergies.on('click', function() {
        window.scrollTo(0,document.querySelector(".container").scrollHeight);
    });

    allergies.on('change', function() {
        zipCode.fadeIn();
    });

    // zipCode.on('change', function() {
    //     button.fadeIn();
    // });

    $(".chosen-select").chosen({max_selected_options: 3});
    $(".chosen-select-2").chosen();

  });