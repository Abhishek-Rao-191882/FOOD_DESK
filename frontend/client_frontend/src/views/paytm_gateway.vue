<template>

    <div>

         <center>
         <h1>Please do not refresh this page...</h1>
      </center>
      <form method="POST" action="http://localhost:8000/paytm_gateway/payment/">
         <table border="1">
            <tbody>
               <!-- <input type="hidden" name="mid" value="YOUR_MID_HERE">
               <input type="hidden" name="orderId" value="YOUR_ORDERID_HERE">
               <input type="hidden" name="txnToken" value="YOUR_TXNTOKEN_HERE"> -->

               <input type="text" name="amount" value="30">




               <input type="submit" value="SUBMIT">
            </tbody>










<!--          
		<input type="hidden" name="MID" value="zwfsDv38259108810773">


		<input type="hidden" name="INDUSTRY_TYPE_ID" value="Retail">


		<input type="hidden" name="WEBSITE" value="WEBSTAGING">


		<input type="hidden" name="CHANNEL_ID" value="WEB">


		<input type="hidden" name="CALLBACK_URL" value="http://localhost:8000/response/">


		<input type="hidden" name="MOBILE_NO" value="7777777777">


		<input type="hidden" name="EMAIL" value="arao8732@gmail.com">


		<input type="hidden" name="CUST_ID" value="123123">


		<input type="hidden" name="ORDER_ID" value="OLu7qA">


		<input type="hidden" name="TXN_AMOUNT" value="100">


		<input type="hidden" name="CHECKSUMHASH" value="RayjTykuTEyiP8h+14csHleEVKD7oYWGjniBqGRgJx63irOJLm3NCH9P0txV4r4O5ylaN93+h9AOfxk5ppJf9srPdLwLvx7uUkrsSZWS16Q=">


 -->















         </table>
      </form>

    </div>
    
</template>

<script>


export default {
   data() {
      return {
         client_id:'',
         amount:'',
         order_id:'',
      }
   },
    mounted()
    {
      //  document.paytm.submit();
      var form =new FormData();
      form.append("name","kumar")
      // form.append("")
      // form.append("")
      // form.append("")
      // form.append("")
      // form.append("")
      // form.append("")
      // form.append("")
      // form.append("")
      // form.append("")
      // form.append("")
    }
}
</script>

<style scoped>

</style>