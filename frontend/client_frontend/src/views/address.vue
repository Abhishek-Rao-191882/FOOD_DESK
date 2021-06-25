<template>
<div>
  
<div class="main">
        <section class="heading">Select where you want to Deliver</section>
    <div>
        <label class="ok"><input type="radio" name="colorRadio" value="orange"> Saved Address</label><br>
        <label class="ok"><input type="radio" name="colorRadio" value="green"> Edit Address</label>
        


    </div>
    <center>
    <div class="orange box">
      <div class="text">Deliver To :- <br> <strong>{{$store.state.first_name}} {{$store.state.last_name}}</strong> <br>
      Mob.- {{$store.state.Mobile_No}}<br>
      {{$store.state.address}}
      </div><br>
      <form method="POST" action="http://localhost:8000/paytm_gateway/payment/">
            <input type="number" :value="Mobile_No" name="mobile" hidden>
            <input type="number" step="0.01" :value="total_amount" name="amount" hidden>
            <input type="text" :value="address" name="address" hidden>
            <input type="text" name="order_items" :value="orders" hidden>
            <input type="submit" value="Continue to checkout" class="btn" >
      </form>
      </div>
   </center>
    <div class="green box">
        
    <div class="container">
        <div class="row">
          <div class="address">
            
            <h3>Delivery Address</h3>
            <!-- <label for="fname">Full Name</label>
            <input type="text" id="fname" name="firstname" placeholder="Enter Your Name"> -->
        <form method="POST" action="http://localhost:8000/paytm_gateway/payment/">
            <label for="mobile"> Mobile No.</label>
            <input :value="Mobile_No" type="number" id="phone" name="mobile" placeholder="Enter Mobile No.">

            <!-- <label for="adr"> Room No. & Floor</label> -->
            <!-- <input type="text" id="adr" name="address" placeholder="Enter Room No. And Floor"> -->
            <label for="adr"> Full Address</label>
            <textarea type="text" :value="address" placeholder="Enter Full Address" name="address"></textarea>
            <h5 style="color:red;font-size:15px">*Delivery adress must be around 1.5 km radius to the CUH hostel.</h5>



            <input type="number" step="0.01" :value="total_amount" name="amount" hidden>
            <input type="text" name="order_items" :value="orders" hidden>
            <input type="submit" value="Continue to checkout" class="btn" >
      </form>


         </div>
        </div>
        
            
    </div>

    </div>
    </div>




</div>
</template>

<script>


import API from '../API/API'

export default {
  data(){
    return{
      orders:"",
      address:"",
      total_amount:"",
      Mobile_No:"",
    }
  },
    mounted(){

      this.orders = JSON.stringify(this.$store.state.ordersArray)
      this.total_amount = this.$store.state.ordersAmount
      this.address = this.$store.state.address
      this.Mobile_No = this.$store.state.Mobile_No
      // console.log(this.orders)


        $(document).ready(function(){
           $('input[type="radio"]').click(function(){
           var inputValue = $(this).attr("value");
           var targetBox = $("." + inputValue);
           $(".box").not(targetBox).hide();
           $(targetBox).show();
    });
});
    },

    methods:{
      run(){
        console.log(this.orders)
      }
    }


}

</script>


<style scoped>
    *{
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        box-sizing: border-box;
    }
    
body {
    font-family: Arial;
    font-size: 17px;
    padding: 8px;
  }
  
  .main{
    border:1px solid grey;
    margin-left: 25%;
    width:50%;

  }
.heading{
    width: 100%;
    height: 10vh;
    background: orange;
    text-align: center;
    padding-top: 2.5vh;
    font-size: 30px;
    font-weight: bolder;
    color: white;
    margin-bottom: 5vh;
}
    .box{
        color: #fff;
        padding: 20px;
        display: none;
        margin-top: 20px;
    
    }
    .orange{
         background: orange;
         width: 90%;
         text-align: left;
        
    }
    .text{
    padding-left: 25vh;
    }

        .ok{
        font-size: 30px;
        font-weight: bolder;
        text-align: center;
    }
    label{
         margin-right: 15px;
         font-size: 20px; 
         font-weight: bolder;
        
        }
 
  .address {
    -ms-flex: 50%; 
    flex: 50%;
    padding: 0 16px;
    color: black;
  }
  .container {
    background-color: #f2f2f2;
    padding: 5px 20px 15px 20px;
    border: 1px solid lightgrey;
    border-radius: 3px;
    width: 100%;
  }
  input[type=text],input[type=number] {
    width: 100%;
    margin-bottom: 20px;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 3px;
  }
   label {
    margin-bottom: 10px;
    display: block;
  }
  
textarea[type=text]{
  resize: none;
  height: 80px;
  width: 100%;
  margin-bottom: 20px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 3px;
}
  .btn {
    background-color: #4CAF50;
    color: white;
    padding: 12px;
    margin: 10px 0;
    border: none;
    width: 100%;
    border-radius: 3px;
    cursor: pointer;
    font-size: 17px;
  }
  .btn:hover {
    background-color: #45a049;
  }  
  @media all and (max-width: 768px){
    .main{
    width:100%;
    margin:0;
  }
  }
  @media all and (max-width: 600px){
    .main{
    width:100%;
    margin:0;
  }
      .heading{
          font-size: 20px;
      }
      .orange{
        width: 100%;
      }
      .text{
        padding-left: 27%;
      }
      h5{
        font-size: 10px;
      }
  }
       

</style>