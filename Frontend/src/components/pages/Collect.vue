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
                                <input @click="sampleData.origin = j" type="checkbox" class="btn-check"
                                    :id="'btn-check-' + j.id" autocomplete="off" data-bs-toggle="modal"
                                    data-bs-target="#UnitsModal">
                                <label class="btn custom-bg-2 pt-2 text-white btn-sm" :for="'btn-check-' + j.id">{{ j.name
                                }}</label>
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
                    <div id="reader" style="width:100%; height:50vh;"></div>
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
                                    <td><button class="btn btn-danger btn-sm" @click="sampleData.sample_no = sampleData.sample_no.filter((val) => val != i)" ><i class="fa-solid fa-trash"></i></button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                    <button type="button" @click="addSampleData" class="btn custom-bg-2 text-white" data-bs-dismiss="modal">Save</button>
                </div>
            </div>
        </div>
        {{ decod }}
    </div>
</template>
<script>
import { Html5QrcodeScanner } from "html5-qrcode";
import { onMounted, ref } from "vue";
import Sample from "../../services/Sample"
export default {
    setup() {
        let sampleData = ref({
            "sample_no": [],
            "origin": {
                name:"",
                id:""
            },
        })

        // const addUnits = (val) => {
        //     if (sampleData.value.origin.filter((fil) => fil == val).length > 0) {
        //         sampleData.value.origin = sampleData.value.origin.filter((fil) => fil != val)
        //         // alert("unselected")
        //     }
        //     else {
        //         sampleData.value.origin.push(val);
        //         // alert("new cal selected")
        //     }
        // }

        let list_departments = ref();
        let list_lab = ref();
        let decod = ref();
        // let selected_unit = ref({});
        const onScanSuccess = (decodedText, decodedResult) => {
            // handle the scanned code as you like, for example:
            // console.log(`Code matched = ${decodedText}`, decodedResult);
            decodedResult;
            // let qr = document.getElementById('CodeScan')
            // qr.innerHTML = decodedText
            decod.value = String(decodedText);
            // alert('-')
            if (sampleData.value.sample_no.filter((val) => val == decod.value ).length >0){
                // alert('Sample Already Exisit')
                decod.value = 'Sample Already Exisit';
            }
            else{
                sampleData.value.sample_no.push(decod.value)
                decod.value = decodedText;
            }
        }

        const listDepartment = () => {
            let data = new Sample();
            data.Department().then((response => {
                // sampleData.value = response.data.data;
                list_departments.value = response.data.data;
            }))
        }

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


        const listLaberatory = () => {
            let data = new Sample();
            data.Laberatory().then((response => {
                list_lab.value = response.data.data;
            }))
        }

        const onScanFailure = (error) => {
            // handle scan failure, usually better to ignore and keep scanning.
            // for example:
            console.warn(`Code scan error = ${error}`);
        }

        onMounted(() => {
            listDepartment();
            listLaberatory();
            let html5QrcodeScanner = new Html5QrcodeScanner("reader", { fps: 10, qrbox: { width: 500, height: 500 } }, /* verbose= */ false);
            html5QrcodeScanner.render(onScanSuccess, onScanFailure);
        })

        const dNone = () => {
            const btn = document.getElementById('html5-qrcode-button-camera-permission')
            btn.click()
            console.log('clicked')
        }

        return {
            onScanSuccess,
            onScanFailure,
            list_departments,
            list_lab,
            // addUnits,
            sampleData,
            listLaberatory,
            addSampleData,
            decod,
            // selected_unit,
            dNone
        }
    }
}
</script>