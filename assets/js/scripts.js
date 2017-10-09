(function($) {
    "use strict";

    $('body').scrollspy({
        target: '.fixed-top',
        offset: 60
    });

    $('#collapsingNavbar li a').click(function() {
        /* always close responsive nav after click */
        $('.navbar-toggler:visible').click();
    });

    /*lida code for phot popup*/
    $(".col-sm-3 img").click(function () {
        var $src = $(this).attr("src");
        $(".show").fadeIn();
        $(".img-show img").attr("src", $src);
    });

    $("span, .overlay").click(function () {
      $(".show").fadeOut();
    });


      $('.tab-panels .tabs li').on('click', function () {
          $('.tab-panels .tabs li.active').removeClass('active');
          $(this).addClass('active');

          var showPanel = $(this).attr('rel');

          $('.tab-panels .panel.active').slideUp(300, function () {

              $('#'+ showPanel).slideDown(300, function () {
                  $(this).addClass('active');
              });
          });
       });



})(jQuery);
