/**
 * Created by Hamid FzM on 19/10/2014.
 */
//alert('با عرض پوزش سایت کمپین هنوز شروع به کار نکرده است و مطالب سایت فعلاً نهایی و کامل نیست.');
$(function () {
    $(".avatar").tooltip({
        placement: 'auto bottom'
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
            scrollTop: refElement.offset().top - 76
        }, 1000, 'swing', function () {
            $(document).on("scroll", onScroll);
        });

        currLink.addClass('active');
    });

    $('input[type=text]').keyup(function (e) {
        $(this).css('direction', startsWithRTL($(this).val()) ? 'rtl' : 'ltr');
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

function startsWithRTL(str) {
    // This regex is brought from Google GWT (licensed under Apache 2.0), find FIRST_STRONG_IS_RTL_RE there
    var regex = /^[^A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02B8\u0300-\u0590\u0800-\u1FFF\u2C00-\uFB1C\uFDFE-\uFE6F\uFEFD-\uFFFF]*[\u0591-\u07FF\uFB1D-\uFDFD\uFE70-\uFEFC]/;
    return !!regex.exec(str);
}
