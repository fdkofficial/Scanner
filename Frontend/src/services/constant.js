// import moment from 'moment';
// import URL from "./url"
class Constants {
    // url = new URL()
    // base_url = this.url.base_url;
    base_url = "http://95.177.178.96:50/";
    // ++++++++++++++++++++++++++++++++++++++++++++++++ NEW LINKS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    token = "Token "+ localStorage.getItem('Token')
    // Global
    logout = this.base_url + 'auth/logout/'
    login = this.base_url + 'auth/login/'
    collect_sample_data = this.base_url + 'collect-sample-data/'
    drop_sample_data = this.base_url + 'drop-sample-data/'
    department = this.base_url + 'department/'
    labaratory = this.base_url + 'labaratory/'
    

}

export default Constants;