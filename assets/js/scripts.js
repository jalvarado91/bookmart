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

})(jQuery);