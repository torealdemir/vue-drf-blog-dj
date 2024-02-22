<template>
    <div class="container mb-5">
      <div class="row gy-3">
        <div class="col-md-12">
          <div class="card card mb-3 mt-3">
            <div class="card-body mb-2">
              <h3 class="card-title">{{ blogd.title }}</h3>
              <h4 class="card-title my-4">{{ blogd.short_description }}</h4>
              <p class="my-4"><strong>{{ blogd.created_at }}</strong></p>
              <div class="w-50% h-50%">
                <img v-if="blogd.image" class="img-fluid img-thumbnail" :src="getImageUrl(blogd.image)" alt="Blog Image">
              </div>
              <p class="mx-auto">{{ blogd.created_by }}</p>
              <p class="card-text">{{ blogd.content }}</p>
              <button class="btn btn-danger">Delete!</button>
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
        blogd: []
      };
    },
    mounted() {
      const slug = this.$route.params.slug;
      axios.get(`blogs/${slug}/`)
        .then(response => {
          console.log(response.data);
          this.blogd = response.data;
        });
    },
    methods: {
      getImageUrl(imagePath) {
        return `http://localhost:8000/${imagePath}`;
      }
    }
  };
  </script>