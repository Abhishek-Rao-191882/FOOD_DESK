<template>
  <div class="home">


    <!--searchbar-->
<div class="slider_main">
  <div class="searchbox">
    <form>
      <input style="background-color:#fff;" type="text" name="search" placeholder="Search Food Or Resturants..."/>
      <input type="submit" name="submit" placeholder="search" />
    </form>
  </div> 
 <!--searchbox end-->

 <!--slider-->

  <div class="slider">
    <!-- <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../assets/chillipaneer.jpeg" class="d-block w-100" alt="..." style="height: 60vh; width: 100%;"/>
        </div>
        <div class="carousel-item">
          <img src="../assets/chillipaneer.jpeg" class="d-block w-100" alt="..." style="height: 60vh; width: 100%;"/>
        </div>
        <div class="carousel-item">
          <img src="../assets/chillipaneer.jpeg" class="d-block w-100" alt="..." style="height: 60vh; width: 100%;"/>
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>   -->
  

  <!-- <v-carousel  :show-arrows="false" style="z-index:-10"> -->
    <v-carousel
    cycle
    height="auto"
    hide-delimiter-background
    :show-arrows="false"
    style="z-index:-10"
  >
    <v-carousel-item v-for="i in 3" :key="i">
      
      <v-sheet>
        <img src="../assets/chillipaneer.jpeg" style="height: 60vh; width: 100%;">
      </v-sheet>

    </v-carousel-item>

  </v-carousel>

</div> 
</div>
    <!--slider end-->




    <!--symbol box-->
    <div class="symbols">
      <ul>
        <li>
          <a href="#">
            <div class="icon">
              <i class="fa fa-pagelines" aria-hidden="true"></i>
              <i class="fa fa-pagelines" aria-hidden="true"></i>
            </div>
            <div class="name">
              <span data-text="Safe And Hygenic">Safe And Hygenic</span>
            </div>
          </a>
        </li>
        <li>
          <a href="#">
            <div class="icon">
              <i class="fa fa-motorcycle" aria-hidden="true"></i>
              <i class="fa fa-motorcycle" aria-hidden="true"></i>
            </div>
            <div class="name">
              <span data-text="Superfast Delivery">Superfast Delivery</span>
            </div>
          </a>
        </li>
        <li>
          <a href="#">
            <div class="icon">
              <i class="fa fa-free-code-camp" aria-hidden="true"></i>
              <i class="fa fa-free-code-camp" aria-hidden="true"></i>
            </div>
            <div class="name">
              <span data-text="Tasty Food">Tasty Food</span>
            </div>
          </a>
        </li>
        <li>
          <a href="#">
            <div class="icon">
              <i class="fa fa-credit-card-alt" aria-hidden="true"></i>
              <i class="fa fa-credit-card-alt" aria-hidden="true"></i>
            </div>
            <div class="name">
              <span data-text="Pocket Friendly">Pocket Friendly</span>
            </div>
          </a>
        </li>
        <li>
          <a href="#">
            <div class="icon">
              <i class="fa fa-cutlery" aria-hidden="true"></i>
              <i class="fa fa-cutlery" aria-hidden="true"></i>
            </div>
            <div class="name">
              <span data-text="Veg And Non veg">Veg And Non Veg</span>
            </div>
          </a>
        </li>
      </ul>
    </div>  
 <!--symbol box end-->




    <!--cart-->
<div class="main">
  <h1><span class="resto">Favourite Dishes</span></h1>
      <!--cards -->
  <div class="break">
    <div class="part">
      <div class="square">
        <div class="photo">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Gfp-missouri-st-louis-clubhouse-pond-and-scenery.jpg/1199px-Gfp-missouri-st-louis-clubhouse-pond-and-scenery.jpg"/>
        </div>
        <div class="write">
          Potato Chilli
        </div>
        <div class="des">
          <p>PK Resturants</p>
          <p>Price = Rs70</p>
          <a href="home"> <button>Add To Cart</button></a>
        </div>
      </div>
      <!--cards -->
      <div class="square">
        <div class="photo">
          <img src="https://cdn.pixabay.com/photo/2015/11/07/11/41/lake-1031405_1280.jpg" />
        </div>
        <div class="write">
          Chicken Gravy
        </div>
        <div class="des">
          <p>Chicken Centre</p>
          <p>Price = Rs200</p>
          <a href="home"> <button>Add To Cart</button></a>
        </div>
      </div>
    </div>
      <!--cards -->
  <div class="part">
      <div class="square">
        <div class="photo">
          <img
            src="https://cdn.pixabay.com/photo/2018/01/09/03/49/the-natural-scenery-3070808_1280.jpg"
          />
        </div>
        <div class="write">
          Paneer Momos
        </div>
        <div class="des">
          <p>PK Resturant</p>
          <p>Price = Rs50</p>
          <a href="home"> <button>Add To Cart</button></a>
        </div>
      </div>
      <!--cards -->
      <div class="square">
        <div class="photo">
          <img
            src="https://cdn.pixabay.com/photo/2018/01/09/03/49/the-natural-scenery-3070808_1280.jpg"
          />
        </div>
        <div class="write">
          Paneer Pizza
        </div>
        <div class="des">
          <p>Pizza Cafe</p>
          <p>Price = Rs180</p>
          <a href="home"> <button>Add To Cart</button></a>
        </div>
      </div>
    </div>
  </div>
  
  <!--2nd box part-->
    <div class="break">
      <div class="part">
      <!--cards -->
      <div class="square">
        <div class="photo">
          <img
            src="https://cdn.pixabay.com/photo/2018/01/09/03/49/the-natural-scenery-3070808_1280.jpg"
          />
        </div>
        <div class="write">
          Veg Burger
        </div>
        <div class="des">
          <p>Ashoka Hotel</p>
          <p>Price = Rs20</p>
          <a href="home"> <button>Add To Cart</button></a>
        </div>
      </div>
      <!--cards -->
      <div class="square">
        <div class="photo">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Gfp-missouri-st-louis-clubhouse-pond-and-scenery.jpg/1199px-Gfp-missouri-st-louis-clubhouse-pond-and-scenery.jpg"
          />
        </div>
        <div class="write">
          Aaloo Paratha
        </div>
        <div class="des">
          <p>Ashoka Hotel</p>
          <p>Price = Rs30</p>
          <a href="home"> <button>Add To Cart</button></a>
        </div>
      </div>
  </div>
      <!--cards -->
      <div class="part">
      <div class="square">
        <div class="photo">
          <img
            src="https://cdn.pixabay.com/photo/2018/01/09/03/49/the-natural-scenery-3070808_1280.jpg"
          />
        </div>
        <div class="write">
          Paneer Pyaza
        </div>
        <div class="des">
          <p>Royal Plaza</p>
          <p>Price = Rs120</p>
          <a href="home"> <button>Add To Cart</button></a>
        </div>
      </div>
      <!--cards -->
      <div class="square">
        <div class="photo">
          <img
            src="https://cdn.pixabay.com/photo/2015/11/07/11/41/lake-1031405_1280.jpg"
          />
        </div>
        <div class="write">
          Potato Chilli
        </div>
        <div class="des">
          <p>Ashoka Hotel</p>
          <p>Price = Rs30</p>
          <a href="home"> <button>Add To Cart</button></a>
        </div>
      </div>
    </div>
  </div>
</div>


    <!--cart end-->




    <!--Resturants-->
    
      <h1><span class="resto">RESTURANTS</span></h1>
    
    
    <div class="cards-list">
      <div class="shopCard">
        <div class="card_image">
          <img src="https://i.redd.it/b3esnz5ra34y.jpg" />
        </div>
        <div class="card_title title-white">
          <p>Ashoka Hotel</p>
        </div>
      </div>

      <div class="shopCard">
        <div class="card_image">
          <img src="https://i.redd.it/b3esnz5ra34y.jpg" />
        </div>
        <div class="card_title title-white">
          <p>Royal Plaza</p>
        </div>
      </div>

      <div class="shopCard">
        <div class="card_image">
          <img src="https://i.redd.it/b3esnz5ra34y.jpg" />
        </div>
        <div class="card_title title-white">
          <p>PK Resturant</p>
        </div>
      </div>
    </div>

    <div class="cards-list">
      <div class="shopCard">
        <div class="card_image">
          <img src="https://i.redd.it/b3esnz5ra34y.jpg" />
        </div>
        <div class="card_title title-white">
          <p>Pizza Cafe</p>
        </div>
      </div>

      <div class="shopCard">
        <div class="card_image">
          <img src="https://i.redd.it/b3esnz5ra34y.jpg" />
        </div>
        <div class="card_title title-white">
          <p>Chicken Centre</p>
        </div>
      </div>

      <div class="shopCard">
        <div class="card_image">
          <img src="https://i.redd.it/b3esnz5ra34y.jpg" />
        </div>
        <div class="card_title title-white">
          <p>Hostel Canteen</p>
        </div>
      </div>
    </div>
  

    <!--resturants end-->


<!-- footer-->

<footer>
<div class="main-content">
  <div class="left box">
    <h2>About us</h2>
    <div class="content">
        <p> We the TEAM DESSPER and students of Central University
         Of Haryana started the online food
         delivery for you as a small startup and to ease the life of 
         students of university who lives in hostel or nearby PG. We cover almost
         all the resturants nearby so that you get the best food 
         options. Hope you will enjoy our service and appreciate our effort.
         </p>
    </div>
  </div>
  <div class="center box">
    <h2>Address</h2>
    <div class="content">
      <div class="place">
          <span class="iicon fa fa-map-marker" aria-hidden="true"></span>
          <span class="text">Central University Of Haryana</span>
      </div>
      <div class="phone">
          <span class="iicon fa fa-phone"></span>
          <span class="text">+91 8252988705</span>
      </div>
      <div class="email">
          <span class="iicon fa fa-envelope"></span>
          <span class="text">ss4094061@gmail.com</span>
      </div>
    </div>
  </div>
  <div class="right box">

    <div class="log">FOOD <span>DESK</span></div>
  
    <div class="social">

       
      <a href="" class="sicon fa fa-facebook" aria-hidden="true"></a>
      <a href="" class="sicon fa fa-instagram" aria-hidden="true"></a>
      <a href="" class="sicon fa fa-twitter" aria-hidden="true"></a>
      <a href="" class="sicon fa fa-github" aria-hidden="true"></a>
      <a href="" class="sicon fa fa-linkedin" aria-hidden="true"></a>
    </div>
  
    <div class="bottom">
        <center>
          <span class="credit">Created By <a href="">DASSPER</a> | </span>
          <span class="fa fa-copyright"></span> 2020 All rights reserved.
        </center>
    </div>
  </div>
</div>
</footer>



  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  data() {
    return {
      store: '',
      store2: '',

      msg:'Sourabh',
      images:["@/assets/chillipaneer.jpeg"],
    }
  },
  name: 'Home',
  components: {
    HelloWorld
  },

  mounted(){
    
  },

  methods:{

  }



}
</script>













<style scoped>


* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}
body {
  font-family: arial;
}


/*searchbar*/
form {
  width: 100%;

  margin-top: 14vh;
}
input[type="text"] {
  width: 80%;
  padding: 15px;
  border: none;
  font-size: 18px;
  font-family: "Comfortaa", cursive;
  border-radius: 5px 0 0 5px;
}
input[type="submit"] {
  padding: 15px;
  border: none;
  font-size: 18px;
  font-family: "Comfortaa", cursive;
  background: orange;
  color: white;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  position: absolute;
}
/* @media screen and (max-width: 300px) {
  form {
    width: 100%;
  }
  .searchbox{
    justify-content: center;
    margin-right: 100px;
  }
  input[type="text"] {
    width: 60%;
  
    border-radius: 5px;
    padding: 10px;
  }

  input[type="submit"] {
    border-radius: 5px;
    width: 100%;
    margin-top: 5px;
    padding: 10px;
    position: absolute;
  }
} */

/*searchbar ends*/

/* Slideshow */

body {
  font-family: "Comfortaa", cursive;
}
.mySlides {
  display: none;
}
img {
  vertical-align: middle;
}

.slideshow-container {
  max-width: 1000px;
  width: 100%;
  height: 30%;
  position: relative;
  margin: auto;
  margin-top: -10px;
}

.active {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {
    opacity: 0.4;
  }
  to {
    opacity: 1;
  }
}

@keyframes fade {
  from {
    opacity: 0.4;
  }
  to {
    opacity: 1;
  }
}

/* On smaller screens, decrease text size */

.slider_main {
  width: 100%;
  height: 100%;
}

.searchbox {
  position: absolute;
  left: 20%;
  right: 20%;
  z-index: -8;
  box-sizing: border-box;
}
/*slider end*/





/*symbol minibar*/
.symbols {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
}
.symbols ul {
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: -8;
  transform: translate(-50%, -50%);
  margin: 0;
  padding: 1vh 0;
  background: yellow;
  display: flex;
  border-radius: 10px;
  box-shadow: 0 1vh 3vh rgba(0, 0, 0, 0.3);
}
.symbols ul li {
  list-style: none;
  text-align: center;
  display: block;
  border-right: 1px solid rgba(0, 0, 0, 0.2);
}
.symbols ul li:last-child {
  border-right: none;
}
.symbols ul li a {
  text-decoration: none;
  padding: 0 1vh;
  display: block;
}
.symbols ul li a .icon {
  width: 5.3vh;
  height:6vh;
  text-align: center;
  overflow: hidden;
  margin: 0 auto 1vh;
}
.symbols ul li a .icon .fa {
  width: 100%;
  height: 100%;
  line-height: 7vh;
  font-size: 4vh;
  transition: 0.5s;
  color: #000;
}
.symbols ul li a .icon .fa:last-child {
  color: #e91e63;
}
.symbols ul li a:hover .icon .fa {
  transform: translateY(-100%);
}
.symbols ul li a .name {
  position: relative;
  height: 30px;
  width: 150px;
  display: block;
  overflow: hidden;
}
.symbols ul li a .name span {
  width: 100%;
  display: block;
  position: relative;
  color: #000;
  font-size: 17px;
  line-height: 40px;
  transition: 0.5s;
  font-weight: bolder;
}
.symbols ul li a .name span:before {
  content: attr(data-text);
  position: absolute;
  top: -100%;
  left: 0;
  width: 100%;
  height: 100%;
  color: #e91e63;
}
.symbols ul li a:hover .name span {
  transform: translateY(40px);
}
 @media screen and (max-width: 820px) {
  .symbols ul{
    width: 98%;
  }
  .symbols ul li{
    display: flex;
    flex-grow: 1;
    justify-content: center;
  }
   .symbols ul li a .icon{
    width: 24px;
    height: 36px;
    
  }
  .symbols ul li a .icon .fa{
    font-size: 18px;
    font-weight: bold;
  }        
  .symbols ul li a .name{
    width: 58px;
  }  
  .symbols ul li a .name span{
    font-size: 6.6px;
    font-weight: bolder;
    text-align: center;
  }
}  
/*symbolbox end*/





/* cart start */
h1 {
  text-align: center;
  font-style: italic;
  color: green;
  margin: 100px auto;
  max-width: 600px;
  z-index: -10;
  position: relative;
}
h1:before {
  content: "";
  display: block;
  width: 120px;
  height: 2px;
  background: green;
  position: absolute;
  left: 0;
  top: 50%;
  z-index: -2;
}
h1:after {
  content: "";
  display: block;
  width: 120px;
  height: 2px;
  background: green;
  position: absolute;
  right: 0;
  top: 50%;
  z-index: -2;
}
.resto {
  background: #fff;
}
.main {
  margin: 2%;
}
.break {
  display: flex;
  flex-direction: row;
}
.part {
  display: flex;
  flex-direction: row;
}

.square {
  display: inline-block;
  box-shadow: 2px 2px 20px black;
  border-radius: 5px;
  margin: 6%;
  flex: 1;
}

.photo img {
  width: 100%;
  border-top-right-radius: 5px;
  border-top-left-radius: 5px;
}

.write {
  text-align: center;
  padding: 3px;
  font-weight: bold;
  font-size: 30px;
}

.des {
  padding: 20px;
  margin: 0px;
  font-weight: bold;
  text-align: center;

  padding-top: 10px;
  border-bottom-right-radius: 5px;
  border-bottom-left-radius: 5px;
}
button {
  margin-top: 40px;
  margin-bottom: 10px;
  background-color: white;
  border: 1px solid black;
  border-radius: 5px;
  padding: 10px;
  font-weight: bold;
}
button:hover {
  background-color: orangered;
  color: white;
  transition: 0.5s;
  cursor: pointer;
}
@media screen and (max-width: 725px) {
  .part {
    display: flex;
    flex: 1;
    flex-direction: column;
  }
  .square {
    display: flex;
    flex-direction: column;
    flex: 2;
  }
  .des {
    font-size: 14px;
  }
  .write{
    font-size: 18px;
  }
}

/*cart end*/

/* resturants*/
.cards-list {
  z-index: 0;
  width: 100%;

  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.shopCard {
  margin: 30px auto;
  width: 300px;
  height: 300px;
  border-radius: 40px;
  box-shadow: 5px 5px 30px 7px rgba(0, 0, 0, 0.25),
    -5px -5px 30px 7px rgba(0, 0, 0, 0.22);
  cursor: pointer;
  transition: 0.4s;
}

.shopCard .card_image {
  width: inherit;
  height: inherit;
  background-color: #33ffff;
  border-radius: 4000px;
}

.shopCard .card_image img {
  width: inherit;
  height: inherit;
  border-radius: 40px;
  object-fit: cover;
}

.shopCard .card_title {
  text-align: center;
  border-radius: 0px 0px 40px 40px;
  font-family: sans-serif;
  font-weight: bold;
  font-size: 30px;
  margin-top: -80px;
  height: 40px;
}

.shopCard:hover {
  transform: scale(0.9, 0.9);
  box-shadow: 5px 5px 30px 15px rgba(0, 0, 0, 0.25),
    -5px -5px 30px 15px rgba(0, 0, 0, 0.22);
}

.title-white {
  color: white;
}

.title-black {
  color: black;
}

/*footer*/

@import url("https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap");

footer {
  position: relative;
  bottom: 0px;
  width: 100%;
  background: #111;
}
.main-content {
  display: flex;
}
.main-content .box {
  flex-basis: 50%;
  padding: 10px 20px;
}
.box {
  display: inline-block;
  box-shadow: 2px 2px 20px black;
  border-radius: 5px;
  margin: 2%;
  flex: 1;
}
.box h2 {
  font-size: 1.125rem;
  font-weight: 600;
  text-transform: uppercase;
}
.box .content {
  margin: 20px 0 0 0;
  position: relative;
}
.box .content:before {
  position: absolute;
  content: "";
  top: -10px;
  height: 2px;
  width: 100%;
  background: #1a1a1a;
}
.box .content:after {
  position: absolute;
  content: "";
  height: 2px;
  width: 15%;
  background: #f12020;
  top: -10px;
}
.left .content p {
  text-align: justify;
}

.center .content .iicon {
  font-size: 1.4375rem;
  background: #1a1a1a;
  height: 45px;
  width: 45px;
  line-height: 45px;
  text-align: center;
  border-radius: 50%;
  transition: 0.3s;
  cursor: pointer;
}
.center .content .iicon:hover {
  background: #f12020;
}
.center .content .text {
  font-size: 1.0625rem;
  font-weight: 500;
  padding-left: 10px;
}
.center .content .phone {
  margin: 15px 0;
}
/*social*/
.social {
  display: flex;
  justify-content: center;
}
.sicon {
  border-radius: 50%;
  padding: 20px;
  font-size: 0.8em;
  width: 50px;
  text-align: center;
  text-decoration: none;
  margin: 8px 6px;
  margin-left: 10px;
}

.sicon:hover {
  opacity: 0.7;
}

.fa-facebook {
  background: #007bb5;
  color: white;
}

.fa-twitter {
  background: #fffc00;
  color: white;
}
.fa-github {
  background: #55acee;
  color: white;
}

.fa-linkedin {
  background: #007bb5;
  color: white;
}

.fa-instagram {
  background: #007bb5;
  color: white;
}

/*end social*/
.log {
  color: #fff;
  font-size: 50px;
  text-transform: uppercase;
  font-weight: 900;
  margin-bottom: 20px;
  margin-top: 20px;
  margin-left: 15%;
}

 .log span{
  color: #4CCEE8;
}

.bottom center {
  padding: 5px;
  font-size: 0.9375rem;
  margin-bottom: 1px;
  background: #151515;
}
.bottom center span {
  color: #656565;
}
.bottom center a {
  color: #f12020;
  text-decoration: none;
}
.bottom center a:hover {
  text-decoration: underline;
}
@media screen and (max-width: 900px) {
  footer {
    position: relative;
    bottom: 0px;
  }
  .main-content {
    flex-wrap: wrap;
    flex-direction: column;
  }
  .main-content .box {
    margin: 5px 0;
  }
}

/* responsive */

@media all and (max-width: 425px) {
  .card-list {
    /* On small screens, we are no longer using row direction but column */
    flex-direction: column;
  }
}

@media only screen and (max-width: 525px) {
  .text {
    font-size: 11px;
  }
  .log{
    margin-top: 0;
    margin-bottom: 0;
    margin-left:24%;
    font-size: 40px;
  }
}




</style>
