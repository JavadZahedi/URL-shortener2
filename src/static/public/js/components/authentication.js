app.component('authentication', {
    data() {
        return {
            consts: {
                DISPLAY_LOGIN: 1,
                DISPLAY_REGISTER: 2,
                DISPLAY_NONE: 3
            },
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
            formDisplayStatus: 3, // It equals to DISPLAY_NONE
            isAuthenticated: false
        }
    },
    props: {},
    computed: {
        displayOverlay() {
            return this.formDisplayStatus !== this.consts.DISPLAY_NONE;
        }
    },
    methods: {
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },
        setCSRFHeader() {
            axios.get('/accounts/set-csrf-cookie/');
            const csrftoken = this.getCookie('csrftoken');
            axios.defaults.headers.common['X-CSRFToken'] = csrftoken;
        },
        showLoginForm() {
            this.formDisplayStatus = this.consts.DISPLAY_LOGIN;
        },
        showRegisterForm() {
            this.formDisplayStatus = this.consts.DISPLAY_REGISTER;
        },
        hideForms() {
            this.formDisplayStatus = this.consts.DISPLAY_NONE
        },
        submitRegisterForm() {
            this.setCSRFHeader();
            axios
                .post('/accounts/registration/', this.registerForm)
                .then(response => {
                    this.isAuthenticated = true;
                    alert('ثبت نام شما با موفقیت انجام شد');
                })
                .catch(error => {
                    console.log(error);
                });
            this.hideForms();
        },
        submitLoginForm() {
            this.setCSRFHeader();
            // const headers = { 'X-CSRFToken': this.getCSRFToken() };
            // console.log(this.loginForm);
            axios
                .post('/accounts/login/', this.loginForm,)
                .then(response => {
                    this.isAuthenticated = true;
                })
                .catch(error => {
                    console.log(error);
                });
            this.hideForms();
        },
        logout() {
            this.setCSRFHeader();
            axios
                .post('/accounts/logout/')
                .then(response => {
                    this.isAuthenticated = false;
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    template:
    /*html*/
    `
    <ul class="nav p-0 auth-nav">
        <span class='py-2 px-3'><i class='fas fa-link'></i></span>
    
        <template v-if='isAuthenticated'>
            <li class="nav-item">
                <a @click='logout()' class="nav-link">خروج</a>
            </li>
        </template>

        <template v-else>
            <li class="nav-item">
                <a @click='showRegisterForm()' class="nav-link">ثبت نام</a>
            </li>
            <li class="nav-item">
                <a @click='showLoginForm()' class="nav-link">ورود</a>
            </li>
        </template>
    </ul>

    <div v-show='displayOverlay' class='container-fluid overlay'>
        <div @click='hideForms()' class="p-0 m-0 close-btn">&#x2715;</div>
        <div class="card p-3 text-center mx-auto overlay-content">

            <form v-show='formDisplayStatus === consts.DISPLAY_LOGIN' class='text-dark'
                  @submit.prevent='submitLoginForm'>
                <div class='row p-1'>
                    <div class='col-sm-5 text-right px-2'>
                        <label for='login_username'>نام کاربری:</label>
                    </div>
                    <div class='col-sm-7 text-center px-2'>
                        <input id='login_username' type='text' v-model='loginForm.username'>
                    </div>
                </div>
                <div class='row p-1'>
                    <div class='col-sm-5 text-right px-2'>
                        <label for='login_password'>رمز عبور:</label>
                    </div>
                    <div class='col-sm-7 text-center px-2'>
                        <input id='login_password' type='password' v-model='loginForm.password'>
                    </div>
                </div>
                <div class='text-center p-2'>
					<button type='submit' class='btn btn-success py-1 px-3'>
                    ورود
					</button>
				</div>
                <div class='p-0 m-0'>
                    <span>
                        هنوز ثبت نام نکرده اید؟ 
                        <a class='btn btn-link' @click='showRegisterForm()'>ثبت نام</a>
                    </span>
                </div>
            </form>

            <form v-show='formDisplayStatus === consts.DISPLAY_REGISTER' class='text-dark'
                  @submit.prevent='submitRegisterForm'>
                <div class='row p-1'>
                    <div class='col-sm-5 text-right px-2'>
                        <label for='register_username'>نام کاربری:</label>
                    </div>
                    <div class='col-sm-7 text-center px-2'>
                        <input id='register_username' type='text' v-model='registerForm.username'>
                    </div>
                </div>
                <div class='row p-1'>
                    <div class='col-sm-5 text-right px-2'>
                        <label for='register_email'>ایمیل:</label>
                    </div>
                    <div class='col-sm-7 text-center px-2'>
                        <input id='register_email' type='text' v-model='registerForm.email'>
                    </div>
                </div>
                <div class='row p-1'>
                    <div class='col-sm-5 text-right px-2'>
                        <label for='register_password'>رمز عبور:</label>
                    </div>
                    <div class='col-sm-7 text-center px-2'>
                        <input id='register_password' type='password' v-model='registerForm.password'>
                    </div>
                </div>
                <div class='row p-1'>
                    <div class='col-sm-5 text-right px-2'>
                        <label for='register_password_confirm'>تکرار رمز عبور:</label>
                    </div>
                    <div class='col-sm-7 text-center px-2'>
                        <input id='register_password_confirm' type='password' v-model='registerForm.passwordConfirm'>
                    </div>
                </div>
                <div class='text-center p-2'>
					<button type='submit' class='btn btn-success py-1 px-3'>
                    ثبت نام
					</button>
				</div>
                <div class='p-0 m-0'>
                    <span>
                        قبلا ثبت نام کرده اید؟ 
                        <a class='btn btn-link' @click='showLoginForm()'>ورود</a>
                    </span>
                </div>
            </form>
        </div>
    </div>
    `,
});