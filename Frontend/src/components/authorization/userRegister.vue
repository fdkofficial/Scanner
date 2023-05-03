<template>
    <section class="body vh-100 w-100">
        <div class="container-fluid glass-morphism">
            <div class="d-flex flex-column g-4 py-5 vh-100 justify-content-center-align-items-center">
                <div class="col text-center">
                    <h3 class="lh-base text-uppercase fw-medium">SIGN UP</h3>
                    <div class="my-3">
                        <div class="form-floating">
                            <input type="email" class="form-control" id="email" placeholder="name@example.com">
                            <label for="floatingInput">First Name</label>
                        </div>
                    </div>
                    <div class="my-3">
                        <div class="form-floating">
                            <input type="email" class="form-control" id="email" placeholder="name@example.com">
                            <label for="floatingInput">Last Name</label>
                        </div>
                    </div>
                    <div class="my-3">
                        <div class="form-floating">
                            <input type="email" class="form-control" id="email" placeholder="name@example.com">
                            <label for="floatingInput">Username</label>
                        </div>
                    </div>
                    <div class="my-3">
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
                    <div class="my-3 custom-bg-3 px-3 rounded-4">
                        <button class="btn btn-transparent w-100 text-white lh-base p-3" @click="$router.push({'name':'home'})">Sign up <i
                            class="fa-solid fa-sign-in"></i></button>
                    </div>
    
                    <div class="text-center">
                        <span>Already a member? <span class="text-primary" @click="$router.push({'name':'user-login'})">Login here</span></span>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
</script>