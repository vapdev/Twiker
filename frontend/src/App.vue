<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate(){
    this.$store.commit('initiateStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = `Token ${token}`
    } else if (this.$route.name !== 'SignUp') {
      axios.defaults.headers.common['Authorization'] = ''
      return this.$router.push('/login')
    } else {
      return this.$router.push('/signup')
    }
  }
}
</script>

<template>
  <router-view />
</template>