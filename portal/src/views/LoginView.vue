<script>
  import axios from 'axios'
  
  const API_URL = import.meta.env.VITE_API_URL

  export default {
    name: 'LoginView',
    data() {
      return {
        email: '',
        password: ''
      }
    },
    methods: {
      async handleSubmit() {
        const response = await axios.post(API_URL+'/auth', {
          user: this.email,
          password: this.password
        })
        console.log(response)
      }
    }
  }
</script>


<template>
  <main class="container">
    <div class="row align-items-center">
      <div class="col-6 mx-auto">
        <div class="card-login">
          <div class="card-body text-center" style="margin:0">
            <div class="d-flex">
              <div class="align-self-start">
                <RouterLink to="/"><i class="bi bi-arrow-left"></i></RouterLink>
              </div>
              <div class="col text-center">
                <i class="bi bi-person-circle" style="font-size: 4rem;"></i>
              </div>
            </div>
            <h4 class="card-title">Bienvenido a CIDEPINT</h4>
            <hr>
            <form @submit.prevent="handleSubmit()">
              <div class="form-group-login">
                <label for="inputEmail">Dirección de email</label>
                <input
                  name="inputEmail"
                  required
                  type="email"
                  class="form-control"
                  id="inputEmail"
                  v-model="email"
                  aria-describedby="emailHelp"
                  placeholder="nombre@ejemplo.com"
                />
                <small id="emailError" class="form-text text-danger"></small>
              </div>
              <div class="form-group-login">
                <label for="inputPassword">Contraseña</label>
                <input 
                  name="inputPassword" 
                  required type="password" 
                  v-model="password" 
                  class="form-control" 
                  id="inputPassword" 
                  />
              </div>
              <small id="loginError" class="form-text text-danger"></small>
              <button class="btn btn-primary mb-4">Iniciar Sesión</button>
            </form>
          </div>
          <div>
            <p class="text-center">¿No tienes una cuenta? <RouterLink to="/register">Regístrate</RouterLink></p>
          </div>
          <div class="custom-divider text-center">
            <span> o </span>
          </div>
          <div class="text-center">
            <a href="#">
              <button class="btn btn-outline-primary" id="google-login">
                <span data-provider="google"></span>
                <img src="@/assets/google-logo.png" alt="Logo de Google" 
                style="vertical-align: middle; width: 20px; height: 20px; margin-right: 10px;">
                <span href>Continuar con Google</span>
              </button>
            </a>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style>
  .card-login {
    background-color: lightblue;
    padding: 20px;
    border-radius: 5px;
    height: 100%;
    max-width: 600px;
    margin: 0 auto;
  }

  @media screen and (max-width: 768px) {
    .card-login {
      max-width: 400px;
      padding-bottom: 10px;
    }
  }

  .form-group-login {
    text-align: left;
    padding-bottom: 15px;
  }

</style>