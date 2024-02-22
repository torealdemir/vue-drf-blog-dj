<template>
<div class="container mb-5">
    <div class="row gy-3">
        <div class="col-md-12">
            <div v-for="blog in blogs"
                v-bind:key="blog.slug"
                class="card card mb-3 mt-3 ">
                    <div class="card-body mb-2">
                        <div class="d-flex">
                            <div class="w-50% h-50%">
                                <img class="img-fluid img-thumbnail" :src="getImageUrl(blog.image)" alt="Blog Image">
                                <h5 class="card-title">{{blog.title}}</h5>
                            </div>
                        </div>
                       
                        <p class="card-text">{{blog.short_description}}</p>
                        <p ><strong>Created at:  {{ blog.created_at }}</strong></p>
                        
                        
                        <p>{{ blog.created_by_username}}</p>
                        <router-link :to="{name:'blogd', params:{slug:blog.id}}" class="ms-auto btn btn-primary">See More!</router-link>
                        <button @click="deleteItem(blog.id)" class="btn btn-danger mx-4">Delete!</button>
                    </div>
            </div>
        </div>
    </div>

</div>

    
</template>

<script>
import axios from 'axios';
import 'vue-toast-notification/dist/theme-bootstrap.css'
import { useToast } from 'vue-toast-notification';


export default {
    data() {
        return {
            blogs: []
        }
    },
    setup(){
        const toast = useToast();
        return {toast}
    },
    mounted(){
        this.loadPage()     
    },
    methods: {
    loadPage() {
      try {
        axios
          .get('blogs/')
          .then(response => {
            console.log(response.data);
            this.blogs = response.data;
          })
          .catch(error => {
            console.log('You are not authenticated');
            this.triggerAuthenticateAlert()
          });
      } catch (error) {
        console.log(error);
      }
    },
    deleteItem(blogID) {
      axios.delete(`blogs/deleteblog/${blogID}/`);
      this.loadPage();
      window.location.reload();
    },
    getImageUrl(imagePath) {
      return `http://localhost:8000/${imagePath}`;
    },
    triggerAuthenticateAlert(){
        this.toast.warning("U must be authenticate if u want to see the blogs!")
    }
  }
}


</script>