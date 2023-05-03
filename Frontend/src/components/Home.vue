<template>
  <div class="container-fluid py-5 vh-100 p-0">
    <div class="custom-bg-2 card vh-100 rounded-top-5 shadow-sm m-0 p-0">
      <h4 class="p-4 m-0 text-white text-center text-uppercase">Collect Sample</h4>
      <div class="px-3">
        <div class="mb-3">
          <label for="formGroupExampleInput" class="form-label text-white">Sample No</label>
          <input type="text" class="form-control" id="formGroupExampleInput" placeholder="eg : 0963045">
        </div>
        <div class="mb-3">
          <label for="formGroupExampleInput2" class="form-label text-white">Department</label>
          <select class="form-select">
            <option hidden selected>Select Department</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="formGroupExampleInput2" class="form-label text-white">Origin</label>
          <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="eg : origin">
        </div>
        <div class="mb-3">
          <label for="formGroupExampleInput2" class="form-label text-white">Destination</label>
          <select class="form-select">
            <option hidden selected>Select Destination</option>
          </select>
        </div>
        <div class="my-4">
          <button class="btn btn-success me-3"><i class="fa-solid fa-add"></i> Add Sample</button>
          <button class="btn custom-bg-3 text-white"><i class="fa-solid fa-camera"></i> Scan</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  setup() {

  }
}
</script>