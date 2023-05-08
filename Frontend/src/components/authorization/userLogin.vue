<template>
    <section class="body custom-bg-1 vh-100 w-100">
        <div class="container-fluid glass-morphism">
            <div class="d-flex g-4 py-5 vh-100 justify-content-center align-items-center">
                <div class="col text-center">
                    <h3 class="lh-base text-uppercase fw-medium">As-salamu alaykum!</h3>
                    <p class="lh-base text-muted small px-4 fw-bold custom-text">Welcome back, Login to continue </p>
                    <div class="my-3 mt-5">
                        <span class="text-danger" v-if="error_msg">Error Invalid Credentials</span>
                        <div class="form-floating">
                            <input v-model="user.username" type="text" class="form-control" id="email"
                                placeholder="name@example.com">
                            <label for="floatingInput">Username</label>
                        </div>
                    </div>
                    <div class="my-3">
                        <div class="form-floating">
                            <input @click="error_msg = false" v-model="user.password" type="password" class="form-control"
                                id="floatingPassword" placeholder="Password">
                            <label for="floatingPassword">Password</label>
                        </div>
                    </div>
                    <div class="text-end">
                        <span>Forget Password ?</span>
                    </div>
                    <div class="my-3 custom-bg-3 px-3 rounded-4">
                        <button class="btn btn-transparent w-100 text-white lh-base p-3" @click="LoginUSer">Sign in <i
                                class="fa-solid fa-sign-in"></i></button>
                    </div>
                    <!-- <div class="text-center">
                        <span>Not a member? <span class="text-primary"
                                @click="$router.push({ 'name': 'user-register' })">Register now</span></span>
                    </div> -->
                </div>
            </div>
        </div>
    </section>
</template>
<script>
import AuthServices from '../../services/AuthServices';
// import ref from "vue"
import { ref,onMounted } from 'vue';
import router from '../../router';
export default {
    setup() {
        let user = ref({})
        let error_msg = ref(false)
        let token = ref('')
        const LoginUSer = () => {
            let login = new AuthServices();
            login.getAuthRequests(user.value).then((response) => {
                if (response.data.token) {
                    localStorage.setItem('CPT_Token', response.data.token)
                    token.value = response.data
                    router.push({ 'name': 'home' })
                }
                else {
                    error_msg.value = true
                }
            })
            // router.push({'name':'home'})
        }
        let key = ref()
        onMounted(() => {
            key.value = localStorage.getItem('CPT_Token')
            if (key.value) {
                router.push({ 'name': 'home' })
            }
        })
        return {
            user,
            LoginUSer,
            token,
            error_msg
        }
    }
}
</script>