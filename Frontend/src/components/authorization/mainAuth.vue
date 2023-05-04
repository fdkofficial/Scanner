<template>
    <div class="container-fluid">
        <div class="d-flex flex-column g-4 justify-content-center vh-100 py-3">
            <div class="col vh-100 w-100 rounded-5 custom-bg-4 vector-bg">
                <div class="d-flex h-100 align-items-center justify-content-center">
                    <img src="../../assets/logo.png" class="img-fluid p-3"  alt="">
                </div>
            </div>
            <div class="col vh-100 w-100 px-3">
                <div class="d-flex flex-column align-items-center justify-content-center p-0 m-0 h-100">
                    <h4 class="text-center fw-bold lh-base letter-spacing p-0 m-0">NADDA SCAN</h4>
                    <p class="text-center fs-6 text-muted lh-lg text-justify letter-spacing p-0 m-0">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                    </p>
                    <div class="input-group custom-bg-3 shadow-sm rounded-2 my-3">
                        <button @click="$router.push({'name':'user-login'})" class="btn btn-light input-group-item rounded-0 col-6">Login</button>
                        <button @click="$router.push({'name':'user-register'})" class="btn btn-transparent input-group-item col-6 text-white">Register</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {}
</script>