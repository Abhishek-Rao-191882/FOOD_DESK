<template>
  <div class="router_view">
    <router-view></router-view>
  </div>

</template>

<script>
import HelloWorld from './components/HelloWorld';

import Axios from 'axios'
// import API from '../API/API'


export default {
  name: 'App',

  components: {
    HelloWorld,
  },

beforeMount(){
  
    if(localStorage.getItem('token')) 
 {
   console.log("Sourabh")
   const token = localStorage.getItem('token')
  Axios.post(process.env.VUE_APP_SERVER+'/accounts/clientlogin',{"token":token})
          .then((response)=>{
            const msg = "Only Hotels Are Allowed"
            // console.log("Second1")
            if(response.data)
            {
                // console.log(response.data)
                this.$store.dispatch('ClientData', response.data)
                // this.$router.push("/")
                // next('/')

          }
            else{
              // console.log("Second2")
              const token = ""
              this.$store.dispatch('AuthTokenState', token)
            }
              // next()
          }
            )
        .catch( ()=>{
          const token = ""
          this.$store.dispatch('AuthTokenState', token)
          // localStorage.removeItem('token')
          // console.log("Second 3")
          // this.$router.push("/login")
        } 
        )
 } 
//  else
//  {
//   this.$router.push('/login'); // go to '/login';
//  }
else{
  console.log("Saraswat")
}




  },
  data: () => ({
    //
  }),



  // created(){
  //   Axios.get("http://127.0.0.1:8000/accounts/reset_password/")
  //   .then((response)=>{
  //     // localStorage.setItem('checks',response.data.token)
  //     // document.cookie=`csrftoken=${response.data.token};`
  //     console.log(response.data)
  //   })
  //   .catch(()=>{
  //     console.log("Csrf failed")
  //   })
  // },
};
</script>




