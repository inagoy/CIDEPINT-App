<script>
import router from '@/router'
import { fetchWrapper } from '@/helpers/fetch-wrapper'

const API_URL = import.meta.env.VITE_API_URL

export default {
  name: 'ServiceRequestForm',
  props: {
    serviceID: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      message: '',
      title: '',
      files: []
    }
  },
  computed: {
    disableButton() {
      return this.message.length === 0 || this.title.length === 0
    }
  },
  methods: {
    async onSubmit() {
      console.log('entre aca', parseInt(this.serviceID), this.title, this.message)
      console.log('url', `${API_URL}/me/requests/`)
      const request = await fetchWrapper.post(`${API_URL}/me/requests/`, {
        service_id: parseInt(this.serviceID),
        title: this.title,
        description: this.message
      })
      console.log('request: ', request)
      router.push('/requests')
    }
  }
}
</script>
<template>
  <form>
    <div class="mb-3">
      <label for="requestTitleInput" class="form-label"> Título de la solicitud *</label>
      <input class="form-control" v-model="title" type="text" id="requestTitleInput" />
      <label for="requestDetailInput" class="form-label"> Resumen del trabajo a solicitar *</label>
      <textarea
        required
        for="id"
        class="form-control"
        v-model="message"
        placeholder="Resumen..."
        aria-describedby="requestDetailHelp"
      ></textarea>
      <div v-show="disableButton" id="requestDetailHelp" class="form-text">
        Complete todos los datos para solicitar el servicio
      </div>
    </div>

    <div class="d-flex justify-content-end gap-2">
      <button :disabled="disableButton" @click="onSubmit" type="button" class="btn btn-success">
        Solicitar
      </button>
      <button type="dismiss" class="btn btn-secondary">Cancelar</button>
    </div>
  </form>
</template>
