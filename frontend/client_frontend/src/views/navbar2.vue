<template>
    <div>
         <!-- navbar starts -->

      <div class="completeheader">
        <!-- {{$store}} -->
      <div class="head">
        <nav class="header">
        <div class="item" id="item-1">
          <div class="menu-button" id="menu-button">&#9776;</div>
        </div>
        <div class="item" id="item-2">
          <img class="logo" src="../assets/logo.png" alt="" />
        </div>
        <div class="item" id="item-3">
          <div class="searchbox">
            <input type="text" class="searchinput" v-model="search_text">
            <router-link :to="{ name:'Search' , query: {'searching_data':search_text}}" style="text-decoration: none;" >
            <button class="searchsubmit"><img src="../assets/searchicon.png" alt=""></button>
            </router-link>
          </div>
          <div class="signin">
            <a v-if="$store.state.email == ''" href="#" id="myImg">Sign In</a>
          </div>
        </div>
        <div class="item" id="item-4">
          <router-link :to="{ name:'Cart'}">
          <a  class="cart"><img src="../assets/cart.png" alt=""></a>
          </router-link>
        </div> 
        </nav>
        <div class="searchbox1">
            <input type="text" class="searchinput1" v-model="search_text">
            <router-link :to="{ name:'Search' , query: {'searching_data':search_text}}" style="text-decoration: none;" >
            <button class="searchsubmit1" ><img src="../assets/searchicon.png" alt=""></button>
            </router-link>
        </div>
        </div>

         <div class="searchboxwithcart" id="searchboxwithcart">
          <div class="menubar1">
             <div class="menu-button1" id="menu-button2">&#9776;</div>
          </div>
          <div class="seachbox2">
            <input type="text" class="searchinput2" v-model="search_text">
            <router-link :to="{ name:'Search' , query: {'searching_data':search_text}}" style="text-decoration: none;" >
            <button class="searchsubmit2" ><img src="../assets/searchicon.png" alt=""></button>
            </router-link>
          </div>
          <div class="cartmobile">
            <router-link :to="{ name:'Cart'}">
            <a  class="cart1"><img src="../assets/cart.png" alt=""></a>
            </router-link>
          </div>
        </div>
      </div>
      <!-- navbar ends -->

      <!-- sidebar starts -->
      <nav id="hide-menu" class="hide-menu">
        <div class="photopart">
        <div class="introbox">
          <img class="custimg" src="../assets/login.png" alt="">
          <p class="hiCustomer">
            Hi, 
            <span v-if="$store.state.email == ''">There</span>
            <span v-else>{{$store.state.first_name}} {{$store.state.last_name}}</span>

          </p>
          
          <p></p>
          <!-- <p>FoodDesk2020@gmail.com</p> -->
        </div>
        </div>
        <div class="linksmaindiv">
          <div class="linkslist">
            <div class="links" ><router-link :to="{name:'home'}" class="link"><img class="linkicon" src="../assets/home.png" alt=""><a class="linkdev" href="#">Home</a></router-link></div>
            <div class="links" v-if="$store.state.email != ''"><img class="linkicon" src="../assets/active orders.png" alt=""><a class="linkdev" href="#">Orders</a></div>
            <div class="links" ><router-link :to="{name:'Products'}" class="link"><img class="linkicon" src="../assets/active orders.png" alt=""><a class="linkdev" href="#">Products</a></router-link></div>
            <div class="links" v-if="$store.state.email != ''"><img class="linkicon" src="../assets/delivered orders.png" alt=""><a class="linkdev" href="#">Delivered Orders</a></div>
            <div class="links"><img class="linkicon" src="../assets/select hotel.png" alt=""><a class="linkdev" href="#">Hotels</a></div>
          </div>
          <hr>
          <p class="communicate">Communicate</p>
          <div class="linkslistdev">
            <div class="links"><img class="linkicon" src="../assets/share1.png" alt=""><a class="linkdev" href="#">Share</a></div>
            <div class="links"><img class="linkicon" src="../assets/contact us1.png" alt=""><a class="linkdev" href="#">Contact Us</a></div>
            <div class="links"><img class="linkicon" src="../assets/about develpoers.png" alt=""><a class="linkdev" href="#">About Developers</a></div>
          </div>
          <hr>
          <div class="linkslistdev">
          <div class="links"><router-link :to="{name:'User_Settings'}" class="link"><img class="linkicon" src="../assets/contact us1.png" alt=""><a class="linkdev" href="#">Settings</a></router-link></div>
          <div class="links" v-if="$store.state.email == ''"><router-link :to="{name:'Sign_Up'}" class="link"><img class="linkicon" src="../assets/contact us1.png" alt=""><a class="linkdev" href="#">Sign Up</a></router-link></div>
          <div class="links" v-if="$store.state.email == ''"><router-link :to="{name:'Login'}" class="link"><img class="linkicon" src="../assets/contact us1.png" alt=""><a class="linkdev" href="#">Sign In</a></router-link></div>
          <div class="links" @click="logout" v-else><img class="linkicon" src="../assets/contact us1.png" alt="" /><a class="linkdev" href="#">Logout</a></div>
          </div>
        </div>
      </nav>

      <!-- sidebar Ends -->

      <!-- sign in popup starts -->
      <div id="myModal" class="modal">
        <span class="close">&times;</span>
        <!-- <img class="modal-content" id="img01"> -->
        <div id="popup1 img01" class="popup modal-content">
          <h2 class="signin">Sign in</h2>
          <form action="" method="get">
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
        
      </div>



      <!-- sign in popup ends -->

      <div class="views">

      <router-view>
        
      </router-view>

    </div>



    </div>
</template>

<script>
 import $ from 'jquery'
import products from './Products'
import API from '../API/API'


export default {
  data(){
    return{
      search_text:'',
      
    }
  },
    mounted(){
      var modal = document.getElementById("myModal");
      var img = document.getElementById("myImg");
      var modalImg = document.getElementById("img01");
      var modal = document.getElementById('myModal');
      var span = document.getElementsByClassName("close")[0];

      img.onclick = function(){
      modal.style.display = "block";
      modalImg.src = this.src;
    }

     
     span.onclick = function() { 
       modal.style.display = "none";
     }

     
     window.onclick = function(event) {
       if (event.target == modal) {
         modal.style.display = "none";
     }
    }
    window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    document.getElementById("searchboxwithcart").style.display = "block";
      
  } else {
    document.getElementById("searchboxwithcart").style.display = "none";
  }
}

  $('#menu-button').click(function(e){
        e.stopPropagation();
        $('#hide-menu').toggleClass('show-menu');
  });


  $('#menu-button2').click(function(e){
        e.stopPropagation();
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
    },
    methods:{
      
      logout(){
      const token = localStorage.getItem('token')
      API.log_out(token)
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
*{
    margin: 0;
    padding: 0;
}
.views{
  padding-top: 10vh;
  height: 90vh;
  width: 100%;
  /* background-color: #00e5ee; */
}


body{
    overflow:hidden;
    margin: 0;
    padding: 0;
}
/* navbar starts */
.header {
    background: linear-gradient(135deg,#EC8197 , #EE9f63, #2382F8 );
    height: 10vh;
    width: 100%;
    z-index: 10;
    position: fixed;
    display: flex;
    margin: 0;
    align-items: center;
}
.item{
    margin: 0;
}
/* #item-1{
display: none;
} */
/* #item-2{

    
} */
#item-3{
    display: flex;
    flex-grow: 5;
    float: right;
    justify-content: space-between;
}
/* #item-4{
    
} */
/* .menu-button{
    display: none;
} */
.searchbox{
  display: inline-block;
  position: relative;
  /* width: 100%; */
  margin: 0 10px 0 40px;
}
.signin a{
  color: #f1f1f1;
  text-decoration: none;
  font-size: 20px;
}

.searchinput {
  width: 1000px;
  height: 35px;
  border: 0;
  background: white;
  border-radius: 10px 10px 10px 10px;  
  transition: all 0.3s;
  padding: 15px;
}

.searchsubmit {
  width: 50px;
  height: 35px;
  background-color: #99dff9;
  color: #fff;
  border: 0;
  position: absolute;
  top: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 0 10px 10px 0;
}
.searchsubmit img{
  width: 35px;
  height: 35px;
}
.searchboxwithcart{
  display: none;
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
.logo{
    height: 8vh;
    /* width: 10vh; */
    margin-left: 55px  ;
    /* border: 1px solid red; */
}
.cart {
    height: 40px;
    width: 40px;
    display: inline-block;
    /* padding: 10px 10px; */
    border-radius: 50%;
    transition: background 0.3s;
    margin: 0px 20px  ;
    /* border: 1px solid red; */
  }
  .cart img{
    height: 30px;
    width: 40px;
  }
  .cart:hover {
    cursor: pointer;
  }
  .menulist{
      list-style: none;
      display: flex;
      float: right;
      justify-content: center;
      align-items: center;
      font-weight: 800;
  }
  .menulist .list{
    height: 35px;
    font-size: 1.2rem;
    /* border: 1px solid red; */
    margin-right: 40px;
    /* margin-top: 15px; */
    text-align: center;
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




/* navbar ends */

/* side bar starts */



.hide-menu{
    background-color:#f9f9fa;
    position: fixed;
    top:0;
    left:0;
    width: 20%;
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
     
 }
 .hide-menu .photopart p{
     font: 15px;
     line-height: 20px;
     /* margin: 0 0 20px 0; */
     text-align: center;
 }
 .hide-menu .photopart p a{
     text-decoration: none;
 }
.hide-menu .linksmaindiv .linkslist{
     list-style: none;
     margin: 0;
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
     text-decoration: none;
     
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
    text-decoration: none;
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
/* sidebar ended */

/* sign in popup starts */
.modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1000; /* Sit on top */
    padding-top: 100px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
    text-align: center;
    font-family: cursive;
  }
  
  /* Modal Content (image) */
  .modal-content {
    margin: auto;
    display: block;
    width: 80%;
    height: auto;
    max-width: 700px;
  }

  
  /* The Close Button */
  .close {
    position: absolute;
    top: 15px;
    right: 35px;
    color: #f1f1f1;
    font-size: 40px;
    font-weight: bold;
    transition: 0.3s;
  }
  
  .close:hover,
  .close:focus {
    color: #bbb;
    text-decoration: none;
    cursor: pointer;
  }
  .searchbox1{
    display: none;
  }
  .searchboxwithcart{
    display: none;
  }
  .cart1{
    display: none;
  }
  .searchbox2{
    display: none;
  }
  .searchsubmit2{
    display: none;
  }

/* sign in popup ends */

  /* responsive  */
   @media screen and (max-width:1024px){
   
      .menulist .list{
        margin-right: 15px;
        font-size: 18px;
      }
      .searchinput {
         width: 500px;}
   }
  /* for Tablet view */

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
        margin: 0 0 0 0px ;
    }
    #item-1{
        display: block;
    }
    #item-2{
        flex-grow: 3;
    }
    .searchinput {
       width: 400px;}
    /* #item-3{
        display: none;
    } */
    .hide-menu{
      width: 30%;
    }
    .modal-content {
        width: 45%;
      }
  } 
  /* for mobile view */
  @media screen and (max-width:428px){ 
     .head{
       height: 17vh;
       background: linear-gradient(135deg,#EC8197 , #EE9f63, #2382F8 );
       position: relative;
     }
     .header{
         display: flex;
         justify-content: space-between;
         background: none;
          position: relative;
     }
     .searchbox1{
         display: inline-block;
         position: relative;
         width: 90%;
         margin: 0 0 0 15px;
         /* align-content: center; */
         /* text-align: center; */
     }


      .searchinput1 {
        background: white;
         width: 90%;
         height: 35px;
         border: 0;
         border-radius: 10px;  
         transition: all 0.3s;
         padding: 15px; 
     }

      .searchsubmit1 {
         width: 50px;
         height: 35px;
         background-color: #99dff9;
         color: #fff;
         border: 0;
         position: absolute;
         top: 0;
         right: 0;
         display: flex;
         justify-content: center;
         align-items: center;
         border-radius: 0 10px 10px 0;
     }
     .searchsubmit1 img{
         width: 35px;
         height: 35px;
     }
    .searchboxwithcart{
         width: 100%;
         z-index: 1;
         display: none;
         justify-content: space-between;
         height: 10vh;
         background: linear-gradient(135deg,#EC8197 , #EE9f63, #2382F8 );
         position: fixed;
         margin-top: 0;
         top: 0;
     }
     .searchbox2{
         display: block;
         position: absolute;
         width: 70%;
         margin: 10px 0 0 15px;
         /* align-content: center; */
         /* text-align: center; */
     }
     .searchinput2 {
       background: white;
         width: 70%;
         height: 30px;
         border: 0;
         position: absolute;
         top: 10px;
         border-radius: 10px;  
         transition: all 0.3s;
         padding: 15px;
     }

     .searchsubmit2 {
         width: 35px;
         height: 30px;
         background-color: #99dff9;
         color: #fff;
         border: 0;
         position: absolute;
         top: 10px;
         right: 60px;
         display: block;
         /* display: flex;
         justify-content: center;
         align-items: center; */
         border-radius: 0 10px 10px 0;
     }
     .searchsubmit2 img{
         width: 35px;
         height: 30px;  
     }
     .cart1 {
         height: 40px;
         width: 40px;
         display: inline-block;
         /*   padding: 10px 10px; */
         border-radius: 50%;
         transition: background 0.3s;
         /* margin: 0px 20px  ; */
         /* border: 1px solid red; */
         position: absolute;
         top: 10px;
         right: 10px;

     }
     .cart1 img{
         height: 30px;
         width: 40px;
     }
     .cart1:hover {
         cursor: pointer;
     }
     .menu-button1{
         color:#fff;
         display: block;
         /* position: absolute; */
         float: left;
         cursor: pointer;
         font-size: 30px;
         margin: 0 10px 0 10px;
         z-index: 500;
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
    .hide-menu{
      width: 80%;
    }    
    .modal-content {
        width: 100%;
      }


        .views{
  padding-top: 0vh;
  height: 90vh;
  width: 100%;
  /* background-color: #00e5ee; */
}

} 


/* .singindiv{
  text-align: center;
  font-family: cursive;
} */
.signin {
  text-align: center;
  white-space: nowrap;
  color: #00898e;
}
a {
  text-decoration: none;
  /* color: #fff; */
}
/* .btn {
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
} */
.popup {
  position: fixed;
  padding: 10px;
  max-width: 360px;
  height: 65vh;
  border-radius: 10px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  z-index: 30000;
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