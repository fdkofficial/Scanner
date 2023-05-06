<template>
    <div class="container-fluid">
        <h4 class="p-0 m-0 my-4 lh-lg">Destination</h4>
        <div class="my-4" v-for="lab in list_lab" :key="lab">
            <input type="checkbox" class="btn-check " id="destination{id}" autocomplete="off" data-bs-toggle="modal"
                data-bs-target="#UnitsModal">
            <label class="btn custom-bg-3 text-white shadow-sm pt-2 btn-sm w-100 rounded-4" for="destination{id}">{{
                lab.name
            }}</label>
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
                    <div class="mb-3">
                        <label for="ReciverId" class="form-label">Reciver ID</label>
                        <input type="text" class="form-control" id="ReciverId" placeholder="Reciver Id">
                    </div>
                    <div class="mb-3">
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
                                <tr>
                                    <td>Unit</td>
                                    <td>Sample No</td>
                                    <td><button class="btn btn-danger btn-sm"><i class="fa-solid fa-trash"></i></button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn custom-bg-2 text-white">Save changes</button>
                </div>
            </div>
        </div>
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
            "origin": [],
        })

        const addUnits = (val) => {
            if (sampleData.value.origin.filter((fil) => fil == val).length > 0) {
                sampleData.value.origin = sampleData.value.origin.filter((fil) => fil != val)
                // alert("unselected")
            }
            else {
                sampleData.value.origin.push(val);
                // alert("new cal selected")
            }
        }

        let list_departments = ref();
        let list_lab = ref();
        const onScanSuccess = (decodedText, decodedResult) => {
            // handle the scanned code as you like, for example:
            console.log(`Code matched = ${decodedText}`, decodedResult);
            let qr = document.getElementById('CodeScan')
            qr.innerHTML = decodedText
            sampleData.value.sample_no.push(decodedText)
        }

        const listDepartment = () => {
            let data = new Sample();
            data.Department().then((response => {
                list_departments.value = response.data.data;
            }))
        }

        const addSampleData = () => {
            let data = new Sample();
            data.PostSampleData().then((response => {
                list_departments.value = response.data.data;
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
            let html5QrcodeScanner = new Html5QrcodeScanner(
                "reader",
                { fps: 10, qrbox: { width: 400, height: 179 } },
      /* verbose= */ false);
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
            addUnits,
            sampleData,
            listLaberatory,
            dNone
        }
    }
}
</script>