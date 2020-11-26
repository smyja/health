// ========= Navbar changes color on scroll =============
$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    if (scroll < 50) {
        $('.fixed-top').css('background', 'transparent');
    } else {
        $('.fixed-top').css('background', '#FFFFFF');
    }
});