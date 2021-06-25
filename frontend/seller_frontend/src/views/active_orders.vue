<template>
    <div class="orders">
        <div class="active-area">
      <section class="tableContainer">
        <div class="heading">
          <h2>Active Orders</h2>
        </div>
        <table role="table" class="table">
          <thead role="rowgroup">
            <tr role="row">
              <th role="columnheader">S.No.</th>
              <th role="columnheader">User Name</th>
              <th role="columnheader">Mobile</th>
              <th role="columnheader">Product Name</th>
              <th role="columnheader">Quantity</th>
              <th role="columnheader">Price</th>
              <th role="columnheader">Tatal Amount</th>
              <th role="columnheader">Date and Time</th>
              <th role="columnheader">Address</th>
              
            </tr>
          </thead>
          <tbody role="rowgroup">
            <tr role="row" v-for="(data,key) in serverData" :key="key">
              <td role="cell" data-title="Mobile">{{key+1}}</td>
              <td role="cell" data-title="User Name">{{data.Orders_ID.User_Id.first_name}} {{data.Orders_ID.User_Id.last_name}}</td>
              <td role="cell" data-title="Mobile">{{data.Orders_ID.Mobile}}</td>
              <td role="cell" data-title="Product Name" style="color:#f76e2a;">{{data.Product.Product_Name}}</td>
              <td role="cell" data-title="Quantity" style="color:#f76e2a;">{{data.Quantity}}</td>
              <td role="cell" data-title="Price">Rs. {{data.Product.Product_Price}}</td>
              <td role="cell" data-title="Total Amount" style="color:#f76e2a;">Rs. {{data.Total_Amount}}</td>
              <td role="cell" data-title="Date and Time">{{data.Date_Time}}</td>
              <td role="cell" data-title="Date and Time" style="color:#f76e2a;">{{data.Orders_ID.Address}}</td>
              
            </tr>
          </tbody>
        </table>
      </section>
    </div>
    </div>
</template>

<script>
// import Axios from 'axios';

import API from '../API/API';


export default {
  data(){
    return{
      User:'',
      type:1,
      serverData:'',
    }
  },
    async created () {
    // fetch the data when the view is created and the data is
    // already being observed
    
    await this.UserInfo();
    // console.log("user info.")
    this.getOrders();
  },
    methods:{
      
      async UserInfo(){
        await API.UserInfo()
        .then((response)=>{
          this.User = response.data
          // return response.data;
        })
        .catch(err=> {
          this.error = "false "+err;
          // this.verification=false;
        })
    },
      getOrders(){
        API.getOrders(this.User.id,this.type)
        .then((response) => {
          this.serverData = response.data;
          
          // this.verification = true;
          // this.$router.push("home")
        })
        .catch(err=> {
          this.error = "false "+err;
          // this.verification=false;
        })
    },
    },
}
</script>

<style scoped>

 * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      /* table */

      .tableContainer {
        margin: 1%;
        /* border: 1px solid red; */
      }
      .heading {
        display: flex;
        justify-content: space-between;
      }
      .heading h2 {
        font-size: 1.5rem;
        color: red;
        margin-top: 4vh;
      }
      /* Button used to open the contact form  */

      /*--------------------------------------------------------------
# Table
--------------------------------------------------------------*/
      table {
        box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.1),
          0px 0px 60px rgba(0, 0, 0, 0.05), 0px 20px 30px rgba(0, 0, 0, 0.05),
          0px 0px 30px rgba(0, 0, 0, 0.05);
        font-size: 1.2rem;
        width: 100%;
      }

      th {
        color: #ffffff;
        background: #39a2fb;
        font-weight: 700;
      }

      tr {
        background: #fff;
      }

      tr:hover {
        background: #f4f4f4;
      }

      tr:nth-child(even) {
        background: #f4f4f4;
      }

      td {
        word-wrap: break-word;
        border-bottom: 1px solid #ccc;
        align-items: center;
        justify-content: center;
        padding: 1%;
        text-align: center;
      }

      td img {
        height: 55px;
        width: 55px;
      }
      .accept {
        width: 25px;
        height: 25px;
        font-size: 20px;
        border: none;
        margin-right: 15%;
        color: white;
        background-color: yellowgreen;
      }
      .reject {
        width: 25px;
        height: 25px;
        font-size: 20px;
        border: none;
        color: white;
        background-color: red;
        border-radius: 5px;
      }

      /* responsiveness */
      @media screen and (max-width: 426px) {
        /* Force table to not be like tables anymore */
        table,
        thead,
        tbody,
        th,
        td,
        tr {
          display: block;
        }

        /* Hide table headers (but not display: none;, for accessibility) */
        thead tr {
          position: absolute;
          top: -9999px;
          left: -9999px;
          justify-content: center;
        }

        tr {
          margin: 0 0 1rem 0;
        }

        tr:nth-child(odd) {
          background: #ccc;
        }

        td {
          /* Behave  like a "row" */
          border: none;
          border-bottom: 1px solid #eee;
          position: relative;
          /* float: left; */
          padding-left: 60%;
          margin-left: 0;
          text-align: start;
          padding-top: 3px;
          padding-bottom: 3px;
        }

        td:before {
          /* Now like a table header */
          position: absolute;
          /* Top/left values mimic padding */
          top: 0;
          left: 20px;
          width: 50%;
          float: left;
          /* padding-right: 10px; */
          white-space: nowrap;
          padding-top: 3px;
          padding-bottom: 3px;
        }

        /*
		Label the data
    You could also use a data-* attribute and content for this. That way "bloats" the HTML, this way means you need to keep HTML and CSS in sync. Lea Verou has a clever way to handle with text-shadow.
		*/
        td:nth-of-type(1):before {
          content: "User Name";
        }
        td:nth-of-type(2):before {
          content: "Mobile";
        }
        td:nth-of-type(3):before {
          content: "Product Name";
        }
        td:nth-of-type(4):before {
          content: "Quantity";
        }
        td:nth-of-type(5):before {
          content: "Price";
        }
        td:nth-of-type(6):before {
          content: "Total Amount";
        }
        td:nth-of-type(7):before {
          content: "Date and Time";
        }
        td:nth-of-type(8):before {
          content: "Address";
        }
        td:nth-of-type(9):before {
          content: "Accept/Reject";
        }
      }
      @media screen and (max-width: 768px) {
        
      }

</style>