app.component('urls-table', {
    data() {
        return {
            urls: [],
            currentPage: 1,
            pageSize: null,
            totalPages: null,
            loading: true
        }
    },
    props: ['host'],
    computed: {
        hasPrevious() {
            return this.currentPage > 1;
        },
        hasNext() {
            return this.currentPage < this.totalPages;
        }
    },
    watch: {
        currentPage(page) {
            this.updateURLs();
        }
    },
    methods: {
        toPersian(str) {
            newStr = str.toString();
            en_to_fa = ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹'];
            for (let i = 0; i < 10; i++) {
                newStr = newStr.replace(new RegExp(i, 'g'), en_to_fa[i]);
            }
            return newStr;
        },
        shortenedAddress(slug) {
            return this.host + 'shortener/url-redirect/' + slug;
        },
        updateURLs() {
            axios
                .get('/shortener/urls?page='+ this.currentPage + '&sort=+visits')
                .then(response => {
                    this.urls = response.data.results;
                    this.totalPages = response.data.total_pages;
                    this.pageSize = response.data.page_size;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        updateCurrentPage(page) {
            this.currentPage = page;
        }
    },
    mounted() {
        this.updateURLs();
    },
    template:
    /*html*/
    `
    <div class='container text-center'>
        <button v-if='!urls.length' class="btn btn-primary m-3">
            در حال بارگذاری...
            <span class="spinner-border spinner-border-sm"></span>
        </button>

        <table v-else class='table table-bordered table-responsive-sm 
            table-sm table-light table-striped text-center shadow'>
            <thead class='thead-dark'>
                <tr>
                    <th>ردیف</th>
                    <th>عنوان</th>
                    <th>آدرس کوتاه شده</th>
                    <th>تعداد بازدید</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for='(url, index) in urls'>
                    <td>{{ toPersian(pageSize*(currentPage-1) + index + 1) }}</td>
                    <td>{{ url.label }}</td>
                    <td><a :href='shortenedAddress(url.slug)'>{{ shortenedAddress(url.slug) }}</a></td>
                    <td>{{ toPersian(url.visits) }}</td>
                </tr>
            </tbody>
        </table>

        <ul v-if='totalPages > 0' class="pagination justify-content-center flex-row-reverse flex-wrap p-0">
            <li :class="{'page-item':true, 'disabled':!hasPrevious}">
                <a class="page-link" @click='updateCurrentPage(currentPage-1)'>قبلی &#187;</a>
            </li>
            
            <li v-for='index in totalPages' :class="{'page-item':true, 'active':(index === currentPage)}">
                <a class="page-link" @click='updateCurrentPage(index)'>{{ toPersian(index) }}</a>
            </li>
            
            <li :class="{'page-item':true, 'disabled':!hasNext}">
                <a class="page-link" @click='updateCurrentPage(currentPage+1)'>&#171; بعدی</a>
            </li>
        </ul>
    </div>
    `
});