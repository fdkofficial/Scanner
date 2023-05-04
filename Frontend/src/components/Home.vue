<template>
  <div class="container-fluid py-5 vh-100 p-0">
    <div class="custom-bg-2 card vh-100 rounded-top-5 shadow-sm m-0 p-0">
      <h4 class="p-4 m-0 text-white text-center text-uppercase">Collect Sample</h4>
      <div class="px-3">
        <div class="mb-3">
          <label for="formGroupExampleInput" class="form-label text-white">Sample No</label>
          <input type="text" class="form-control" v-model="sampleData.sample_no" id="formGroupExampleInput" placeholder="eg : 0963045">
        </div>
        <!-- Department Start here -->
        <div>
          <label class="form-check-label text-white" for="flexSwitchCheckChecked">Department</label>
        </div>
        <!-- Department Accordion -->
        <div class="accordion" id="accordionExample">
          <!-- For loop come here -->
          <div class="accordion-item" v-for="i in list_departments" :key="i">
            <h2 class="accordion-header custom-bg-3 rounded-2">
              <button class="accordion-button shadow-none p-2 custom-bg-3 text-white rounded-2" type="button"
                data-bs-toggle="collapse" data-bs-target="#collapse{id}" aria-expanded="true"
                aria-controls="collapse{id}">
                {{ i }}
              </button>
            </h2>
            <div id="collapse{id}" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
              <div class="accordion-body p-2">
                <div class="d-flex flex-row flex-wrap justify-content-evenly p-0 m-0">
                  <div class="my-2">
                    <input type="checkbox" class="btn-check" id="btn-check-2" autocomplete="off">
                    <label class="btn custom-bg-2 pt-2 text-white btn-sm" for="btn-check-2">Checked</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Destination Chcked button -->
        <div class="m-0 mt-3">
          <label class="form-check-label m-0 p-0 text-white" for="flexSwitchCheckChecked">Destination</label>
        </div>
        <div class="d-flex flex-row flex-wrap justify-content-evenly p-0 m-0">
          <div class="my-2 mx-1">
            <input type="checkbox" class="btn-check" id="destination{id}" autocomplete="off">
            <label class="btn custom-bg-1 pt-2 btn-sm" for="destination{id}">Checked</label>
          </div>
        </div>
        <!-- Drop date -->
        <div class="my-2">
          <label for="drop_date" class="form-label text-white">Drop Date</label>
          <input type="date" class="form-control" id="drop_date" placeholder="eg : 0963045">
        </div>
        <!-- Reciver ID -->
        <div class="my-2">
          <label for="reciver_id" class="form-label text-white">Reciver ID</label>
          <input type="text" class="form-control" id="reciver_id" placeholder="eg : 85665163">
        </div>
        <div class="my-4">
          <button class="btn btn-success me-3"><i class="fa-solid fa-add"></i> Add Sample</button>
          <!-- <button class="btn custom-bg-3 text-white" data-bs-toggle="modal" data-bs-target="#ScannerModal" @click="dNone()"><i
            class="fa-solid fa-camera"></i> Scan</button> -->
            <button class="btn custom-bg-3 text-white" @click="dNone()"><i class="fa-solid fa-camera"></i> Scan</button>
          </div>
        <span id="CodeScan"></span>
        <div id="reader" width="600px"></div>
        <div class="modal fade" id="ScannerModal" tabindex="-1" aria-labelledby="ScannerModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-fullscreen">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="ScannerModalLabel">Code Scanner</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="m-2">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Html5QrcodeScanner } from "html5-qrcode";
import { onMounted,ref } from "vue";
import Sample from "../services/Sample"
export default {
  setup() {
    let sampleData = ref({
      "sample_no" : []
    })
    let list_departments = ref();
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
        list_departments.value = response.data.data
      }))
    }

    const onScanFailure = (error) => {
      // handle scan failure, usually better to ignore and keep scanning.
      // for example:
      console.warn(`Code scan error = ${error}`);
    }
    onMounted(() => {
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
      sampleData,
      dNone
    }
  }
}
</script>