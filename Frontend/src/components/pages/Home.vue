<template>
  <section class="home_img">
    <div class="d-flex flex-column backdrop vh-100 justify-content-center align-items-center">
      <img src="../../assets/logo.png" class="img-fluid p-5" alt="">
      <button @click="$router.push({'name':'collect'})" class="btn custom-bg-3 text-white w-75 my-3">Collect</button>
      <button @click="$router.push({'name':'drop'})" class="btn custom-bg-2 text-white w-75 my-3">Drop</button>
    </div>
  </section>
</template>