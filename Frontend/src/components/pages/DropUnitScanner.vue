
<template>
    <div class="container-fluid">
        <div class="card">    
            <div id="reader" style="width:auto;"></div>
            <span class="text-danger" v-if="error_msg">{{ error_label }}</span>
        </div>
    </div>
</template>

<script>
import { Quagga } from 'quagga';
import { onMounted } from 'vue'
export default {
    setup() {
        onMounted(() => {
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
                        console.log(last_code);
                        Quagga.stop();
                    });
                });
            }
        })
    },
}
</script>