/**
 * Created by Hamid FzM on 19/10/2014.
 */
alert('با عرض پوزش سایت کمپین هنوز شروع به کار نکرده است و مطالب سایت فعلا کامل نمی باشد.');
$(document).ready(function () {
    $(function () {
        $(".avatar").tooltip({
            placement: 'auto bottom'
        });
    });

    var form = $("#DonatorForm");
    var spinner = $('#support span.fa-spinner');

    form.submit(function (e) {
        e.preventDefault();
        var form_data = form.find('form');

        spinner.show();
        form_data.fadeTo(200, 0, function () {
            form_data.css({visibility: 'hidden'})
        });
        $.ajax({
            type: "POST",
            url: form_data.attr('paction'),
            data: form_data.serialize(),
            success: function (data) {
                //console.log(data);
                if (data.status == 2 || data.status == 3) {
                    if (data.error) alert('خطای شماره ' + data.error + '، لطفا دوباره تلاش کنید.');

                    form_data.fadeTo(200, 1, function () {
                        form_data.css({visibility: 'visible'});
                        form.html(data.form);

                        $('.form-input').tooltip({
                            html: true
                        });

                        // title should exists and must have some value
                        $("[data-original-title!=''][data-original-title]").addClass('error');

                        spinner.hide();
                    });
                } else if (data.status == 1) {
                    window.location = data.redirect;
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
    });

    var dir = $('input[type=text]');
    dir.keyup(function (e) {
        if (isUnicode(dir.val())) {
            $(this).css('direction', 'rtl');
        }
        else {
            $(this).css('direction', 'ltr');
        }
    });
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

function isUnicode(str) {
    var letters = [];
    for (var i = 0; i <= str.length; i++) {
        letters[i] = str.substring((i - 1), i);
        if (letters[i].charCodeAt() > 255) {
            return true;
        }
    }
    return false;
}