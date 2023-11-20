<script>
export default {
  name: 'InstitutionInfo',
  props: {
    institution: {
      type: Object
    }
  }
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h2 class="card-title">{{ institution.name }}</h2>
      <h6 class="card-subtitle mb-2 text-body-secondary">{{ institution.location }}</h6>

      <div class="pb-2 col justify-start align-center">
        <p class="card-text">
          <b> Información:</b>
          <br />
          {{ institution.information }}
        </p>
        <p class="card-text">
          <b> Días y horarios de atención:</b>
          <br />
          {{ institution.days_and_opening_hours }}
        </p>
      </div>

      <div class="pb-2 col justify-start align-center">
        <p class="card-text">
          <b> Sitio web:</b>
          <br />
          {{ institution.web }}
        </p>
        <p class="card-text">
          <b> Mail de contacto:</b>
          <br />
          {{ institution.email }}
        </p>
      </div>
    </div>
  </div>
</template>
