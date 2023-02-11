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
    getAuthenticatedUser() {
      axios.get('/api/auth_user/')
        .then(response => {
          this.$store.commit('setUsername', response.data.username)
          this.$store.commit('setUserId', response.data.id)
          localStorage.setItem('username', response.data.username)
          localStorage.setItem('user_id', response.data.id)
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