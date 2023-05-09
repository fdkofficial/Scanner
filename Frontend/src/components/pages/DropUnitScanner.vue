<template>
    <div class="container-fluid p-0">
        <div class="card vh-100 justify-content-between">
            <div class="card-header custom-bg-3">
                <h6 class="text-white m-0 p-0">Scan Drop Destination</h6>
            </div>
            <div class="card-body d-flex align-items-center">
                <div id="reader"></div>
                <span class="text-danger" v-if="error_msg">{{ error_label }}</span>
            </div>
        </div>
    </div>
</template>
<script>
import Quagga from 'quagga';
import { ref, onMounted, onUnmounted } from 'vue';
import router from "../../router"
export default {
    setup() {
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
                        console.log(last_code)
                        router.push({"name":"drop",params:{id:last_code}})
                    });
                });
            }
        }
        onMounted(() => {
            ChangeFunc();
        })
        onUnmounted(() => {            
            try {
                Quagga.stop();
            } catch (error) {
                console.log(error);
            }
        })
        return {
            ChangeFunc,
            error_msg,
            error_label
        }
    },
}
</script>