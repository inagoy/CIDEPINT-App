<script setup>
import { ref } from 'vue';
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore();

const googleError = ref(null);

const schema = Yup.object().shape({
    email: Yup.string().email('Ingrese un Email válido').required('Ingrese un Email'),
    password: Yup.string().required('Ingrese una contraseña')
});

function onSubmit(values, { setErrors }) {
    const { email, password } = values;
    return authStore.login(email, password)
          .catch(error => setErrors({ apiError: error }))
}

function loginWithGoogle(response){
  return authStore.loginWithGoogle(response)
          .catch(error => googleError.value = error)
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
            <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                <div class="form-group-login">
                    <label>Dirección de Email</label>
                    <Field name="email" type="text" class="form-control" :class="{ 'is-invalid': errors.email }" />
                    <div class="invalid-feedback">{{errors.email}}</div>
                </div>            
                <div class="form-group-login">
                    <label>Contraseña</label>
                    <Field name="password" type="password" class="form-control" :class="{ 'is-invalid': errors.password }" />
                    <div class="invalid-feedback">{{errors.password}}</div>
                </div>            
                <div class="form-group">
                    <button class="btn btn-primary" :disabled="isSubmitting">
                        <span v-show="isSubmitting" class="spinner-border spinner-border-sm mr-1"></span>
                        Iniciar Sesión
                    </button>
                </div>
                <div v-if="errors.apiError" class="alert alert-danger mt-3">{{errors.apiError}}</div>
            </Form>
          </div>
          <div>
            <p class="text-center mt-3">¿No tienes una cuenta? <RouterLink to="/register">Regístrate</RouterLink></p>
          </div>
          <table width="100%">
          <tr>
            <td><hr></td>
            <td style="width:1px; padding: 0 10px; white-space: nowrap;">o</td>
            <td><hr /></td>
          </tr>
        </table>
          <div class="text-center m-2">
            <GoogleLogin :callback="loginWithGoogle"/>
            <div v-if="googleError" class="alert alert-danger mt-3">{{ googleError }}</div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style>
  .card-login {
    background-color: whitesmoke;
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