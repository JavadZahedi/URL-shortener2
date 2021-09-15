app.component('page-footer', {
    props: {
        telegramAddress: String,
        baleAddress: String,
        twitterAddress: String,
        instagramAddress: String,
        phoneNumber: String,
    },
    data() {
        return {
            description: `پس از حمایت گستره شما کاربران از وب سایت «کوتاه نشانی اینترنتی
گستر ایران زمین» به منظور ارتقا کیفیت محصول بر آن شدیم تا شعبه دوم این وب سایت را طراحی کنیم.`,
        };
    },
    template:
    /*html*/
    `
    <footer class='p-2 text-center'>
        <hr class='mt-1 mb-0'>
        <p class='p-3'>
            {{ description }}
            <br><br>
            شماره تماس: {{ phoneNumber }}
            <br><br>
            ما را در فضای مجازی نیز دنبال کنید
        </p>
        <div class='container my-0 p-0 d-flex flex-wrap justify-content-center'>
            <a class='d-block icon telegram m-1' href='telegramAddress'></a>
            <a class='d-block icon bale m-1' href='baleAddress'></a>
            <a class='d-block icon twitter m-1' href='twitterAddress'></a>
            <a class='d-block icon instagram m-1' href='instagramAddress'></a>
        </div>
    </footer>
    `
});