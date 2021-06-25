<template>
    <div>
        <div class="container mt-5">
  <div class="row">
    <div class="col-md-12">  </div>
  </div>
</div>


<!--photo-->
<div class="container">
  <div class="row" style="">
    <div class="col-md-6">
      <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active"><img id="myImg" class="d-block w-100" :src="image | ImageUrl" alt="First slide" style="height: 60vh; width: 100%;"/>
            
           </div>
        </div>
      </div>
    </div>
    <div id="myModal" class="modal">
      <span class="close">&times;</span>
      <img class="modal-content" id="img01">
      <div id="caption"></div>
    </div>

    <!--product description-->
    
    <div class="new">
      <div class="row">
        <h2>{{product_name}}</h2>
      </div>
      <div class="row">
        <h1><i class="fa fa-inr" aria-hidden="true"></i> {{price}}</h1>
    
       
       
       
        <!--discount-->
       <!-- &nbsp; &nbsp;
        <h3><del>250</del></h3>
        &nbsp; &nbsp;
        <h2 class="text-success">20% off</h2> -->
      </div>

<!--ratings-->
    
      <div class="row">
        <h3 class="text-warning"><i class="fa fa-star" aria-hidden="true"></i><i class="fa fa-star" aria-hidden="true"></i><i class="fa fa-star" aria-hidden="true"></i> <i class="fa fa-star-half-o" aria-hidden="true"></i><i class="fa fa-star-o" aria-hidden="true"></i></h3>
        &nbsp; &nbsp;
        <h5>120 star rating  and 20 reviews</h5>
      </div>


      <!--offer zone-->
      <!-- <div class="row">
        <p><i class="text-success fa fa-check-square-o" aria-hidden="true"></i> <strong>Card Offer</strong> 20% Instant Discount on SBI Credit Cards</p>
        <p><i class="text-success fa fa-check-square-o" aria-hidden="true"></i> <strong>Bank Offer</strong> kfjwisjfsjjgvhsobjeajbhoijaojrjohjerkh;pgjrj </p>
        <p><i class="text-success fa fa-check-square-o" aria-hidden="true"></i> <strong>Bank Offer</strong> Extra 5% off* with Axis Bank Buzz Credit Card</p>
        <p><i class="text-success fa fa-check-square-o" aria-hidden="true"></i> <strong>Bank Offer</strong>20% Instant Discount on pay with <i class="fa fa-google-wallet" aria-hidden="true"></i> google wallet </p>
      </div> -->



      <div class="row mt-4">
        <h3 class="text-info"><i class="fa fa-map-marker" aria-hidden="true"></i></h3>
        <p style="font-size: 20px"> &nbsp; Delivery in 30 mins | &nbsp; <span class="text-success">FREE</span> </p>
      </div>
      <div class="row mt-4">
             <h4>Quantity: &nbsp; &nbsp;</h4>
             <select class="bootstrap-select">
              <option value="1" selected="selected">Full Plate</option>
              <option value="2">Half Plate</option>
             </select>
        <!-- <div class="dropdown show"> <a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Select Quantity </a>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuLink"> <option class="dropdown-item"  href="#">Full Plate</option> <option class="dropdown-item" href="#">Half Plate </option> </div>
        </div> -->
         <!-- <div class="quantity">
          <input type="number" value="1" min="1" class="quantity-field">
      </div> -->
      <div class="wrap quantity">
        <button :disabled="quantity<=1" type="button" @click="quantity--" id="sub" class="sub">-</button>
        <input class="count" type="text" id="1"  min="1" max="100" v-model="quantity" />
        <button type="button" @click="quantity++" id="add" class="add">+</button>
      </div>
      
      </div>
      <div class="row mt-4">
      	<h4>Resturant: &nbsp; &nbsp;</h4>
      	<p style="font-size: 18px">P.K Resturant </p>
      </div>
      <div class="card-text">
        <a class="btn btn-success text-light"> Buy Now</a> &nbsp; <a @click="AddToCart" class="btn btn-danger text-light"><i class="fa fa-cart-plus" aria-hidden="true"></i>  Add To Cart</a> <br/><br/>
      </div>
      <span :style="{color:statusColor}"><b>{{msg}}</b></span>
     <!-- dd {{product}} {{seller_id}} {{client_id}} -->
      
    </div>
  
  </div>
</div>


    </div>
</template>

<script>


import $ from 'jquery'
import API from '../API/API'

export default {

   props: ['exampleProp'],

    data(){

        return{
            quantity:1,
            product:'',
            product_id:'',
            seller_id:'',
            client_id:'',
            product_name:'',
            price:'',
            msg:'',
            image:'',
            statusColor:"",
        }
    },

  
    created(){
         this.product = JSON.parse(this.$route.query.product_id);  
        //  this.product = this.$route.query.product_id; 

         //console.log(this.$route)
        //  console.log(JSON.parse(this.$route.query.product_id)) 
         this.seller_id = this.$route.query.seller_id;
        //  this.client_id = this.$route.params.client_id;
        this.product_id = this.product.id
        this.product_name = this.product.Product_Name
        this.price = this.product.Price
        this.image = this.product.Image

    },

    mounted(){
            
            // $('.add').click(function () {		
            // var th = $(this).closest('.wrap').find('.count');    	
            // th.val(+th.val() + 1);
            // });
            // $('.sub').click(function () {
            // var th = $(this).closest('.wrap').find('.count');    	
            //         if (th.val() > 1) th.val(+th.val() - 1);
            // });
                
            var modal = document.getElementById("myModal");

            // Get the image and insert it inside the modal - use its "alt" text as a caption
            var img = document.getElementById("myImg");
            var modalImg = document.getElementById("img01");
            var captionText = document.getElementById("caption");
            img.onclick = function(){
              modal.style.display = "block";
              modalImg.src = this.src;
              // captionText.innerHTML = this.alt;
            }

            // Get the <span> element that closes the modal
            var span = document.getElementsByClassName("close")[0];

            // When the user clicks on <span> (x), close the modal

            span.onclick = function() { 
            modal.style.display = "none";
            }

            // getting the model
            var modal = document.getElementById('myModal');

            // When the user clicks anywhere outside of the modal, close it
                window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                    }
                }
    },

    methods:{
        AddToCart(){
          this.msg=''
                this.client_id = 27
                if(this.quantity<1)
                {
                  this.statusColor="red"
                  this.msg='Quantity Should Be Greater than 0'
                  return;
                }
                else{
                    if(this.$store.state.client_id)
                    {
                      this.client_id = this.$store.state.client_id
                      API.AddToCart(this.product_id,this.seller_id,this.client_id,this.quantity)
                      .then((response) => {
                        // console.log(response.data)
                          this.statusColor="green"
                          this.msg="Product Added To Card Successfully"
                        // this.$notify({ group: 'add_product',title: "Successfull", text: 'Product Added Successfully' ,type:'success'})
                      })
                      .catch((err) => {
                        // console.log(err)
                        this.statusColor="red"
                          this.msg="Product Unable To Add To Card"
                        // this.$notify({ group: 'add_product',title: "Error", text: 'Error While Adding Product' ,type:'error'})
                      })
                    }
                    else{
                      alert("Login First")
                      this.$router.push('/login')
                    }
                    // API.AddToCart(this.product_id,this.seller_id,this.client_id,this.quantity)
                    // .then(() => {
                    //   this.statusColor="green"
                    //   this.msg="Product Added To Card Successfully"
                    // })
                    // .catch(() => {
                    //   this.statusColor="red"
                    //   this.msg="Product Unable To Add To Card"
                    // })
                }

                
                
                
        }
    },

    filters:
    {
      ImageUrl(value)
      {
        //var url="http://localhost:8000/seller/"+value.split("http://localhost:8000/")[1];
        // console.log(value);
        return "http://localhost:8000/seller/"+value.split("http://localhost:8000/")[1];
      }
    }
}
</script>

<style scoped>


/* CSS Document */
.container{
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin-left: 270px;
}
.new{
    margin-left: 50px;
}
.quantity{
    position: relative;
    margin-top: 50px;
    margin-left: -123px;
}
.wrap .count{
  width: 30px;
  height: 30px;
  text-align: center;
}
.add, .sub{
  text-align: center;
  height: 30px;
  font-size: 20px;
  line-height: 30px;
}

.bootstrap-select{
  height: 40px;
  width: 150px;
  background-color:lightgray;
  border-radius: 5%;
} 
.bootstrap-select option{
  background-color: white;
  /* border-radius: 10%; */
}

input{
    border: none;
    outline: none;
    padding: 5px;
    border-radius: 5px;
    margin: 0 5px !important;
    box-shadow: 0 2px 5px rgba(0,0,0,.5);
}
input:hover,
input:focus{
    /* background: #ff008b; */
    color: black;
}
button{
    background-color: rgb(182, 159, 159);
    border: none;
    outline: none;
    padding: 0 10px;
    border-radius: 5px;
}
button:hover{
    background: #bebcbd;
    box-shadow: 0 2px 5px rgba(0,0,0,.5); 
}
.nice-number {
    display: inline-flex;
    justify-content: stretch;
  }
  
  .nice-number input {
    vertical-align: middle;
    -moz-appearance: textfield;
    box-sizing: content-box;
    margin: 0;
    text-align: center;
  }
  
  .nice-number input::-webkit-inner-spin-button,
  .nice-number input::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
  .count{
    width: 20px; 
  }
 
@media only screen and (max-width: 700px){
  .container{
    margin-left: 7px;
  }
  .card-text{
    margin-left: 4vh;
  }
}



  .modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 20vh; /* Location of the box */
    /* left: 0; */
    top: 10vh;
    width: 100%; /* Full width */
    height: 90vh; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
  }
  
  /* Modal Content (image) */
  .modal-content {
    margin: auto;
    display: block;
    width: 80%;
    height: auto;
    max-width: 700px;
  }
  
  /* Caption of Modal Image */
  /* #caption {
    margin: auto;
    display: block;
    width: 80%;
    max-width: 700px;
    text-align: center;
    color: #ccc;
    padding: 10px 0;
    height: 150px;
  } */
  
  /* Add Animation */
  .modal-content, #caption {  
    -webkit-animation-name: zoom;
    -webkit-animation-duration: 0.6s;
    animation-name: zoom;
    animation-duration: 0.6s;
  }
  
  @-webkit-keyframes zoom {
    from {-webkit-transform:scale(0)} 
    to {-webkit-transform:scale(1)}
  }
  
  @keyframes zoom {
    from {transform:scale(0)} 
    to {transform:scale(1)}
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
  
  /* 100% Image Width on Smaller Screens */
  @media only screen and (max-width: 700px){
    .modal-content {
      width: 100%;
    }
  }
  


</style>