<template>
    <div class="container-fluid">
        <h4 class="p-0 px-3 m-0 my-4 lh-lg">Department</h4>
        <div class="accordion" id="accordionExample">
            <!-- For loop come here -->
            <div class="accordion-item my-5" v-for="(i, index) in list_departments" :key="index">
                <h2 class="accordion-header custom-bg-3 rounded-2">
                    <button
                        :class="index == 0 ? 'accordion-button shadow-none p-2 custom-bg-3 text-white rounded-2' : 'accordion-button shadow-none p-2 custom-bg-3 text-white rounded-2 collabsed'"
                        type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse' + index" aria-expanded="true"
                        aria-controls="collapse{id}">
                        {{ i.name }}
                    </button>
                </h2>
                <div :id="'collapse' + index"
                    :class="index == 0 ? 'accordion-collapse collapse show' : 'accordion-collapse collapse'"
                    data-bs-parent="#accordionExample">
                    <div class="accordion-body p-2">
                        <div class="d-flex flex-row flex-wrap justify-content-evenly gap-2 p-0 m-0">
                            <div class="my-2" v-for="j in i.units" :key="j">
                                <input @click="sampleData.origin = j; ChangeFunc()" type="checkbox" class="btn-check"
                                    :id="'btn-check-' + j.id" autocomplete="off" data-bs-toggle="modal"
                                    data-bs-target="#UnitsModal">
                                <label class="btn custom-bg-2 pt-2 text-white btn-sm" :for="'btn-check-' + j.id">{{
                                    j.name }}</label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
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
                    <span class="text-danger" v-if="error_msg">{{ error_label }}</span>
                    <div class="table-responsive my-3">
                        <table class="table table-bordered table-stripped text-center">
                            <col style="width:25%;">
                            <col style="width:70%;">
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
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                    <button type="button" @click="addSampleData" class="btn custom-bg-2 text-white"
                        data-bs-dismiss="modal">Save</button>
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
            "origin": {
                name: "",
                id: ""
            },
        })

        let list_departments = ref();
        let error_msg = ref(false);
        let error_label = ref();
        let list_lab = ref();
        let decod = ref();
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
                        error_label.value = err;
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
        // Adding sample
        const addSampleData = () => {
            let data = new Sample();
            sampleData.value.origin = sampleData.value.origin.id;
            data.AddCollectSampleData(sampleData.value).then((response => {
                // sampleData.value = response.data.data;
                console.log('saved', response.data)
                sampleData.value = {
                    "sample_no": [],
                    "origin": '',
                }
            }))
        }
        // Listing library
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
            decod,
            ChangeFunc,
            error_msg,
            error_label
        }
    }
}
</script>