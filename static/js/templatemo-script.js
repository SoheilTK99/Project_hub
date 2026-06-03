

$(document).ready(function () {

    // فقط اگر صفحه اصلی بود اجرا شود
    if ($('body').hasClass('home-page')) {

        const autoplayBg = true;
        initBg(autoplayBg);

        const bgControl = $('.tm-bg-control');
        bgControl.click(function () {
            bgControl.removeClass('active');
            $(this).addClass('active');
            const id = $(this).data('id');
            setBg(id);
        });

        $(window).on("backstretch.after", function (e, instance, index) {
            const bgControl = $('.tm-bg-control');
            bgControl.removeClass('active');
            const current = $(".tm-bg-controls-wrapper").find(`[data-id=${index}]`);
            current.addClass('active');
        });


    

    } else {
        // اگر صفحه داخلی بود، هر بک‌گراندی destroy شود
        $.backstretch('destroy', true);
    }

});
