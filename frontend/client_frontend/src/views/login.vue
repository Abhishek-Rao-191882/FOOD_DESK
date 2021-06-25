<template>
    <div class="loginpage">
        <div class="signin">
           <div class="form">
           <h2 style="color:#fff;">Log In</h2>
           <input type="email" v-model="email" name="Email" placeholder="Email"/><br /><br />
           <input type="password" v-model="password" name="password" placeholder="Password" /><br /><br />
           <input type="button" @click="log_in" value="Log In" ><br /><br />
           <div class="container">
             <p class="link">Reset Password?</p> <p>|</p>
             <p class="link">Forgot Password?</p>
           </div>
           <router-link to="/">Home</router-link>

             <p> Don't have account? <a href="#"> Sign Up </a></p>             
        </div>
        </div>
    </div>
</template>


<script>

import axios from 'axios'
import API from '../API/API'



export default {
  name: 'Log_In',

  data(){
      return{
          email:'',
          password:'',
      }
  },

  methods:{
      log_in(){
        //   this.$store.dispatch('addState',this.msg)
    // this.store = this.$store.state.user;
        //   this.$store.dispatch('LogInState',)
          API.log_in(this.email,this.password)
          .then((response)=>{
              localStorage.setItem("token",response.data.token)
              this.$store.dispatch('AuthTokenState', response.data.token)
              this.$router.push("/")
          })
            .catch((err)=>{
                // console.log(err.data)
            })

      },
  },

}
</script>

<style  scoped>
.loginpage{
    background-color: #ff944d;
    height: 100vh;
    width: 100%;
}
.signin
{
    background: rgba(44,62,80,0.7);
    padding: 40px;
    width: 25%;
    height: 75vh;
    border-radius: 20px;
    position: absolute;
    top: 50%;
    left: 50%;
    -moz-transform: translateX(-50%) translateY(-50%);
    -webkit-transform: translateX(-50%) translateY(-50%);
    transform: translateX(-50%) translateY(-50%);
}
.form
{
    width: 100%;
    text-align: center;
}
input
{
    width: 270px;
    text-align: center;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    font-family: 'Play', sans-serif;
    font-size: 16px;
    font-weight: 200px;
    padding: 10px 0;
    transition: border 0.5s;
    outline: none;
    color: #fff;
    text-align: left;
}
input[type=button]
{
    border: none;
    width: 190px;
    background: white;
    color: #000;
    font-size: 16px;
    line-height: 25px;
    padding: 10px 0;
    border-radius: 15px;
    cursor: pointer;
    margin-bottom: 30px;
    text-align: center;
}
input[type=button]:hover
{
    color: #fff;
    background-color: black;
}
h2
{
    color: white;
    margin-bottom: 40px;
    font-size: 40px;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    
}
.link
{
    color: yellow;
    text-decoration: none;
    cursor: pointer;
    font-size: 15px;
    margin-right: 5px;
}
.link:hover
{
    color: skyblue;
}
a{
    color: yellow;
    text-decoration: none;
    cursor: pointer;
}
.link:hover
{
    color: skyblue;
}
.container
{
    font-size: 50px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 70px;
}
.container  a{
    margin-right: 0px; 
    font-size: 14px;
    width: 100%;
    font-family:Tahoma, Geneva, sans-serif;
    margin: 0;
    padding: 0;
}
::placeholder {
    color:aliceblue;
    opacity: 0.8; /* Firefox */
}
p{
    font-size: 18px;
    color: #fff;
}
@media screen and (max-width: 1440px){
.loginpage{
        width: 100%;
    }
    .signin{
    height: 70vh;
    width: 40%;
    margin: 0;
    padding: 40px;
    }
    input{
        width: 100%;
    }
    input[type=button]{
        width: 240px;
    }
}
@media screen and (max-width: 768px) {
    .loginpage{
        width: 100%;
    }
    .signin{
    height: 90vh;
    width: 80%;
    margin: 0;
    padding: 40px;
    }
    input{
        width: 100%;
    }
    input[type=button]{
        width: 240px;
    }
}
@media screen and (max-width: 428px) {
    .loginpage{
        width: 100%;
    }
    .signin{
        height: 90vh;
        width: 80%;
        margin: 0;
        padding: 10px;
    }
    input{
        width: 230px;
    }
    input[type=button]{
        width: 200px;
    }
}
</style>