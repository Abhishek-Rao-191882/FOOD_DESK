<template>
  <div id="app">
    <router-view>
      <SellerLogin />
    </router-view>
    
  </div>
</template>

<script>
import SellerLogin from './views/Seller_Login'
// import API from "./API/API"
  export default{
    mounted(){
    // console.log(this.$router);
  },
    components:
    {
      
      // dashboard,
      SellerLogin,
    },
    beforeMount() {
      document.title="testing";
    },
  }
</script>

<style>
*{
  margin: 0;
  padding: 0%;
  box-sizing: border-box;
}
</style>
