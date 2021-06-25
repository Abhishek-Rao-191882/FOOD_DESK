<template>
    <div class="nav-component">
        <nav class="header">
      <div class="item" id="item-1">
        <div class="menu-button" id="menu-button">&#9776;</div>
      </div>
      <div class="item" id="item-2">
        <img class="logo" src="../assets/logo.png" alt="" />
      </div>
      <div class="item" id="item-3">
        <ul class="menulist">
          <li class="list"><router-link :to="{name:'Products'}" class="link" href="#">Home</router-link></li>
          <li class="list"><router-link :to="{name:''}" class="link" href="#">Get App</router-link></li>
          <li class="list"><router-link :to="{name:''}" class="link" href="#">Services</router-link></li>
          <li class="list"><router-link :to="{name:''}" class="link" href="#">Feedback</router-link></li>
          <li class="list"><router-link :to="{name:'Sign_Up'}" class="link" href="#">Sign up</router-link></li>
          <li class="list"><a class="link" href="#popup1">Sign in</a></li>
        </ul>
      </div>
      <div class="item" id="item-4">
        <router-link :to="{ name:'Cart'}">
        <a  class="cart"><img style="height:25px" src="../assets/cart.png" alt=""></a>
        </router-link>
      </div> 
    </nav>
    <!-- navbar ends -->

    <!-- signindiv starts -->
    <div class="signindiv">
      <div id="popup1" class="popup">
        <a href="#" class="close">&times;</a>
        <h2 class="signin">Sign in</h2>
        <form action="index_submit" method="get" accept-charset="utf-8">
          <input type="Email" placeholder="Enter Email">
          <input type="password" placeholder="Enter Password">
          <div class="btn-box">
            <button class="common-btn">Sign In</button>
          </div>
          <p><a class="forgot" href="#">forgot password?</a></p>
          <p>don't have account create <a href="#" class="forgot"> a new one</a></p>
          <hr>
          <p class="stext">or</p>
          <p class="stext">sign in using</p>
          <div class="singinoption">
          <a href="#" class="sicon"> <img src="../assets/download.png" alt=""> </a>
          <a href="#" class="sicon"><img src="../assets/facebook.png" alt=""></a>
          </div>
        </form>
      </div>
      <a href="#" class="close-popup"></a>
    </div>
    <!-- signindiv ends -->
    <nav id="hide-menu" class="hide-menu">
      <div class="photopart">
      <div class="introbox">
        <img class="custimg" src="../assets/login.png" alt="">
        <p class="hiCustomer">Hi, <span>Customer Name</span></p>
        <p>FoodDesk2020@gmail.com</p>
      </div>
      </div>
      <div class="linksmaindiv">
        <div class="linkslist">
          <div class="links"><img class="linkicon" src="../assets/home.png" alt=""><a class="linkdev" href="#">Home</a></div>
          <div class="links"><img class="linkicon" src="../assets/active orders.png" alt=""><a class="linkdev" href="#">Active Orders</a></div>
          <div class="links"><img class="linkicon" src="../assets/delivered orders.png" alt=""><a class="linkdev" href="#">Delivered Orders</a></div>
          <div class="links"><img class="linkicon" src="../assets/select hotel.png" alt=""><a class="linkdev" href="#">Select Hotel</a></div>
        </div>
        <hr>
        <p class="communicate">Communicate</p>
        <div class="linkslistdev">
          <div class="links"><img class="linkicon" src="../assets/share1.png" alt=""><a class="linkdev" href="#">Share</a></div>
          <div class="links"><img class="linkicon" src="../assets/contact us1.png" alt=""><a class="linkdev" href="#">Contact Us</a></div>
          <div class="links"><img class="linkicon" src="../assets/about develpoers.png" alt=""><a class="linkdev" href="#">About Developers</a></div>
        </div>
        <hr>
        <div class="loginbuttondiv">
          <button class="loginbutton"><a href="#">Sign up</a></button>
          <button class="loginbutton"><a href="#popup1">Sign In</a></button>
        </div>
      </div>
    </nav>

    <div class="views">

      <router-view>
        
      </router-view>

    </div>

    </div>
</template>

<script>


import $ from 'jquery'
import products from './Products'

export default {
    mounted(){

        $('#menu-button').click(function(e){
            e.stopPropagation();
            console.log('clicked');
            $('#hide-menu').toggleClass('show-menu');
        });
        $('#hide-menu').click(function(e){
            e.stopPropagation();
        });
        $('body,html').click(function(e){
              $('#hide-menu').removeClass('show-menu');
        });
    },
    
    components:{
        products,
    }
}
</script>

<style scoped>

.views{
  padding-top: 10vh;
  height: 90vh;
  width: 100%;
  /* background-color: #00e5ee; */
}

.nav-component{
  margin-top: 0;
}

*{
    margin: 0;
    padding: 0;
}
body{
    overflow:hidden;
    margin: 0;
    padding: 0;
}

.header {
    background: linear-gradient(135deg,#EC8197 , #EE9f63, #2382F8 );
    height: 10vh;
    width: 100%;
    z-index: 10;
    position: fixed;
    display: flex;
    margin: 0;
    /* justify-content: space-between;  */
    align-items: center;
}
.item{
    margin: 0;
    /* border: 1px solid red; */
}
#item-1{
display: none;
}
/* #item-2{

    
} */
#item-3{
    flex-grow: 5;
    float: right;
}
/* #item-4{
    
} */
.menu-button{
    display: none;
}
.logo{
    height: 8vh;
    /* width: 10vh; */
    margin-left: 55px  ;
    /* border: 1px solid red; */
}
.cart {
    height: 30px;
    width: 40px;
    display: inline-block;
    padding: 10px 10px;
    border-radius: 50%;
    transition: background 0.3s;
    margin: 20px ;
    /* border: 1px solid red; */
  }
  .cart img{
    height: 30px;
    width: 40px;
  }
  .cart:hover {
    background: #00898e;
  }
  .menulist{
      list-style: none;
      display: flex;
      float: right;
  }
  .menulist .list{
    height: 35px;
    font-size: 1.5rem;
    /* border: 1px solid red; */
    margin-right: 80px;
  } 
  .menulist .list .link{
      text-decoration: none;
      transition: ease 0.5s;
      color: white;
  }
  
  .menulist .list .link::after {
    content: "";
    display: block;
    width: 0;
    height: 2px;
    background: #fff;
    transition: width 0.5s;
  }
  .menulist .list .link:hover::after {
    width: 100%;
    transition: width 0.5s;
  }

  .hide-menu{
    background-color:#f9f9fa;
    position: absolute;
    top:0;
    left:0;
    z-index: 1;
    width: 80%;
    height: 100%;
    transform: translateX(-100%);   
    transition: all 0.3s linear;
    z-index: 200;
    border: 1px solid rgb(199, 195, 195);
   
} 
 .show-menu{
   transform: translateX(0);
 }
 .hide-menu .photopart{
     width: 100%;
     height: 30vh;
     background: linear-gradient(135deg,#EC8197 , #EE9f63, #2382F8 );
     display: flex;
     /* flex-direction: column; */
     justify-content: center;
     /* position: relative; */
 }  
 .hide-menu .photopart .introbox{
     display: flex;
     flex-direction: column;
     justify-content: space-evenly;
 }
 .hide-menu .photopart img{
     height: 80px;
     width: 80px;
     margin-top: 20px;
     margin-left: 50px;
     margin-bottom: 10px;
 }
 .hide-menu .photopart p{
     font: 15px;
     line-height: 20px;
     /* margin: 0 0 20px 0; */
     text-align: center;
 }

.hide-menu .linksmaindiv .linkslist{
     list-style: none;
     margin: 0;
     padding: 0;
 }

 .hide-menu .linksmaindiv .linkslist .links{
     line-height: 40px;
     margin: 0;    
     color: black; 
 }
 .hide-menu .linksmaindiv .linkslist .links:first-child{
     margin-top: 10px;
 }
 .hide-menu .linksmaindiv .linkslist .links:last-child{
     margin-bottom: 10px;
 }
 .hide-menu .linksmaindiv .linkslist .links:hover{
     background: rgb(194, 189, 189);
     color: coral;
 }
 .hide-menu .linksmaindiv .linkslist .links .linkdev{
     color: black;
     font-size: 15px;
     width: 100%;
     
 }
 .hide-menu .linksmaindiv .linkslist .links .linkdev:hover{
     color: coral;
 }
 .hide-menu .linksmaindiv .linkslist .links .linkicon{
     height: 15px;
     width: 15px;
     margin-right: 30px;
     margin-left: 20px;
 }
hr{
    margin: 0px;
}
 .communicate{
     margin-left: 20px;
     color: rgb(56, 55, 55);
     font-size: 15px;
     line-height: 40px;
 }
 .hide-menu .linksmaindiv .linkslistdev{
     list-style: none;

 }
 .hide-menu .linksmaindiv .linkslistdev .links{
    margin: 0;
    line-height: 40px;
}
.hide-menu .linksmaindiv .linkslistdev .links:last-child{
    margin-bottom: 10px;
}
.hide-menu .linksmaindiv .linkslistdev .links:hover{
    background: rgb(194, 189, 189);
    color: coral;
}
.hide-menu .linksmaindiv .linkslistdev .links .linkdev{
    color: black;
}
.hide-menu .linksmaindiv .linkslistdev .links .linkdev:hover{
    color: coral;
}
 .hide-menu .linksmaindiv .linkslistdev .links .linkicon{
    height: 15px;
    width: 15px;
    margin-right: 30px;
    margin-left: 20px;
}
.hide-menu .linksmaindiv .loginbuttondiv {
    display: flex;
    justify-content: center;
}
.hide-menu .linksmaindiv .loginbuttondiv button{
    width: 100px;
    /* height: 25px;
    line-height: 25px; */
    border-radius: 15%;
    /* border: rgb(110, 106, 106); */
    background: lightblue;
    margin: 5px;
}
.hide-menu .linksmaindiv .loginbuttondiv button a{
    font-size: 20px;
}
@media screen and (max-width:768px){
    .header{
         display: flex;
         justify-content: space-between;
     }
    .menu-button{
        color:#fff;
        display: block;
        /* position: absolute; */
        float: left;
        cursor: pointer;
        font-size: 30px;
        margin: 10px;
        z-index: 500;
    }
    .menulist{
        display: none;
    }
    .btn{
        float: right;
        margin: 0px;

    }
    .logo{
        height: 8vh;
        /* width: 10vh;  */
        margin: 0 0 0 10px ;
    }
    #item-1{
        display: block;
    }
    #item-2{
        flex-grow: 3;

    
    }
    #item-3{
        display: none;
    }
  } 
  @media screen and (max-width:428px){ 
     .header{
         display: flex;
         justify-content: space-between;
     }
    .menu-button{
        color:#fff;
        display: block;
        /* position: absolute; */
        float: left;
        cursor: pointer;
        font-size: 30px;
        margin: 10px;
        z-index: 500;
    }
    .menulist{
        display: none;
    }
    .btn{
        float: right;
        margin: 0px;

    }
    .logo{
        height: 8vh;
        /* width: 10vh;  */
        margin: 0 0 0 10px ;
    }
    #item-1{
        display: block;
    }
    #item-2{
        flex-grow: 3;

    
    }
    #item-3{
        display: none;
    }
} 

.signindiv{
  text-align: center;
  font-family: cursive;
  z-index: 30000;
}
.signin {
  text-align: center;
  white-space: nowrap;
  color: #00898e;
}
a {
  text-decoration: none;
  /* color: #fff; */
}
.btn {
  height: 30px;
  width: 30px;
  display: inline-block;
  padding: 10px 10px;
  border-radius: 50%;
  transition: background 0.3s;
}
.btn img{
  height: 30px;
  width: 30px;
}
.btn:hover {
  background: #00898e;
}
.popup {
  position: fixed;
  padding: 10px;
  max-width: 500px;
  height: 65vh;
  border-radius: 10px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  visibility: hidden;
  opacity: 0;
  /* "delay" the visibility transition */
  -webkit-transition: opacity 0.5s, visibility 0s linear 0.5s;
  transition: opacity 0.5s, visibility 0s linear 0.5s;
  z-index: 1;
}
.popup:target {
  visibility: visible;
  opacity: 1;
  /* cancel visibility transition delay */
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
}
.popup-close {
  position: absolute;
  padding: 10px;
  max-width: 500px;
  border-radius: 10px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, 0.9);
}
.popup .close {
  position: absolute;
  right: 5px;
  top: 5px;
  padding: 5px;
  color: #000;
  transition: color 0.3s;
  font-size: 2em;
  line-height: 0.6em;
  font-weight: bold;
}
.popup .close:hover {
  color: #00e5ee;
}

.close-popup {
  background: rgba(0, 0, 0, 0.7);
  cursor: default;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0;
  visibility: hidden;
  /* "delay" the visibility transition */
  -webkit-transition: opacity 0.5s, visibility 0s linear 0.5s;
  transition: opacity 0.5s, visibility 0s linear 0.5s;
}
.popup:target + .close-popup {
  opacity: 1;
  visibility: visible;
  /* cancel visibility transition delay */
  -webkit-transition-delay: 0s;
  transition-delay: 0s;
}
/* popup Form */
form{
	max-width: 350px;
	margin: 20px 0;
}
form input{
	width: 100%;
	padding: 12px 10px;
	margin-bottom: 5px;
	outline: none;
	box-shadow: none;
	box-sizing: border-box;
	border:2px solid rgb(75, 73, 73);
}
.btn-box{
	width: 100%;
	display: flex;
	justify-content: center;
}
.btn-box button{
	flex-basis: 48%;
  padding: 10px 0;
  font-size: 15px;
}
p .forgot{
  color: green;
  cursor: pointer;
  text-align: center;
}
.stext{
  justify-content: center;
  margin: 0;
  text-align: center;
}
.singinoption{
  height: 60px;
  width: 80%;
  transform: translate(13%, 20%);
}
.sicon{
  height: 60px;
  width: 60px;
  line-height: 60px;
  font-size: 30px;
  margin: 10px;
}
.sicon img{
  height: 50px;
  width: 50px;
}
/* responsive */
@media  (max-width:768px){
 .popup{
   max-width: 700px;
   height: 75vh;
 }
}
@media  (max-width:428px){
  .popup{
    width: 80%;
    height: 75vh;
  }
}


</style>