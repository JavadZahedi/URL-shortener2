app.component('url-input', {
    data() {
        return {
            shortenedURL: '',
            urlLabel: '',
            urlAddress: '',
        }
    },
    props: ['host'],
    template:
    /*html*/
    `
    <form @submit.prevent='shortenURL' class='container text-center mx-auto my-2 p-2 url-input'>
        <div class='row m-0 p-0'>
            <div class='row col-lg-4 m-0 p-0'>
                <div class='col-sm-3 m-0 p-0'>
                    <label for='url-label'>عنوان:</label>
                </div>
                <div class='col-sm-9 text-center m-0 p-0'>
                    <input id='url-label' placeholder='label' class='m-1' type='text' v-model='urlLabel'>
                </div>
            </div>
            <div class='row col-lg-6 m-0 p-0'>
                <div class='col-sm-3 m-0 p-0'>
                    <label for='url-address'>نشانی:</label>
                </div>
                <div class='col-sm-9 text-center m-0 p-0'>
                    <input id='url-address' placeholder='address' class='m-1' type='url' v-model='urlAddress'>
                </div>
            </div>
            <div class='text-center col-lg-2 m-0 p-0'>
                <button type='submit' class='btn btn-warning m-1 py-1 search-btn'>کوتاه کردن</button>
            </div>
        </div>

        <div v-if='shortenedURL' class='row container mx-auto my-1 p-2 alert alert-info'>
            <div class='col-md-3'>نشانی کوتاه شده:</div>
            <div class='col-md-9'>{{ shortenedURL }}</div>
        </div>
    </form>
    `,
    methods: {
        shortenURL() {
            const URL = {
                label: this.urlLabel,
                address: this.urlAddress
            };
            axios
                .post('/shortener/urls/', URL)
                .then(response => {
                    console.log(response.data.slug);
                    this.shortenedURL = this.host + 'shortener/url-redirect/' + response.data.slug;
                })
                .catch(error => {
                    console.log('OK');
                    console.log(error);
                });
        }
    }
});