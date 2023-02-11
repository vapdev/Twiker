<template>
  <router-view />
</template>

<script setup>
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router';
import { useStore } from 'vuex'

const router = useRouter();
const route = useRoute();

const store = useStore();

store.commit('initializeStore')

const token = store.state.token

function verifyToken() {
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Token ${token}`
  } else if (route.name !== 'SignUp') {
    axios.defaults.headers.common['Authorization'] = ''
    return router.push('/login')
  } else {
    return router.push('/signup')
  }
}

function getAuthenticatedUser() {
  axios.get('/api/auth_user/')
    .then(response => {
      store.commit('setUsername', response.data.username)
      store.commit('setUserId', response.data.id)
      localStorage.setItem('username', response.data.username)
      localStorage.setItem('user_id', response.data.id)
    })
    .catch(error => {
      console.log(error)
    })
}

getAuthenticatedUser();
verifyToken();

</script>