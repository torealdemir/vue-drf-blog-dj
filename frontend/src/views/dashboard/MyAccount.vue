<template>
    <div class="about">
        <h1>MyAcoount</h1>

        <button class="btn btn-danger" @click="logout()">Logout</button>
    </div>
  </template>

<script>
import axios from 'axios';
import { toHandlers } from 'vue';

export default {

    methods: {
        async logout(){
            console.log('Logout')
            await axios
            .post('token/logout/')
            .then(response => {
                console.log('logout')
                axios.defaults.headers.common['Authorization']=""
                localStorage.removeItem('token')
                this.$store.commit('removeToken')
                this.$router.push('/')
            })
            
        }
    }
}

</script>
  