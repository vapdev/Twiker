<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = `Token ${token}`
    } else if (this.$route.name !== 'SignUp') {
      axios.defaults.headers.common['Authorization'] = ''
      return this.$router.push('/login')
    } else {
      return this.$router.push('/signup')
    }
  },
  created() {
    this.getAuthenticatedUser()
  },
  methods: {
    logout() {
      this.$store.commit('logout')
      this.$router.push('/login')
    },
    getAuthenticatedUser() {
      axios.get('/api/auth_user/')
        .then(response => {
          console.log(response.data)
          this.$store.commit('setAuthenticatedUsername', response.data.username)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<template>
  <router-view />
</template>