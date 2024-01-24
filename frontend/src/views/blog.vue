<template>
<div class="container mb-5">
    <div class="row gy-3">
        <div class="col-md-12">
            <div v-for="blog in blogs"
                v-bind:key="blog.id"
                class="card card mb-3 mt-3 ">
                    <div class="card-body mb-2">
                        <h5 class="card-title">{{blog.title}}</h5>
                        <p class="card-text">{{blog.short_description}}</p>
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
    }
}
</script>