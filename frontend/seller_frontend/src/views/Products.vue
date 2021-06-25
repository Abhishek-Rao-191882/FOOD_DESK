<template>
<div class="active-area">
      <section class="tableContainer">
        <div class="heading">

          <h2>Product Table</h2>
          <!-- {{User}} -->
          <button class="add" @click="openAddForm">Add Product</button>
        </div>
        <table role="table" class="table">
          <thead role="rowgroup">
            <tr role="row">
              <th role="columnheader">S.No.</th>
              <th role="columnheader">Product Name</th>
              <th role="columnheader">Category</th>
              <th role="columnheader">Product Id</th>
              <th role="columnheader">Price</th>
              <th role="columnheader">image</th>
              <th role="columnheader">Edit</th>
              <th role="columnheader">Delete</th>
              <th role="columnheader">
                Availability <br />
                Status
              </th>
            </tr>
          </thead>
          <!-- {{ProductData}} -->
          <tbody role="rowgroup">
            <tr role="row" v-for="(data,key) in ProductData" :key="key">
              <td role="cell" data-title="S.No.">{{key+1}}</td>
              <td role="cell" data-title="Product name">{{data.Product_Name}}</td>
              <td role="cell" data-title="Product name">{{data.Category.Category_Name}}</td>
              <td role="cell" data-title="Product Id">{{data.id}}</td>
              <td role="cell" data-title="Price">{{data.Price}}</td>
              <td role="cell" data-title="image">
                
                <!-- <img src="../../../../server/API" alt="" /> -->
                <a :href="'http://localhost:8000/seller'+data.Image" target="_blank"><img :src="'http://localhost:8000/seller'+data.Image"></a>
              </td>
              <td role="cell" data-title="Edit">
                <button
                  style="width: 25px;height: 25px;font-size: 20px;border: none;color: white;background-color: yellowgreen;" @click="openEditForm(data)"
                >
                  <i class="fa fa-pencil-square-o" aria-hidden="true"></i>
                </button>
              </td>
              <td role="cell" data-title="Delete">
                <button @click="DeleteProducts(data,key)" style=" width: 25px; height: 25px; font-size: 20px; border: none; color: white; background-color: red; border-radius: 5px;">
                  <i class="fa fa-trash-o" aria-hidden="true"></i>
                </button>
              </td>
              <td role="cell" data-title="Status"><input type="checkbox" /></td>
            </tr>
          </tbody>
        </table>
        
      </section>

      <!-- table ended -->
      <!-- pop up form started-->
      <div class="form-popup" id="AddForm">
        <div id="form_1" name="form_1" class="form-container">
          <div class="head_cancel">
            <h1>Add Product</h1>
            <button type="submit" class="cancel" @click="closeAddForm">
              &#x2716;
            </button>
          </div>
          <br/>
          <br/>
          <!-- <label for="product ID"><b>Product ID</b></label> -->
          <!-- <input type="text" placeholder="Product ID" name="product ID" required /> -->
          <label for="pdname"><b>Product Name</b></label>
          <input type="text" v-model="product_name" placeholder="Product Name" name="pdname" required />
          <label for="pdname"><b>Category</b></label>
          <select name="categories" id="category" v-model="product_category" required>
              <option selected disabled>Choose here</option>
              <option v-for="(categ,key) in CategoriesData" :key="key" :value="categ.id">{{categ.Category_Name}}</option>
              
          </select>
          <!-- <input type="text" v-model="product_category" placeholder="Category" name="pdname" required /> -->
          <label for="price"><b>Price</b></label>
          <input type="number" v-model="product_price" placeholder="Price" name="price" required />
          <label for="image"><b>Image</b></label>
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload"/>
          <!-- button -->
          <button type="submit" @click="AddProduct" class="btn">Add</button><br>

          <center>{{AddProductStatus}}</center>
        </div>
      </div>
      <div class="form-popup" id="EditForm">
        <div class="form-container">
          <div class="head_cancel">
            <h1>Edit Product</h1>
            <button type="submit" class="cancel" @click="closeEditForm">
              &#x2716;
            </button>
          </div>
          <br />
          <br />
          <!-- <label for="product ID"><b>Product ID</b></label> -->
          <!-- <input type="text" v-model="product_id" placeholder="Product ID" name="product ID" required /> -->
          <label for="pdname"><b>Product Name</b></label>
          <input type="text" v-model="product_name" placeholder="Product Name" name="pdname" required />
          <label for="pdname"><b>Category</b></label>
          <select name="categories" id="category" v-model="product_category" required>
              <option selected disabled>Choose here</option>
              <option v-for="(categ,key) in CategoriesData" :key="key" :value="categ.id">{{categ.Category_Name}}</option>
          </select>
          <label for="price"><b>Price</b></label>
          <input type="number" v-model="product_price" placeholder="Price" name="price" required />
          <label for="image"><b>Image {{product_image}}</b></label>
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload"/>
          <!-- button -->
          <button @click="EditProducts" type="submit" class="btn">Update</button>
          <br><center>{{msg}}</center>
        </div>
        
      </div>
    </div>
</template>



<script>

import axios from 'axios'
import API from '../API/API'

export default {
  
  data(){
    return{
      // ss:'',
      User:'',
      product_id:'',
      product_name:'',
      product_category:'',
      product_price:'',
      product_image:'',
      ProductData:'',
      CategoriesData:'',
      AddProductStatus:'',
      msg:''
    }
  },
  // watch:{
  //   '$route' (to,from) {
  //     alert(to.params.userInfo);
  //   }
  // }, 
  async created () {
    // alert(this.$route.params.userInfo);
    // fetch the data when the view is created and the data is
    // already being observed
    await this.UserInfo()
    this.getProducts()
    this.getCategories()
  },
  methods:{
  async UserInfo(){
      await API.UserInfo()
      .then((response)=>{
        this.User = response.data
      })
      .catch(err=> {
        this.error = "false "+err;
        // this.verification=false;
      })
    },
    getProducts(){
      API.getProducts(this.User.id)
      .then((response) => {
        this.ProductData = response.data;
        // this.verification = true;
        // this.$router.push("home")
      })
      .catch(err=> {
        this.ProductData = "false "+err;
        // this.verification=false;
      })
    },

    EditProducts(){
      let formData2 = new FormData();
        formData2.append('Product_Name',this.product_name)
        formData2.append('Price',this.product_price)
        formData2.append('Category',this.product_category)
        formData2.append('Seller',this.User.id)
        console.log(this.User.id)
        formData2.append('Image',this.product_image)
      
      // console.log(this.product_price)
      
      API.EditProducts(this.product_id,formData2)
      .then(() => {
        this.msg = "Successfuly Edited"
        console.log("Edited")
        // this.category_name = response.data;
        // this.verification = true;
        // this.$router.push("home")
      })
      .catch(err=> {
        this.error = "false "+err;
        // this.verification=false;
      })
    },


    DeleteProducts(data,index){
      // const token = localStorage.getItem('token')
      // console.log(datas)
      API.DeleteProducts(data)
      .then(() => {
        this.msg = "Successfull Deleted"
        console.log("Deleted")
        // this.$router.go('/categories');
        this.ProductData.splice(index);
        // this.$router.reload()
        // this.category_name = response.data;
        // this.verification = true;
        // this.$router.push("home")
      })
      .catch(err=> {
        this.error = "false "+err;
        // this.verification=false;
      })
    },


    getCategories(){
          // console.log(this.User.id)
        API.getCategories(this.User.id)
        .then((response) => {
          this.CategoriesData = response.data;
          // this.verification = true;
          // this.$router.push("home")
        })
        .catch(err=> {
          this.error = "false "+err;
          // this.verification=false;
        })
    },
    openAddForm(){
        document.getElementById("AddForm").style.display = "block";
        this.getProducts()
      },

    closeAddForm(){
        document.getElementById("AddForm").style.display = "none";
      },

    openEditForm(edits){
        document.getElementById("EditForm").style.display = "block";
        this.getCategories()
        this.product_id = edits.id
        this.product_name = edits.Product_Name
        this.product_category = edits.Category
        this.product_price = edits.Price
        this.product_image = edits.product_image
        this.getCategories()
      },

    closeEditForm() {
        document.getElementById("EditForm").style.display = "none";
      },


      handleFileUpload(event){
        console.log(event)
        // this.product_image = this.$refs.file.files[0];
        this.product_image = event.target.files[0]
      },
      async AddProduct() {
        let formData = new FormData();
        formData.append('Product_Name',this.product_name)
        formData.append('Price',this.product_price)
        formData.append('Category',this.product_category)
        formData.append('Seller',this.User.id)
        console.log(this.User.id)
        formData.append('Image',this.product_image)
        //  console.log(JSON.stringify(formData));
      axios.post('http://localhost:8000/seller/products',formData)
      .then(() => {
        this.AddProductStatus = 'Added Successfuly'
        // this.ProductData.push(JSON.stringify(InputData));
        // console.log(JSON.stringify(InputData));
        // console.log(this.ProductData)
        console.log('SUCCESS!!');
        /*
        await --- fetch
          await --- fetch/ not fetch        
        */
      })
      .catch(err=> {
        if(err.response.status == 400)
          this.AddProductStatus = 'Failed To Upload--> ' + 'Error : Please Upload All Details Correctly.'
        // this.ProductData = "false "+err;
        // else(err)
        //   this.AddProductStatus = 'Failed To Upload--> ' + err
        console.log('FAILURE!!');
        // this.verification=false;
      })
      }
  }
}
</script>


<style scoped>
* {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      .active-area{
        margin-top:-5vh;
      }

      /* The popup form - hidden by default */
      .form-popup {
        display: none;
        position: fixed;
        bottom: 0;
        top: 10%;
        right: 25%;
        left: 25%;
        border: 1% solid #f1f1f1;
        z-index: 9;
        height: 100%;
        width: 50%;
        align-self: center;
      }
      .form-container {
        max-width: 100%;
        padding: 1%;
        padding-left: 7%;
        background-color: white;
        justify-content: center;
      }
      /* close button */
      .head_cancel {
        display: flex;
        justify-content: space-between;
      }
      .head_cancel button {
        font-size: 25px;
      }
      .head_cancel .cancel {
        border: none;
        background: none;
        cursor: pointer;
      }

      /* input fields */
      .form-container input[type="text"],
      .form-container input[type="number"],
      .form-container input[type="file"],
      #category {
        width: 90%;
        padding: 15px;
        margin: 5px 0 22px 0;
        border: none;
        background: #f1f1f1;
        display: block;
      }
      

      /* When the inputs get focus, do something */
      .form-container input[type="text"]:focus,
      .form-container input[type="number"]:focus,
      .form-container input[type="file"]:focus,
      #category {
        background-color: #ddd;
        outline: none;
      }

      /*style for the submit/login button */
      .form-container .btn {
        background-color: #4caf50;
        color: white;
        padding: 16px 20px;
        border: none;
        cursor: pointer;
        width: 90%;
        margin-bottom: 10px;
        opacity: 0.8;
      }
      /*hover effects to buttons */
      .form-container .btn:hover,
      .open-button:hover {
        opacity: 1;
      }
      /* table */

      .tableContainer {
        margin: 4%;
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
      .add {
        background-color: red;
        color: white;
        border: none;
        cursor: pointer;
        opacity: 0.6;
        float: right;
        width: 6rem;
        margin: 1rem;
        border-radius: 5%;
        font-size: 1.2rem;
      }

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
        text-align: center;
      }

      td img {
        height: 55px;
        width: 55px;
      }

      /* responsiveness */
      @media screen and (max-width: 426px) {
        .active-area{
        margin-top:30vh;
      }
        .add {
          font-size: 1.2rem;
        }
        .form-popup {
          position: fixed;
          bottom: 0;
          top: 10%;
          right: 0;
          left: 0;
          border: 1% solid #f1f1f1;
          z-index: 9;
          height: 100%;
          width: 100%;
          align-self: center;
        }
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
          content: "Product Name";
        }
        td:nth-of-type(2):before {
          content: "Product ID";
        }
        td:nth-of-type(3):before {
          content: "Price";
        }
        td:nth-of-type(4):before {
          content: "Image";
        }
        td:nth-of-type(5):before {
          content: "Edit";
        }
        td:nth-of-type(6):before {
          content: "Delete";
        }
        td:nth-of-type(7):before {
          content: "Status";
        }
      }
      @media screen and (max-width: 768px) {
        .active-area{
        margin-top:-2vh;
      }
        .add {
          font-size: 1.2rem;
        }
        .form-popup {
          position: fixed;
          bottom: 0;
          top: 10%;
          right: 0;
          left: 0;
          border: 1% solid #f1f1f1;
          z-index: 9;
          height: 100%;
          width: 100%;
          align-self: center;
        }
      }
</style>