
<template>
<div>
  <Nav />  
  <Footer />
</div>
  <RouterView/>


</template>


<script>
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'
import axios from 'axios';
import 'vue-toast-notification/dist/theme-bootstrap.css'
import { useToast } from 'vue-toast-notification';




export default {
  name: 'App',
  components:{
    Nav,
    Footer,
  },

  setup(){
   const toast = useToast();
   return {toast}
 },
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.user.token
    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
}
</script>
<style lang="scss">

li:hover {
  transition: 0.3s;
  scale: 1.3;
  color: aquamarine;
}

a:hover {
  transition: 0.3s;
  scale: 1.3;
}
</style>
