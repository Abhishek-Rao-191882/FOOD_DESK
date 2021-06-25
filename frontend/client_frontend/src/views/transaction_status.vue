<template>
    <div class="active-area">
      <section class="tableContainer">
        <div class="heading">
          <h2 :style="{color:statusColor}">Transaction Status</h2>
          <p v-if="status"><img src="../assets/aniTick.gif" alt=""> Payment Done Successfully </p>
          <p v-else><img src="../assets/cross.png" alt=""> Payment Failed </p>

          <!-- <p><img src="../assets/cross.png" alt=""> Payment <span>Failed.</span></p> -->
        </div>
        <table role="table" class="table">
          <thead role="rowgroup">
            <tr role="row">
              <th role="columnheader">Transaction Detail</th>
              <th role="columnheader"></th>
            </tr>
          </thead>
          <tbody role="rowgroup">
            <tr role="row">
              <td role="cell" data-title="Category Name">Transaction ID</td>
              <td role="cell" data-title="Action">
                {{t_id}}
              </td>
            </tr>
            <tr role="row">
              <td role="cell" data-title="Category Name">Bank Transaction Id</td>
              <td role="cell" data-title="Action">
                {{bt_id}}
              </td>
            </tr>
            <tr role="row">
              <td role="cell" data-title="Category Name">Order ID</td>
              <td role="cell" data-title="Action">
                {{o_id}}
              </td>
            </tr>
            <tr role="row">
              <td role="cell" data-title="Category Name">Transaction Amount</td>
              <td role="cell" data-title="Action">
                {{t_amt}}
              </td>
            </tr>
            <tr role="row">
              <td role="cell" data-title="Category Name">Status</td>
              <td role="cell" data-title="Action">
                {{sts}}
              </td>
              <!-- <td role="cell" data-title="Action">
                Failure
              </td> -->
            </tr>
            <tr role="row">
              <td role="cell" data-title="Category Name">Bank Name</td>
              <td role="cell" data-title="Action">
                {{b_name}}
              </td>
            </tr>
             <tr role="row">
              <td role="cell" data-title="Category Name">Transaction Date</td>
              <td role="cell" data-title="Action">
                {{t_date}}
              </td>
            </tr>
             <!-- <tr role="row">
              <td role="cell" data-title="Category Name">Transaction Time</td>
              <td role="cell" data-title="Action">
                11:11:11 PM
              </td>
            </tr> -->
          </tbody>
        </table>
      </section>
      <!-- table ended -->

    </div>

</template>

<script>
export default {
  data(){
    return{
      t_id:'',
      bt_id:'',
      o_id:'',
      t_amt:'',
      sts:'',
      b_name:'',
      t_date:'',
      statusColor:'',
      status:false,
    }
  },
  mounted(){
         this.t_id = this.$route.query.t_id;
         this.bt_id = this.$route.query.bt_id;
         this.o_id = this.$route.query.o_id;
         this.t_amt = this.$route.query.t_amt;
         this.sts = this.$route.query.sts;
         this.b_name = this.$route.query.b_name;
         this.t_date = this.$route.query.t_date;

         if(this.sts == "TXN_SUCCESS")
         {
           this.statusColor = "green";
           this.status = true;
           console.log(this.status)

         }

  }
    
}
</script>

<style scoped>      
      /* table */

      .tableContainer {
        margin: 4%;
        /* border: 1px solid red; */
        /* text-align: center; */
      }
      .heading {
          display: block;

      }
      .heading h2 {
        font-size: 1.5rem;
        color: red;
        /* margin-top: 4vh; */
      } 
      .heading p{
          margin-bottom: 1%;
      }
      .heading p span{
          color: red;
      }
      .heading p img{
          height: 30px;
          width: 30px;
      }
      /* Button used to open the contact form  */

      /* Table */
      table {
        /* box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.1),
          0px 0px 60px rgba(0, 0, 0, 0.05), 0px 20px 30px rgba(0, 0, 0, 0.05),
          0px 0px 30px rgba(0, 0, 0, 0.05); */
          border: 1px solid rgb(204, 197, 197);
          /* border-radius: 200px; */
          font-size: 1.2rem;
          width: 70%;
      }

      th {
        color: #ffffff;
        background: #39a2fb;
        font-weight: 700;
        text-align: start;
        /* padding-left: 15%; */
      }

      tr {
        background: #fff;
        border: none;
        line-height: 15px;
        font-size: 80%;
      }

      /* tr:hover {
        background: #f4f4f4;
      }

      tr:nth-child(even) {
        background: #f4f4f4;
      } */

      td {
        word-wrap: break-word;
        /* border-bottom: 1px solid #ccc; */
        /* padding-left: 15%; */
        border: none;
      }

      /* responsiveness */
      @media screen and (max-width: 426px) {
        table{
            width: 100%;
        }
        th,
        td {
          padding-left: 40%;
        }
      }
      @media screen and (max-width: 768px) {
        table{
            width: 100%;
        }
        th,
        td {
          max-width: 80px;
          padding-left: 20px;
        }
      }
    </style>
  
    
