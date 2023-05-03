<template class="body">
    <section class="body vh-100 w-100">
        <div class="container-fluid glass-morphism">
            <div class="d-flex flex-column g-4 py-5 vh-100 justify-content-center-align-items-center">
                <div class="col text-center">
                    <h3 class="lh-base text-uppercase fw-medium">As-salamu alaykum!</h3>
                    <p class="lh-base text-muted small px-4 fw-normal">Welcome Back Let's know About Islam And The Holy
                        Qur'aan
                    </p>
                    <div class="my-3 mt-5">
                        <div class="form-floating">
                            <input type="email" class="form-control" id="email" placeholder="name@example.com">
                            <label for="floatingInput">Email Address</label>
                        </div>
                    </div>
                    <div class="my-3">
                        <div class="form-floating">
                            <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                            <label for="floatingPassword">Password</label>
                        </div>
                    </div>
                    <div class="text-end">
                        <span>Forget Password ?</span>
                    </div>
                    <div class="my-3 custom-bg-3 px-3 rounded-4">
                        <button class="btn btn-transparent w-100 text-white lh-base p-3"
                            @click="$router.push({ 'name': 'home' })">Sign in <i class="fa-solid fa-sign-in"></i></button>
                    </div>
                    <div class="position-relative">
                        <span class="text-muted line">or continue with</span>
                    </div>
                    <div class="text-center my-4 col">
                        <img src="https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-webinar-optimizing-for-success-google-business-webinar-13.png"
                            width="40" height="40" class="img-fluid p-1 rounded-2 border" alt="">
                    </div>
                    <div class="text-center">
                        <span>Not a member? <span class="text-primary"
                                @click="$router.push({ 'name': 'user-register' })">Register now</span></span>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
</script>