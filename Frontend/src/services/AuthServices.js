import axios from 'axios';
import Constants from './constant.js';

var constants = new Constants();

export default class AuthServices {

    async logout() {
        var _data = {
        }
        const res = await axios({
            url: constants.logout,
            method: "GET",
            data: _data
        });
        localStorage.removeItem('scanner_token')
        localStorage.removeItem('user_id')
        localStorage.removeItem('full_name')
        localStorage.removeItem('userType')
        return res;
    }

    async getAuthRequests(data) {
        // console.log(_data.type.type,'=====')
        const res = await axios({
            url: constants.login,
            method: "POST",
            data: data
        });
        return res;
    }

    async getUser() {
        const res = await axios.get(constants.getUser, {
          headers: {
            "Authorization": constants.token
          }
        });
        return res.data;
      }
}
