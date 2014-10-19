/**
 * Created by Hamid FzM on 19/10/2014.
 */

$(document).ready(function () {
    var form = $("#DonatorForm");

    form.submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: form.find('form').attr('action'),
            data: form.serialize(),
            success: function (data) {
                if (data.status == 2){
                    form.html(data.form);
                    console.log(data)
                }
            }
        });
    });

    $(document).on("scroll", onScroll);

    $('.top-menu-item').click(function (e) {
        var currLink = $(this);
        var refElement = $(currLink.attr('href'));

        if (!refElement.length) return;

        e.preventDefault();
        $(document).off("scroll");


        $('.top-menu-item.active').removeClass('active');

        $('html, body').stop().animate({
            scrollTop: refElement.offset().top - 100
        }, 1000, 'swing', function () {
            $(document).on("scroll", onScroll);
        });

        currLink.addClass('active');
    })
});

function onScroll(e) {
    var scrollPos = $(document).scrollTop();
    $('.top-menu-item').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr('href'));

        if (!refElement.length) return;

        var top = refElement.position().top - 100;
        if (top <= scrollPos && top + refElement.height() > scrollPos) {
            $('.top-menu-item.active').removeClass('active');
            currLink.addClass('active');
        }
        else {
            currLink.removeClass('active');
        }
    });
}