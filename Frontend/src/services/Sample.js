import axios from 'axios';
import Constants from './constant.js';

var constants = new Constants();

export default class SampleServices {

    async CollectSampleData() {

        const res = await axios({
            url: constants.sample_data,
            headers: {
                "Authorization": constants.token
            },
            method: "GET"
        });
        return res;
    }

    async AddCollectSampleData(data) {

        const res = await axios({
            url: constants.collect_sample_data,
            headers: {
                "Authorization": constants.token
            },
            method: "POST",
            data:data
        });
        return res;
    }
    


async DropSampleData() {

        const res = await axios({
            url: constants.drop_sample_data,
            headers: {
                "Authorization": constants.token
            },
            method: "GET"
        });
        return res;
    }

    async AddDropSampleData(data) {

        const res = await axios({
            url: constants.drop_sample_data,
            headers: {
                "Authorization": constants.token
            },
            method: "POST",
            data:data
        });
        return res;
    }

    

    async Department() {

        const res = await axios({
            url: constants.department,
            headers: {
                "Authorization": constants.token
            },
            method: "GET"
        });
        return res;
    }

    async Laberatory() {

        const res = await axios({
            url: constants.labaratory,
            headers: {
                "Authorization": constants.token
            },
            method: "GET"
        });
        return res;
    }


}
