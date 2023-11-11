<script setup>
const props = defineProps({
  service: {
    type: Object
  }
})

console.log(props.foo)
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">
        {{ service.name }} <span class="badge bg-secondary"> {{ service.service_type }}</span>
      </h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">{{ service.laboratory }}</h6>
      <p class="card-text">
        {{ service.description }}
      </p>
      <p class="card-text">
        {{ service.keywords }}
      </p>
      <button class="btn btn-primary" :disabled="!service.enabled">Solicitar servicio</button>
    </div>
  </div>
</template>
