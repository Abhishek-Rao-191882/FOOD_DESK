<template>

  <div>
    <span style="color:white;">
    {{requestStatus}}</span>
    <h2>Seller Login Page</h2>
    <input type="text" v-model="username" placeholder="Username">
    <input type="text" v-model="password" placeholder="Password">
    <button @click="authenticate">Log In</button>


  </div>

</template>

<script>
import axios from 'axios'
import API from "../API/API"
export default {
  name: 'SellerLogin',
  props: {
    // msg: String
  },
  data() {
    return {
      ApiResponse : null,
      verification:false,
      username : '',
      password : '',
      requestStatus:'not requested',
      
    }
  },
  methods: {

    authenticate(){
    API.authenticate(this.username,this.password)
    // axios.post(process.env.VUE_APP_SERVER+'/accounts/login',{"username":this.username,"password":this.password})
    .then(response => {
        this.ApiResponse = response.data;
        localStorage.setItem("token",response.data.token);
        this.verification = true;
        this.$router.push("home")
      })
      .catch(err=> {
        console.log('Helloooo')
        console.log(JSON.stringify(err))
        this.ApiResponse = "false "+err;
        this.verification=false;
      })
    }
  },

  async beforeRouteEnter (to, from, next) {
  
    const token=localStorage.getItem("token");
    
    if(token)
    {
      await axios.post(process.env.VUE_APP_SERVER+'/accounts/sellerlogin',{"token":token})
      .then(()=>
      {
        console.log("first")
        next("/home");
      })
      .catch(()=>{
            // localStorage.removeItem('token')   
      })
    }
    next();
  },
 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login{
 
  color: #272727;
  width: 100%;
  font-family: "Quicksand", serif;
  font-style: normal;
  font-weight: 400;
  margin-top: 10vh;
  letter-spacing: 0;
  padding: 1rem;
}
input{
  margin: 3vh;
}
</style>
