<template>
    <div class="m-2">
        <div id="reader" width="600px"></div>
    </div>
</template>
<script>
import { Html5QrcodeScanner } from "html5-qrcode";
import { onMounted } from "vue";
export default {
    setup() {
        const onScanSuccess = (decodedText, decodedResult) => {
            // handle the scanned code as you like, for example:
            console.log(`Code matched = ${decodedText}`, decodedResult);
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
        return {
            onScanSuccess,
            onScanFailure
        }
    }
}
</script>