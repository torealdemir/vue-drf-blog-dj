<template>
    <div class="container mb-5">
        <div class="row gy-3">
            <div class="col-md-12">
                <div 
                    class="card card mb-3 mt-3 ">
                        <div class="card-body mb-2">
                            <h3 class="card-title">{{blogd.title}}</h3>
                            <h4 class="card-title">{{ blogd.short_description }}</h4>
                            <p class="mx-auto">{{ blogd.created_by }}</p>

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
            .get(`blogs/${slug}/`)
            .then(response =>{
                console.log(response.data)
                this.blogd = response.data
            })
    }
}
</script>