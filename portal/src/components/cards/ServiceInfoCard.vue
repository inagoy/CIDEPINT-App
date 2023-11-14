<script>
export default {
  props: {
    service: {
      type: Object
    }
  },
  setup(props) {
    console.log(props.foo)
  }
}
</script>

<template>
  <div class="card mb-4">
    <div class="card-body">
      <h4 class="card-subtitle">
        <span class="badge bg-info text-light y-1"> {{ service.service_type }}</span>
      </h4>
      <h2 class="card-title">
        {{ service.name }}
      </h2>
      <h6 class="card-subtitle mb-2 text-body-secondary">Laboratorio: {{ service.laboratory }}</h6>

      <div class="pb-2 col justify-start align-center">
        <p class="card-text">
          <b> Descripción:</b>
          <br />
          {{ service.description }}
        </p>
        <p class="card-text">
          <b> Palabras clave:</b>
          <br />
          {{ service.keywords }}
        </p>
      </div>
    </div>
  </div>
</template>
