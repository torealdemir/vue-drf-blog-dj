<template>

    <div class="d-flex justify-content-center align-items-center my-5">
        <div class="title w-50 d-flex justify-content-center w-100">
            <div class="w-50 d-flex justify-content-center">
    
                
    
                <form  v-on:submit.prevent="submitForm"  class="col-md-4 col-md-offset-4">
    
                <div class="form-group">
                    <h1 class="my-3">Login!</h1>
          
                    <label for="exampleInputEmail1">Email address</label>
                    <input v-model="username" type="email" class="form-control mb-3" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                </div>
                <div class="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input v-model="password" type="password" class="form-control mb-3" id="exampleInputPassword1" placeholder="Password">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
                </form>
    
                <div v-if="errors.length" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                    <div class="toast-header">
                        <p v-for="error in errors"
                        v-bind:key="error">{{ error }}</p>
                    </div>
    
                </div>
    
            </div>
           
        </div>
    
    </div>
    
    
    
    </template>
    
    <script>
    
    import axios from "axios";
    import { Toast } from "bootstrap/dist/js/bootstrap.esm.min.js";
    import { toHandlers } from "vue";
     
    export default {
        name:'Login',
    
    
        data(){
            return {
                username:'',
                password:'',
                errors:[]
            }
        },
        methods:{
            submitForm (){
                console.log('submit!')

                axios.defaults.headers.common['Authorization']= ""

                localStorage.removeItem('token')
                
                this.errors=[]
                
                if(this.username === ''){
                    this.errors.push('the username is missing!')
                    console.log('empty email')
                }
                if(this.password === '' ){
                    this.errors.push('password is missing')
                }
                if(!this.errors.length){
                    const formData = {
                        username: this.username,
                        password: this.password
                    }
                    axios
                        .post('token/login/', formData)
                        .then(response => {
                            const token = response.data.auth_token

                            this.$store.commit('setToken', token)

                            axios.defaults.headers.common['Authorization'] = "Token " + token

                            localStorage.setItem('token', token)

                            this.$router.push('/dashboard/my-account')
                        })
                        .catch(error => {
                            if(error.response){
                                for(const property in error.response.data){
                                    this.errors.push(`${property}:${error.response.data[property]}`)
                                }
                                console.log(JSON.stringify(error.response.data))
                            } else if (error.message) {
                                this.errors.push('something went wrong try again')
                                console.log(JSON.stringify(error))
                            }
                        })
                }
            }
        }
    }
    
    </script>