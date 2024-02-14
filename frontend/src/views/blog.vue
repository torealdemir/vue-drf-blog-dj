<template>
<div class="container mb-5">
    <div class="row gy-3">
        <div class="col-md-12">
            <div v-for="blog in blogs"
                v-bind:key="blog.slug"
                class="card card mb-3 mt-3 ">
                    <div class="card-body mb-2">
                        <h5 class="card-title">{{blog.title}}</h5>
                        <p class="card-text">{{blog.short_description}}</p>
                        <p ><strong>Created at:  {{ blog.created_at }}</strong></p>
                        <p>{{ blog.username }}</p>
                        <router-link :to="{name:'blogd', params:{slug:blog.id}}" class="ms-auto btn btn-primary">See More!</router-link>
                    </div>
            </div>
        </div>
    </div>

</div>

    
</template>

<script>
import axios from 'axios';



export default {
    data() {
        return {
            blogs: []
        }
    },
    mounted(){
        console.log('mounted!')
        axios
            .get('blogs/')
            .then(response =>{
                console.log(response.data)
                this.blogs = response.data
            })
    },
    computed: {
        createByUserName(){
            if(this.blogs.created_by){
                return this.blogs.created_by.username;
                console.log(username)
            } else {
                return "";
            }
        }
    }
}
</script>