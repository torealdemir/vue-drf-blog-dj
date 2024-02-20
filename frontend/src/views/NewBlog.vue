<template>
  <div class="mb-5 vw-100">
    <form v-on:submit.prevent="submitBlog()" class="vh-100">
      <div class="w-50 mx-auto pt-2">
        <div >
        <label for="exampleFormControlInput1" class="form-label mx-1"><strong>Title</strong></label>
        <input type="text" class="form-control" id="" placeholder="NewBlog" v-model="blog.title">
      </div>
      </div>
      <div class="w-50 mx-auto pt-2">
        <div>
        <label for="exampleFormControlInput1" class="form-label  mx-1"><strong>Slug</strong></label>
        <input type="text" class="form-control" id="" placeholder="Slug" v-model="blog.slug">
      </div>
      </div>
      <div class="w-50 mx-auto pt-2">
        <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label mt-3 mx-1"><strong>Short Description</strong></label>
        <input type="text" class="form-control" id="" placeholder="Short Description" v-model="blog.short_description">
      </div>
      <div class="w-50 mb-5 pt-2">
        <div>
          <label for="exampleFormControlInput1" class="form-label mx-1 w-100%"><strong>Image</strong></label>
          <input type="file" class="form-control" id="" v-on:change="handleImageUpload">
        </div>   
      </div>
        <div class="mb-2">
          <label for="exampleFormControlTextarea1" class="form-label mt-3 mx-1"><strong>Content!</strong></label>
          <textarea class="form-control" id="exampleFormControlTextarea1" placeholder="Content" rows="10" v-model="blog.content"></textarea>
        </div>

       
        <button type="submit" class="btn btn-primary">Submit!</button>
     </div>
    </form>
  </div>
  
  <!-- <Footer /> -->
</template>

<script>
import axios from 'axios';
import Footer from '../components/Footer.vue'

export default {
  data(){
    return{
      blog: {
        title: '',
        content: '',
        slug:'',
        short_description:'',
        image: null,
    },
    }   
  },
  components: {
    Footer
  },


  methods:{
      async submitBlog(){
        const token = localStorage.getItem('token')
        const formData = new FormData();

        formData.append('title', this.blog.title);
        formData.append('content', this.blog.content);
        formData.append('slug', this.blog.slug);
        formData.append('shor_descrtiption', this.blog.short_description);
        formData.append('image', this.blog.image);

        try{
          const response = await axios.post('blogs/addblog/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
              Authorization: `Token ${token}`,
            },
          });
          console.log(formData)

          this.blog.title = '';
          this.blog.content = '';
          this.blog.slug = '';
          this.blog.short_description='';
          this.blog.image = null;

          alert('Blog was added');

        } catch (error){
          console.log(error);
        }
      },
      handleImageUpload(event) {
        const file = event.target.files[0];
        this.blog.image=file;
      }
      
    }
}
</script>