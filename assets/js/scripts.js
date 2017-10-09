(function($) {
  "use strict";

  $("body").scrollspy({
    target: ".fixed-top",
    offset: 60
  });

  $("#collapsingNavbar li a").click(function() {
    /* always close responsive nav after click */
    $(".navbar-toggler:visible").click();
  });

  /*lida code for phot popup*/
  $(".col-sm-3 img").click(function() {
    $(".show").fadeIn();
  });

  $("#close-overlay, .overlay").click(function() {
    $(".show").fadeOut();
  });

  $(".tab-panels .tabs li a").on("click", function() {
    $(".tab-panels .tabs li a.active").removeClass("active");
    $(this).addClass("active");

    var showPanel = $(this).attr("rel");

    $(".tab-panels .panel.active").hide(0, function() {
      $("#" + showPanel).show(0, function() {
        $(this).addClass("active");
      });
    });
  });
})(jQuery);
