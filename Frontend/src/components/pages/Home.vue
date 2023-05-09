<template>
  <section class="home_img">
    <div class="d-flex flex-column backdrop vh-100 justify-content-center align-items-center">
      <img src="../../assets/logo.png" class="img-fluid p-5" alt="">
      <button @click="$router.push({ 'name': 'collect-unit-scanner' })" class="btn custom-bg-3 text-white w-75 my-3">Collect</button>
      <button @click="$router.push({ 'name': 'drop-unit-scanner' })" class="btn custom-bg-2 text-white w-75 my-3">Drop</button>
      <button @click="logout" class="btn danger text-white w-75 my-3">Logout</button>
    </div>
  </section>
</template>
<script>
import { ref, onMounted } from 'vue';
import router from '../../router';
export default {
  setup() {
    let key = ref()
    const logout = () =>{
      localStorage.removeItem('CPT_Token')
      router.push({name:'user-login'})
    }
    onMounted(() => {
      key.value = localStorage.getItem('CPT_Token')
      if (!key.value) {
        router.push({ 'name': 'user-login' })
      }
    })
    return{
      key,
      logout
    }
  }
}
</script>