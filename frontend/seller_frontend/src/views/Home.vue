<template>
  <div class="home">
    <div class="header">
      <div><img src="../assets/logo3.png" style="" alt="" /></div>
      <div><button class="log_out" @click="logout"><i class="fa fa-sign-out" aria-hidden="true"></i> Log Out</button></div>
      <!-- <h1>FOOD DESK</h1> -->
    </div>
    <input type="checkbox" id="openSidebarMenu" />
    <label for="openSidebarMenu" class="sidebarIconToggle">
      <div class="spinner top"></div>
      <div class="spinner middle"></div>
      <div class="spinner bottom"></div>
    </label>
    <div id="sidebarMenu">
      <ul class="menu">
       <center><div class="user"> <img src="../assets/img.jpeg" height="100vh" width="70%" style="border-radius:50%;border:2px solid white;margin-bottom:1vh;">
       <br>
       <span style="font-family: cursive;color:orange;font-size:3vh;"><b>{{User.first_name}} {{User.last_name}}</b></span>
       </div>
       </center>
        <li><router-link to="/home">Dashboard</router-link></li>
        <!-- <li><router-link v-bind:to="{ name: 'Products', params: { userInfo: User}}">Products</router-link> -->
        <li><router-link to="/products">Products</router-link></li>

        <li><router-link to="/categories">Categories</router-link></li>

        <li><router-link to="/orders" class="dropbtn">Orders</router-link></li>

        <li><router-link to="/active_orders" class="dropbtn">Active Orders</router-link></li>

        <li><router-link to="/rejected_orders" class="dropbtn">Rejected Orders</router-link></li>
        
      </ul>

      <div class="footer">
        <div class="socialIcon">
          <button>
            <i class="fa fa-facebook-official" aria-hidden="true"></i>
          </button>
          <button><i class="fa fa-google-plus" aria-hidden="true"></i></button>
          <button><i class="fa fa-instagram" aria-hidden="true"></i></button>
          <button><i class="fa fa-twitter" aria-hidden="true"></i></button>
        </div>
        <div class="copyright">
          <button><i class="fa fa-copyright" aria-hidden="true"></i></button>
          <p style="color: white;">copyright-2020 FOOD DESK</p>
        </div>
      </div>
    </div>

    <div class="main">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

import API from "../API/API"
export default{
  data(){
    return{
      User : '',
    }
  },
  created () {
    this.UserInfo()
  },
  methods:{
    UserInfo(){
      API.UserInfo()
      .then((response)=>{
        console.log('Attempted')
        this.User = response.data
      })
      .catch(()=>{
        // localStorage.removeItem('token')
      })
    },
    logout(){
      const token = localStorage.getItem('token')
      console.log('come here')
      axios.post('http://localhost:8000/accounts/logout',{"token":token})
      .then(()=>{
        localStorage.removeItem('token')
      this.$router.push("/")
      })
      .catch(()=>{
          // this.$router.push("/products")
      })
    }
  }
}

</script>

<style scoped>
/* require('@/assets/styles/main.css') */
/* @import url('./assets/font-awesome/css/font-awesome.min.css'); */
* {
  box-sizing: border-box;
}
html,
body {
  overflow-x: hidden;
  height: 100%;
}
body {
  font-family: arial, sans-serif;
  background: #fff;
  padding: 0;
  margin: 0;
}

.header {
  /* background:  #2e86de; */
  background:  #0F9FB4;
  background: #f76e2a;

  width: 100%;
  height: 10vh;
  position: fixed;
  z-index: 10;
  /* margin: 0; */
  display: flex;
  justify-content: center;
  align-items:flex-start;
}
.header img {
  height: 75px;
  width: 150px;
  margin: 5px;
  float: right;
}
.header h1 {
  color: #FFF;
}
.header div:nth-child(1){
  flex: 1.5;
  
}
.header div:nth-child(2){
  flex: 1;
}
.log_out{
        background-color: rgb(0, 153, 255);
        color: white;
        border: none;
        cursor: pointer;
        opacity: 1;
        float: right;
        /* transform: translate(200px); */
        width: 7rem;
        margin: 1rem;
        border-radius: 5%;
        border: 2px solid blue;
        font-size: 1.2rem;
      }
#sidebarMenu {
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  width: 15%;
  margin-top: 10vh;
  /* background: #444543; */
  background: #002984;
  z-index:20;
  /* transform: translateX(-310px); */
  transition: transform 250ms ease-in-out;
}

.main {
  height: 88vh;
  margin-top: 10vh;
  padding: 10px 0px;
  margin-left: 15%;
}
.menu {
  list-style: none;
  padding: 10%;
  /* margin-top: 0vh; */
/*  margin-bottom: 10vh;*/
}
.user{
  
  margin-bottom: 2vh;
  /* border: 2px solid black; */
}
.menu li {
    color: #fff;
    height: 7vh; 
/*  border-bottom: 1px solid rgba(255, 255, 255, 0.1);*/
}
.menu li ul li {
  list-style: none;
}
.menu li ul {
  display: none;
}
.menu li a {
  color: #fff;
  display: block;
  text-decoration: none;
  text-transform: uppercase;
  padding: 5%;
}
.footer {
  margin-top: 13vh;
  margin-left: 5%;
}
.footer .socialIcon {
  display: flex;
    color: #fff;
  justify-content: space-evenly;
}
.socialIcon button {
    color: #fff;
  border: none;
  background: none;
  font-size: 25px;
  cursor: pointer;
}
.footer .copyright {
  display: flex;
    
  justify-content: flex-start;
}
.footer .copyright button {
  border: none;
    color: #fff;
  background: none;
  font-size: 15px;
  cursor: pointer;
}
.footer .copyright p {
  margin-top: 4%;
  font-size: 10px;
}

/* responsive */

@media screen and (max-width: 768px) {
  .sidebarIconToggle {
    height: 22px;
    width: 22px;
    position: absolute;
    z-index: 20;
    top: 22px;
    left: 15px;
    cursor: pointer;
  }
  .header img {
  height: 80px;
  width: 150px;
  margin: 5px;
}
  .spinner {
    height: 3px;
    background: #000;
    transition: all 0.3s;
  }
  .spinner.middle,
  .spinner.bottom {
    margin-top: 3px;
  }
  #openSidebarMenu:checked ~ .sidebarIconToggle > .spinner.middle {
    opacity: 0;
  }
  #openSidebarMenu:checked ~ .sidebarIconToggle > .spinner.top {
    transform: rotate(135deg);
    margin-top: 9px;
  }
  #openSidebarMenu:checked ~ .sidebarIconToggle > .spinner.bottom {
    transform: rotate(-135deg);
    margin-top: -9px;
  }

  #sidebarMenu {
    height: 100%;
    position: fixed;
    left: 0;
    top: 0;
    width: 40%;
    margin-top: 10vh;
    /* background: #2e86de; */
    transform: translateX(-310px);
    transition: transform 250ms ease-in-out;
  }
  #openSidebarMenu:checked ~ #sidebarMenu {
    transform: translateX(0px);
  }
  .main {
    margin-left: 0;
  }
}
@media screen and (max-width: 426px) {
  .sidebarIconToggle {
    height: 22px;
    width: 22px;
    position: absolute;
    z-index: 20;
    top: 22px;
    left: 15px;
    cursor: pointer;
  }
  .spinner {
    height: 3px;
    background: #000;
    transition: all 0.3s;
  }
  .spinner.middle,
  .spinner.bottom {
    margin-top: 3px;
  }
  #openSidebarMenu:checked ~ .sidebarIconToggle > .spinner.middle {
    opacity: 0;
  }
  #openSidebarMenu:checked ~ .sidebarIconToggle > .spinner.top {
    transform: rotate(135deg);
    margin-top: 9px;
  }
  #openSidebarMenu:checked ~ .sidebarIconToggle > .spinner.bottom {
    transform: rotate(-135deg);
    margin-top: -9px;
  }
  #sidebarMenu {
    height: 100%;
    position: fixed;
    left: 0;
    top: 0;
    width: 50%;
    margin-top: 10vh;
    /* background: #444543; */
    transform: translateX(-310px);
    transition: transform 250ms ease-in-out;
  }
  #openSidebarMenu:checked ~ #sidebarMenu {
    transform: translateX(0px);
  }
  .header img {
  height: 80px;
  width: 150px;
  margin: 5px;
  }
  .footer {
  margin-top: 10vh;
  margin-left: 5%;
  }

}
</style>