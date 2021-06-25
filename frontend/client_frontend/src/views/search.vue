<template>
    <div>
        <div class="flex-container">
      <div class="main">
        <!-- {{mine}} -->
        <!-- {{products}} -->
        <notifications position="top center" group="add_product"/>
        <h1 class="mainhead">Your Search Result : <span>{{search_count}}</span></h1>
        <p></p>{{search_data}}
        <ul class="cards">
          {{$store.getters.getPreviousPageArray}}
          <li class="cards_item" v-for=" (datas,key) in products" :key="key">
            <div class="card">
              <div class="card_image">
                
                <!-- <a target="_blank"><img :src="'http://localhost:8000/seller'+datas.Image"></a> -->
                <a target="_blank"><img :src="datas.Image | ImageUrl"></a>

              </div>
              
              <div class="card_content">
                <router-link :to="{ name:'Product_Details' , query: {product_id:JSON.stringify(datas), seller_id:datas.Seller.id}}" style="text-decoration: none;" >
                <h2 class="card_title">{{datas.Product_Name}}</h2>
                <p class="card_text">
                  Price: <span>{{datas.Price}}</span> 
                </p>
                <p class="card_text">
                  Category: <span>{{datas.Category.Category_Name}}</span> 
                </p>
                <p class="card_text">
                  {{datas.Seller.first_name}} {{datas.Seller.last_name}}
                </p>
              </router-link>

                <button class="btn card_btn" @click="AddToCart(datas)">Add To Cart</button>
              </div>
            </div>
          </li>
          
          
          
        </ul>
      </div>
    </div>
<center>
  <div style="display:block;">
    <!-- <button class="page_change" @click="previousPage(1)">Previous</button> <button class="page_change" @click="next_page">Next</button> -->
  </div>
      <br><br>
      
</center>




    <footer>
      <p>copyright FoodDesk2020</p>
    </footer>
    </div>
</template>
<script>
import axios from 'axios'
import API from '../API/API'

export default {
  data(){
    return{
      products:'',
      product_id:'',
      seller_id:'',
      client_id:'',
      msg:'',
      search_text:'',
      search_data:'',
      search_count:'',
    }
  },

  watch:{
    '$route'(to,from){
      this.search_text = to.query.searching_data
      this.search()
    }
  },
    created(){
      this.search_text = this.$route.query.searching_data
      this.search()
    },
    methods:{
      
      search(){
        if(this.search_text.length==0)
        {
          this.$notify({ group: 'add_product',title: '<h4>Warning</h4>', text: '<h6>Please First Enter Something To Search .</h6>' ,type:'warn', width:'50%'})
        }
        else
        {
          API.search(this.search_text)
          .then((response)=>{
            console.log(response.data)
            this.products = response.data
          })
          .catch(()=>{
             this.$notify({ group: 'add_product',title: '<h4>Warning</h4>', text: '<h6>There Is A Server Error While Searching .</h6>' ,type:'warn', width:'50%'})
           })
        }
      },

      AddToCart(datas){
        this.product_id = datas.id
        this.seller_id = datas.Seller.id
        this.client_id = this.$store.state.client_id
        
        if(this.$store.state.client_id)
        {
          API.AddToCart(this.product_id,this.seller_id,this.client_id,1)
          .then((response) => {
            // console.log(response.data)
            this.$notify({ group: 'add_product',title: "Successfull", text: 'Product Added Successfully' ,type:'success'})
          })
          .catch((err) => {
            // console.log(err)

            this.$notify({ group: 'add_product',title: "Error", text: 'Error While Adding Product' ,type:'error'})
          })
        }
        else{
          alert("Login First")
          this.$router.push('/login')
        }
      },

  
      


    },
    computed:{
      getPrevPageArray()
      {
        return this.$store.getters.getPrevArray;
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

/* Font */
@import url("https://fonts.googleapis.com/css?family=Quicksand:400,700");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.page_change {
  margin-top: 40px;
  margin-bottom: 10px;
  background-color: white;
  border: 1px solid black;
  border-radius: 5px;
  padding: 10px;
  width: 10%;
  font-size: 15px;
  font-weight: bold;
}
.page_change:hover {
  background-color: orangered;
  color: white;
  transition: 0.5s;
  cursor: pointer;
}


body {
  color: #272727;
  font-family: "Quicksand", serif;
  font-style: normal;
  font-weight: 400;
  letter-spacing: 0;
  padding: 0;
  margin: 0;
}
.flex-container {
  display: flex;
  /* margin-top: 10vh; */
  margin-left: 1vw;
  margin-right: 1vw;
  border-top: 1px solid rgba(0, 0, 0, 0.3);
}
.main {
  /* max-width: 1200px; */
  margin: 0;
  width: 70vw;
  flex: 5;
  order: 2;
  border: 1px solid rgba(0, 0, 0, 0.3);
}
.mainhead {
  font-size: 45px;
  font-weight: 400;
  text-align: start;
}
.mainhead span {
  font-weight: 800;
}
.cards {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  margin: 0;
  padding: 1rem 0 0 0;
  /* border: 1px solid rgba(0, 0, 0, 0.3); */
}
.cards_item {
  display: flex;
  justify-content: center;
  margin: 0 0 0 0;
  /* padding: 0 10px 0 10px; */
  /* padding: 0; */
  width: 100%;
  /* border: 1px solid rgba(0, 0, 0, 0.3); */
}
.card {
  background-color: white;
  border-radius: 0.25rem;
  box-shadow: 0 20px 40px -14px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  width: 300px;
  margin-bottom: 10px;
  /* border: 1px solid rgba(0, 0, 0, 0.3); */
  
}

.card_content {
  padding: 1rem;
  height: 178px;
  /* background: linear-gradient(to bottom left, #ef8d9c 40%, #ffc39e 100%); */
}

.card_title {
  color: #000000;
  font-size: 1.1rem;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: capitalize;
  margin: 0px;
}

.card_text {
  color: #000000;
  font-size: 0.875rem;
  line-height: 1.5;
  margin-bottom: 0.5rem;
  font-weight: 400;
}
.card_text span{
  font-weight: 800;
}
img {
  height: 150px;
  width: 300px;
  vertical-align: middle;
}

.btn {
  color: #c91d7b;
  padding: 0.8rem;
  font-size: 14px;
  text-transform: uppercase;
  border-radius: 4px;
  font-weight: 400;
  display: block;
  width: 100%;
  cursor: pointer;
  border: none;
  background: rgb(240, 229, 231);
}
.btn:hover {
  background-color: rgba(177, 49, 49, 0.12);
}
footer {
  text-align: center;
}
/* Responsive */
@media (min-width: 40rem) {
  .cards_item {
    width: 50%;
  }
 
}

@media (min-width: 56rem) {
  .cards_item {
    width: 33.3333%;
  }
}

@media (max-width: 768px) {
  .page_change{
    width: 10%;
    font-size: 10px;
  }
  .flex-container {
    flex-direction: column;
  }
  .main {
    width: 100%;
    /* border-top: 1px solid rgba(0, 0, 0, 0.3); */
  }
  .mainhead {
    font-size: 40px;
  }

}
@media (max-width: 428px) {

  .page_change{
    width: 16%;
    font-size: 10px;
  }

  .flex-container {
    flex-direction: column;
  }
  .sidemenu {
    width: 100%;
  }
  .main {
    width: 100%;
  }
  .card{
    display: flex;
    flex-direction: row;
    width: 400px;
    box-shadow: none;
  }
  .cards_item{
    margin: 0 0 0.5rem 0;
    border-bottom: 1px solid lightgray;
    padding: 0;
  }
  .card_image{
    width: 100px;
    height: 100px;
  }
  .card_image img{
    height:80px ;
    width:80px ;
    margin: 10px;
  }
  .card_content{
    width: 300px;
    height: 100px;
    padding: 0.5rem;
  }
  .card_title{
    font-size: 15px;
    margin: 0;
  }
  .card_text{
    font-size: 10px;
    margin: 0;
  }
  .card_btn{
    font-size: 15px;
    margin: 10px 0 0 0;
    height: 17px;
    line-height: 15px;
    justify-content: center;
    height: 20px;
    padding: 0;
  }
  .cards li:first-child{
   border-top: 1px solid lightgrey; 
  } 
}


</style>