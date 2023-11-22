<script>
export default {
  name: 'NoteCard',
  props: {
    note: {
      type: Object
    }
  }
}
</script>

<template>
  <div class="card mb-2">
    <div class="card-body">
      <h6 class="card-subtitle mb-2 text-body-secondary">
        {{ note.user.first_name }} {{ note.user.last_name }} ( {{ note.user.email }} )
      </h6>
      <p class="card-text">
        {{ note.text }}
      </p>
      <h6 class="card-subtitle mb-2 text-body-secondary text-end">
        {{ note.inserted_at }} 
      </h6>
    </div>
  </div>
</template>
