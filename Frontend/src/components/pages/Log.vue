<template>
    <div class="container-fluid p-0 table-responsive">
        <table class="table table-stripped table-bordered nowrap">
            <thead>
                <tr class="custom-bg-3 text-white">
                    <th>User</th>
                    <th>Sample No</th>
                    <th>Unit</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="i in logs.logs" :key="i">
                    <td>{{ i.collector_user }}</td>
                    <td><span v-for="j in i.sample_no" :key="j" >{{ j }}, &nbsp;</span></td>
                    <td>{{ i.origin }}</td>
                    <td>{{ i.collect_date }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import { onMounted, ref } from "vue";
import Sample from "../../services/Sample";
export default {
    setup() {
        let logs = ref({
           
        })

        
        // Listing Department
        const listLogs = () => {
            let data = new Sample();
            data.Logs().then((response => {
                // sampleData.value = response.data.data;
                logs.value = response.data.data;
            }))
        }
        
        onMounted(() => {
            
            listLogs();
            
        })
        return {
           logs,
           listLogs
        }
    }
}
</script>