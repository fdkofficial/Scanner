// import moment from 'moment';
import URL from "./url"
class Constants {
    url = new URL()
    base_url = this.url.base_url;
    // ++++++++++++++++++++++++++++++++++++++++++++++++ NEW LINKS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    token = "Token "+ 'f4f5ec52ba61ac099f8571e940aadb479cb50af0'
    // Global
    logout = this.base_url + 'auth/login/'
    login = this.base_url + 'auth/logout/'
    

}

export default Constants;