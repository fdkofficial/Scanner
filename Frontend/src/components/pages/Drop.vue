<template>
    <div class="container-fluid">
        <h4 class="p-0 m-0 my-4 lh-lg">Destination</h4>
        <div class="my-4" v-for="lab in list_lab" :key="lab">
            <input type="checkbox" class="btn-check " id="destination{id}" autocomplete="off" data-bs-toggle="modal"
                data-bs-target="#UnitsModal">
            <label @click="sampleData.destination = lab; ChangeFunc()"
                class="btn custom-bg-3 text-white shadow-sm pt-2 btn-sm w-100 rounded-4" for="destination{id}">{{
                    lab.name
                }}</label>
        </div>
        <!-- {{ sampleData }} -->
    </div>
    <!-- Modal -->
    <div class="modal fade" id="UnitsModal" tabindex="-1" aria-labelledby="UnitsModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-fullscreen">
            <div class="modal-content">
                <div class="modal-header custom-bg-3">
                    <h1 class="modal-title fs-5 text-white" id="UnitsModalLabel">Scan Sample</h1>
                    <button type="button" class="btn-close" style="filter:invert(1)" data-bs-dismiss="modal"
                        aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div id="reader" style="width:auto;"></div>
                    <div class="mb-3">
                        <label for="ReciverId" class="form-label">Reciver ID</label>
                        <input type="text" v-model="sampleData.reciever_id" class="form-control" id="ReciverId"
                            placeholder="Reciver Id">
                    </div>
                    <span class="text-danger" v-if="error_msg">{{ error_label }}</span>
                    <div class="mb-3">
                        <table class="table table-bordered table-stripped text-center">
                            <col style="width:25%;">
                            <col style="width:70%;">
                            <col style="width:5%;">
                            <thead>
                                <tr class="custom-bg-3 text-white">
                                    <th>Destination</th>
                                    <th>Sample No</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="i in sampleData.sample_no" :key="i">
                                    <td>{{ sampleData.destination.name }}</td>
                                    <td>{{ i }}</td>
                                    <td><button @click="sampleData.sample_no = sampleData.sample_no.filter((val) => val != i)" class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                    <button type="button" @click="addSampleData" class="btn custom-bg-2 text-white"
                        :data-bs-dismiss="!error_msg ? 'modal' : ''">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { onMounted, ref } from "vue";
import Sample from "../../services/Sample"
import Quagga from 'quagga'
export default {
    setup() {
        let sampleData = ref({
            "sample_no": [],
            "reciever_id": null,
            "destination": {
                name: "",
                id: ""
            },
        })
        let list_departments = ref();
        let list_lab = ref();
        let error_msg = ref(false);
        let error_label = ref();
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
        const listDepartment = () => {
            let data = new Sample();
            data.Department().then((response => {
                // sampleData.value = response.data.data;
                list_departments.value = response.data.data;
            }))
        }
        let decod = ref({})
        const addSampleData = () => {
            let data = new Sample();
            if (!sampleData.value.reciever_id) {
                alert("Please Enter Reciever id")
            }
            else {
                sampleData.value.destination = sampleData.value.destination.id;
                data.AddDropSampleData(sampleData.value).then((response => {
                    if (response.status == 201) {
                        console.log(response.status, '---')
                        // sampleData.value = response.data.data;
                        console.log('saved', response.data)
                        sampleData.value = {
                            "sample_no": [],
                            "destination": {
                                name: "",
                                id: ""
                            },
                        }
                    }
                    else {
                        error_msg.value = true
                        error_label.value = response.data.data
                    }
                }))
            }
        }
        const listLaberatory = () => {
            let data = new Sample();
            data.Laberatory().then((response => {
                list_lab.value = response.data.data;
            }))
        }
        onMounted(() => {
            listDepartment();
            listLaberatory();
        })
        return {
            list_departments,
            list_lab,
            sampleData,
            listLaberatory,
            addSampleData,
            error_msg,
            error_label,
            decod,
            ChangeFunc
        }
    }
}
</script>