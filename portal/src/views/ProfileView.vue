<!-- <script>

const API_URL = import.meta.env.VITE_API_URL

export default {
  name: 'ProfileView',
  methods: {
    async function makeRequestWithJWT(){
      const options = {
        method: 'post',
        credentials: 'same-origin',
        headers: {
          'X-CSRF-TOKEN': getCookie('csrf_access_token'),
        },
      };
      const response = await fetch(API_URL+'/me/profile', options);
      const result = await response.json();
      return result;
    }
  }
}
</script> -->

<template>
  <div >
    <h1> PROFILE </h1>
  </div>
</template>
