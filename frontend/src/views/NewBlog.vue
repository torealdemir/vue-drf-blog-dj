<template>
  <form v-on:submit.prevent="submitBlog()">
      <div class="w-50 mx-auto pt-5">
        <div >
        <label for="exampleFormControlInput1" class="form-label mx-1"><strong>Title</strong></label>
        <input type="text" class="form-control" id="" placeholder="NewBlog" v-model="blog.title">
      </div>
      </div>
      <div class="w-50 mx-auto pt-5">
        <div>
        <label for="exampleFormControlInput1" class="form-label  mx-1"><strong>Slug</strong></label>
        <input type="text" class="form-control" id="" placeholder="Slug" v-model="blog.slug">
      </div>
      </div>
      <div class="w-50 mx-auto pt-5">
        <div class="mb-3">
        <label for="exampleFormControlInput1" class="form-label mt-3 mx-1"><strong>Short Description</strong></label>
        <input type="text" class="form-control" id="" placeholder="Short Description" v-model="blog.short_description">
      </div>
        <div class="mb-3">
          <label for="exampleFormControlTextarea1" class="form-label mt-3 mx-1"><strong>Content!</strong></label>
          <textarea class="form-control" id="exampleFormControlTextarea1" placeholder="Content" rows="10" v-model="blog.content"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit!</button>
     </div>
  </form>
  
</template>

<script>
import axios from 'axios';

export default {
  data(){
    return{
      blog: {
        title: '',
        content: '',
        slug:'',
        short_description:'',
    },
    }   
  },


  methods:{
      async submitBlog(){
        const token = localStorage.getItem('token')
        await axios
            .post('blogs/addblog/', this.blog, {
              headers:{
                Authorization: `Token ${token}`
              }
            })
            .then(response => {
              this.blog.title=''
              this.blog.name=''
              this.blog.content=''
              this.blog.slug = ''
              this.blog.short_description = ''
              alert('Blog was added')
            })
            .catch(error => {
              console.log(error)
            })
      }
      
    }
}
</script>

<!-- title = models.CharField(max_length=120)
slug = models.SlugField(null=True)
short_description = models.TextField(blank=True, null = True)
created_at = models.DateField(auto_now_add = True, null = True)
updated_at = models.DateField(auto_now= True)
content = models.TextField()
created_by = models.ForeignKey(User, on_delete= models.CASCADE, null = True) -->