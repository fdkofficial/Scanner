<template>
    <div class="container-fluid p-0">
        <div class="card vh-100 p-0 m-0">
            <div class="card-header p-0">
                <h4 class="p-0 px-2 m-0 lh-lg">Scan Sample</h4>
            </div>
            <div class="card-body p-0 m-0">
                <div id="reader" style="width:auto;"></div>
                <span class="text-danger" v-if="error_msg">{{ error_label }}</span>
                <div class="my-2 mx-2">
                    <div class="form-check form-switch">
                        <input @change="sampleData.took_a_round = !sampleData.took_a_round" class="form-check-input"
                            type="checkbox" role="switch" id="flexSwitchCheckDefault">
                        <label class="form-check-label" for="flexSwitchCheckDefault">Took a round</label>
                    </div>
                </div>
                <div class="vh-50 table-responsive my-3">
                    <table class="table table-bordered table-stripped text-center m-0 vh-30">
                        <col style="width:30%;">
                        <col style="width:65%;">
                        <col style="width:5%;">
                        <thead>
                            <tr class="custom-bg-3 text-white">
                                <th>Unit</th>
                                <th>Sample No</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="i in sampleData.sample_no" :key="i">
                                <td>{{ sampleData.origin.name }}</td>
                                <td>{{ i }}</td>
                                <td><button class="btn btn-danger btn-sm"
                                        @click="sampleData.sample_no = sampleData.sample_no.filter((val) => val != i)"><i
                                            class="fa-solid fa-trash"></i></button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="card-footer text-end">
                <button class="btn btn-primary mx-2" @click="addSampleData">Save</button>
                <button class="btn btn-secondary" @click="$router.push({ 'path': '/' })">Close</button>
            </div>
        </div>
    </div>
</template>
<script>
import router from "../../router";
import { onMounted, onUnmounted, ref } from "vue";
import { useRoute } from "vue-router";
import Sample from "../../services/Sample"
import Quagga from 'quagga'
export default {
    setup() {
        // Declaration
        let sampleData = ref({
            "sample_no": [],
            "took_a_round": false,
            "origin": { name: "", id: "" },
        });
        let list_departments = ref();
        let error_msg = ref(false);
        let error_label = ref();
        let list_lab = ref();
        let decod = ref();
        let unit = ref()
        // Scaning Part
        const ChangeFunc = () => {
            if (navigator.mediaDevices && typeof navigator.mediaDevices.getUserMedia === 'function') {
                Quagga.init({
                    inputStream: {
                        name: "Live",
                        type: "LiveStream",
                        width: 0,
                        target: document.querySelector('#reader')
                    },
                    decoder: {
                        readers: ["code_128_reader"]
                    },
                    constraints: {
                        facingMode: "environment",
                        frameRate: {
                            ideal: 10,
                            max: 15
                        },
                        focusMode: "manual"
                    },
                }, function (err) {
                    if (err) {
                        error_msg.value = true;
                        error_label.value = err
                        setTimeout(() => {
                            error_msg.value = false;
                        }, 2000);
                        return
                    }
                    console.log("Initialization finished. Ready to start");
                    Quagga.start();
                    Quagga.onDetected(function (result) {
                        var last_code = result.codeResult.code;
                        if (sampleData.value.sample_no.filter((val) => val == last_code).length > 0) {
                            error_msg.value = true;
                            error_label.value = 'Sample Already Exisit';
                            setTimeout(() => {
                                error_msg.value = false;
                            }, 2000);
                        }
                        else {
                            error_msg.value = false;
                            sampleData.value.sample_no.push(last_code)
                            decod.value = last_code;
                        }
                    });
                });
            }
        }
        // Listing Department
        const listDepartment = () => {
            let data = new Sample();
            data.Department().then((response => {
                // sampleData.value = response.data.data;
                list_departments.value = response.data.data;
            }))
        }
        onUnmounted(() => {
            Quagga.stop();
        })
        // Adding sample
        const addSampleData = () => {
            let data = new Sample();
            sampleData.value.origin = sampleData.value.origin.id;
            data.AddCollectSampleData(sampleData.value).then((response => {
                // sampleData.value = response.data.data;
                console.log('saved', response.data)
                Quagga.stop();
                router.push({ path: '/' })
                sampleData.value = {
                    "sample_no": [],
                    "origin": '',
                }
            }))
        }
        // Listing library
        const listUnits = () => {
            let data = new Sample();
            data.Units(unit.value).then((response => {
                sampleData.value.origin = response.data.data;
                console.log(sampleData.value.origin, response.data)
            }))
        }
        onMounted(() => {
            const {
                params: { id },
            } = useRoute();
            unit.value = id;
            ChangeFunc();
            listDepartment();
            listUnits();
            try {
                Quagga.stop();
            } catch (error) {
                console.log(error);
            }
        })
        return {
            list_departments,
            list_lab,
            sampleData,
            addSampleData,
            decod,
            ChangeFunc,
            error_msg,
            error_label
        }
    }
}
</script>
<style>
.vh-30 {
    height: 30vh;
    overflow-y: scroll;
}
</style>