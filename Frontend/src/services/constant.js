// import moment from 'moment';
// import URL from "./url"
class Constants {
    // url = new URL()
    // base_url = this.url.base_url;
    base_url = "http://127.0.0.1:8000/";
    // ++++++++++++++++++++++++++++++++++++++++++++++++ NEW LINKS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    token = "Token "+ localStorage.getItem('Token')
    // Global
    logout = this.base_url + 'auth/logout/'
    login = this.base_url + 'auth/login/'
    sample_data = this.base_url + 'sample-data/'
    department = this.base_url + 'department/'
    labaratory = this.base_url + 'labaratory/'
    

}

export default Constants;