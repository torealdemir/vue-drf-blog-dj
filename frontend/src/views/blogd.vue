<template>
    <div class="container mb-5">
        <div class="row gy-3">
            <div class="col-md-12">
                <div 
                    class="card card mb-3 mt-3 ">
                        <div class="card-body mb-2">
                            <h5 class="card-title">{{blogd.title}}</h5>
                            <p class="card-text">{{blogd.content}}</p>
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
        }
    },
    mounted(){
        console.log('mounted!')

        const slug = this.$route.params.slug

        axios
            .get(`api/v1/blogs/${slug}`)
            .then(response =>{
                console.log(response.data)
                this.blogd = response.data
            })
    }
}
</script>