<script setup>
const profile = JSON.parse(localStorage.getItem('user')).profile;
</script>

<template>
  <main class="container">
    <h1 class="mb-4"> Perfil </h1>
    <div class="card mb-4">
      <div class="card-body">
        <div class="row">
          <div class="col-sm-3">
            <p class="mb-0">Nombre Completo</p>
          </div>
          <div class="col-sm-9">
            <p class="text-muted mb-0">{{ profile.first_name }} {{ profile.last_name }}</p>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <p class="mb-0">Email</p>
          </div>
          <div class="col-sm-9">
            <p class="text-muted mb-0">{{ profile.email }}</p>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <p class="mb-0">Teléfono</p>
          </div>
          <div class="col-sm-9">
            <p class="text-muted mb-0"> {{ profile.phone_number }} </p>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <p class="mb-0"> {{ profile.document_type }}</p>
          </div>
          <div class="col-sm-9">
            <p class="text-muted mb-0">{{ profile.document_number }}</p>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <p class="mb-0">Dirección</p>
          </div>
          <div class="col-sm-9">
            <p class="text-muted mb-0"> {{ profile.address }}</p>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-sm-3">
            <p class="mb-0">Género</p>
          </div>
          <div class="col-sm-9">
            <p class="text-muted mb-0"> {{ profile.gender }}</p>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
