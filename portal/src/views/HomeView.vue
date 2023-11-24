<script>
import { ref, watch, onBeforeMount } from 'vue'
import { fetchWrapper } from '@/helpers/fetch-wrapper'
import { useAuthStore } from '@/stores/auth'
const API_URL = import.meta.env.VITE_API_URL

export default {
  setup() {
    const contact_info = ref(null)
    const authStore = useAuthStore()
    const profile = ref([])

    onBeforeMount(async () => {
      const response = await fetchWrapper.get(API_URL + '/contact-info')
      contact_info.value = response.contact_info
      if (authStore.user) {
        profile.value = JSON.parse(localStorage.getItem('user')).profile
      }
    })

    watch(authStore, () => {
      if (authStore.user) {
        profile.value = JSON.parse(localStorage.getItem('user')).profile
      }
    })

    return {
      contact_info,
      authStore,
      profile
    }
  }
}
</script>

<template>
  <main class="container">
    <div class="d-flex flex-column flex-lg-row gap-4 justify-content-start">
      <div class="col">
        <div class="card text-start p-4 bg-light w-100">
          <div v-if="!authStore.user">
            <h3 class="mb-4">Bienvenido al sitio de CIDEPINT</h3>
            <p class="card-text">
              ¡Te damos la bienvenida al Portal de CIDEPINT! Aquí podrás acceder a información
              relevante sobre el Laboratorio, información Institucional y servicios habilitados.
            </p>
          </div>
          <h3 v-else>
            {{ profile.gender === 'Femenino' ? 'Bienvenida' : 'Bienvenido' }}
            {{ profile.first_name }} {{ profile.last_name }} al sitio de CIDEPINT
          </h3>
          <p style="margin-top: 10px">En este portal, podrás:</p>
          <ul class="list px-4">
            <li class="list-item">Ver todos los servicios que prestan nuestras instituciones</li>
            <li class="list-item">Buscar un servicio específico</li>
            <li class="list-item">
              Visualizar la sección de análisis de datos, donde podrás ver:
              <ul class="list">
                <li class="list-item">Cantidad de solicitudes realizadas agrupadas por estado</li>
                <li class="list-item">Ranking de los servicios más solicitados</li>
                <li class="list-item">
                  Top 10 de las instituciones con el mejor tiempo de resolución.
                </li>
              </ul>
            </li>
          </ul>
          <p class="list-item">
            <b>{{ !authStore.user ? 'Regístrate como usuario para:' : 'Además, ahora puedes:' }}</b>
          </p>
          <ul class="list">
            <li class="list-item">Solicitar un servicio</li>
            <li class="list-item">Ver tus solicitudes</li>
            <li class="list-item">Detalles del Pedido</li>
            <li class="list-item">Ver y agregar notas a los pedidos</li>
          </ul>
        </div>
      </div>
      <div class="col">
        <div class="card text-start p-4 bg-light" id="contact">
          <h3>Información de contacto</h3>
          <p class="card-text">
            ¡Nos encantaría escucharte! Ponte en contacto para cualquier consulta o comentario.
          </p>
          <p class="card-text">
            <strong>{{ contact_info }}</strong>
          </p>
        </div>
        <div class="card text-start p-4 mt-4 bg-light">
          <h4 class="mb-3 text-muted">Información Adicional:</h4>
          <p class="card-text">
            En la actualidad, CIDEPINT es una institución que depende del sistema
            <b>CICPBA-CONICET-UNLP</b> y ha ampliado considerablemente su campo de experiencia.
          </p>
          <p class="card-text">
            El centro cuenta con personal capacitado en el desarrollo y caracterización de pinturas
            anticorrosivas y decorativas, antiincrustantes, con propiedades antifúngicas, entre
            otras con aplicaciones específicas.
          </p>
          <p class="card-text">
            Además, se han incorporado líneas de trabajo en el área de pretratamientos de aceros,
            biodeterioro de materiales estructurales, inhibición de la corrosión, galvanoplastía y
            siderurgia. Muchas de estas líneas se enfocan en la obtención de alternativas ecológicas
            que reduzcan el impacto de la industria sobre el medio ambiente.
          </p>
          <h4 class="mb-3 text-muted">Compromiso Ambiental:</h4>
          <p class="card-text">
            CIDEPINT está comprometido con la investigación y desarrollo de soluciones que
            contribuyan a la sostenibilidad ambiental. Nuestro objetivo es ofrecer alternativas que
            minimicen el impacto de las actividades industriales en el medio ambiente.
          </p>
          <h4 class="mb-3 text-muted">Colaboración y Proyectos:</h4>
          <p class="card-text">
            Fomentamos la colaboración con otras instituciones y participamos en proyectos de
            investigación a nivel nacional e internacional. Estamos dedicados a avanzar en el
            conocimiento y la innovación en el ámbito de la protección y tratamiento de materiales.
          </p>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
}

#contact {
  max-height: 200px;
}
</style>
