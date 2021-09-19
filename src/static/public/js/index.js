const app = Vue.createApp({
    data() {
        return {
            host: 'http://127.0.0.1:8000/',
            authToken: null,
            contactUs: {
                telegramAddress: '#',
                baleAddress: '#',
                twitterAddress: '#',
                instagramAddress: '#',
                phoneNumber: '۰۲۱۵۵۳۳۲۲۱۱'
            }
        }
    },
    computed: {},
    methods: {}
});