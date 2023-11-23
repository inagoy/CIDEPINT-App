<script>
import { fetchWrapper } from '@/helpers/fetch-wrapper'
import NoteCard from '../cards/NoteCard.vue'

const API_URL = import.meta.env.VITE_API_URL

export default {
  props: {
    request: {
      type: Object
    }
  },
  components: {
    NoteCard
  },
  data() {
    return {
      isCollapseOpen: false,
      notes: [],
      noteText: ''
    }
  },
  methods: {
    toggleCollapse() {
      this.isCollapseOpen = !this.isCollapseOpen
      if (this.isCollapseOpen && this.notes.length === 0) {
        this.getNotes()
      }
    },
    async getNotes() {
      const request = await fetchWrapper.get(`${API_URL}/me/requests/${this.request.id}/notes`)
      this.notes = request.data
      console.log('notes:', this.notes)
    },
    async addNote() {
      await fetchWrapper.post(`${API_URL}/me/requests/${this.request.id}/notes`, {
        text: this.noteText,
        user_id: this.request.user_id
      })
      this.noteText = ''
      await this.getNotes()
    }
  }
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h6 class="card-subtitle mb-2 text-body-secondary">
        Servicio: {{ request.service.name }}
      </h6>
      <h5 class="card-title">
        {{ request.title }} <span class="badge bg-secondary ms-2"> {{ request.status }}</span>
      </h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">
        Fecha de creación: {{ request.creation_date }}
      </h6>
      <p class="card-text">
        {{ request.description }}
      </p>
      <div class="d-inline-flex gap-1 mb-2">
        <button class="btn btn-primary" type="button" @click="toggleCollapse">Ver notas</button>
      </div>
      <div v-show="isCollapseOpen" class="container">
        <h6 class="text-muted card-text mb-2 mt-2" v-if="notes.length === 0">No hay notas</h6>
        <div class="" v-for="note in notes" :key="note.id">
          <NoteCard :note="note" />
        </div>
        <div class="w-100 d-inline-flex flex-column gap-1 mb-2 mt-2">
          <textarea v-model="noteText" class="form-control" placeholder="Añadir nota"></textarea>
          <button
            :disabled="noteText.length === 0"
            class="btn btn-primary"
            type="button"
            @click="addNote"
          >
            Añadir nota
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
