app.component('authentication', {
    data() {
        return {
            loginForm: {
                username: '',
                password: ''
            },
            registerForm: {
                username: '',
                email: '',
                password: '',
                passwordConfirm: ''
            },
            
        }
    },
    props: {
        host: String,
        authToken: String
    },
    template:
    /*html*/
    `
    <ul class="nav p-0 auth-nav">
        <span class='py-2 px-3'><i class='fas fa-link'></i></span>
        <template v-if='authToken'>
            <li class="nav-item">
                <a class="nav-link" href="#logout">خروج</a>
            </li>
        </template>
        <template v-else>
            <li class="nav-item">
                <a class="nav-link" href="#register">ثبت نام</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#login">ورود</a>
            </li>
        </template>
    </ul>

    <div class='container-fluid overlay'>
        <div id="delete-url-overlay" class="text-right d-none overlay">
            <span id='close-delete-url' class="p-0 m-0 close-btn">&#x2715;</span>
            <div class="card p-3 text-center mx-auto overlay-content">
                <div id='delete-url-message'></div>
                <div class='text-center m-2'>
                    <a id='delete-url-confirm' class='btn btn-success py-1'>بله</a>
                    <button id='cancel-delete-url' class='btn btn-danger py-1'>خیر</button>
                </div>
            </div>
        </div>
    </div>
    `,
    methods: {}
});