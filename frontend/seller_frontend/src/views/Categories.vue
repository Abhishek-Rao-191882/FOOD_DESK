<template>
    <div class="active-area">
      <section class="tableContainer">
        <div class="heading">
          <!-- {{User.id}} -->
          <h2>Manage Category</h2>
          <button class="add" @click="openAddForm()">Add Categories</button>
        </div>
        <table role="table" class="table">
          <thead role="rowgroup">
            <tr role="row">
              <th role="columnheader">Sr.No.</th>
              <th role="columnheader">Category Name</th>
              <th role="columnheader">Category Id</th>
              <th role="columnheader">Action</th>
            </tr>
          </thead>
          <tbody role="rowgroup">
            <tr role="row" v-for=" (datas,key) in serverData" :key="key">
              <td role="cell" data-title="S.No.">{{key+1}}</td>
              <td role="cell" data-title="Category Name">{{datas.Category_Name}}</td>
              <td role="cell" data-title="Category Id">{{datas.id}}</td>
              <td role="cell" data-title="Action">
                <button class="editIcon" @click="openEditForm(datas)">
                  <i class="fa fa-pencil-square-o" aria-hidden="true"></i>
                </button> <button @click="DeleteCategories(datas,key)" class="deleteIcon">
                  <i class="fa fa-trash-o" aria-hidden="true"></i>
                </button>
              </td>
            </tr>
           
          </tbody>
        </table>
      </section>
      <!-- table ended -->
      <!-- pop up form started-->
      <!-- add form -->
      <div class="form-popup" id="AddForm">
        <div action="" class="form-container">
          <div class="head_cancel">
            <h1>Add Category</h1>
            <button type="submit" class="cancel" @click="closeAddForm">
              &#x2716;
            </button>
          </div>
          <br />
          <br />
          <label for="Category Name"><b>Category Name</b></label>
          <input type="text" placeholder="Category Name" v-model="category_name" name="Category Name" required />
          <button type="submit" @click="AddCategories" class="btn">Add</button>
          {{msg}}
        </div>
      </div>
      <!-- edit Form -->
      <div class="form-popup" id="EditForm">
        <div action="" class="form-container">
          <div class="head_cancel">
            <h1>Edit Category</h1>
            <button type="submit" class="cancel" @click="closeEditForm">
              &#x2716;
            </button>
          </div>
          <br />
          <br />
          <label for="Category Name"><b>Category Name</b></label>
          <input type="text" v-model="category_name" placeholder="Category Name" name="Category Name" required />
          <!-- button -->
          <button type="submit" @click="EditCategories" class="btn">Update</button>
          {{msg}}
        </div>
      </div>
      
    </div>
</template>
<script>

// import axios from 'axios'
import API from '../API/API'

export default {
    data(){
        return{
            User:'',
            category_name:'',
            category_id:'',
            serverData:'',
            error:'',
            msg:'',
        }
    },
    async created () {
    // fetch the data when the view is created and the data is
    // already being observed
    
    await this.UserInfo();
    // console.log("user info.")
    this.getCategories();
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
      AddCategories(){
      // const token = localStorage.getItem('token')
      // console.log(this.User.id)
      API.AddCategories(this.User.id,this.category_name)
      .then((response) => {
        this.msg = "Successfuly Uploaded"
        console.log("Uploaded");
        console.log(response.data['id'])
        this.serverData.push({'Seller':this.User.id,'Category_Name':this.category_name,'id':response.data['id']});

        // this.category_name = response.data;
        // this.verification = true;
        // this.$router.push("home")
      })
      .catch(err=> {
        this.error = "false "+err;
        // this.verification=false;
      })
    },
    EditCategories(){
      // const id = datas.id
      // console.log(this.category_id)
      // const token = localStorage.getItem('token')
      API.EditCategories(this.User.id,this.category_id,this.category_name)
      .then(() => {
        this.msg = "Successfuly Edited"
        // this.category_name = response.data;
        // this.verification = true;
        // this.$router.push("home")
      })
      .catch(err=> {
        this.error = "false "+err;
        // this.verification=false;
      })
    },
    DeleteCategories(datas,index){
      // const token = localStorage.getItem('token')
      // console.log(datas)
      API.DeleteCategories(datas.id)
      .then(() => {
        this.msg = "Successfull Deleted"
        console.log("Deleted")
        // this.$router.go('/categories');
        this.serverData.splice(index);
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
          this.serverData = response.data;
          
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
      },

      closeAddForm(){
        document.getElementById("AddForm").style.display = "none";
      },

      openEditForm(datas){
        document.getElementById("EditForm").style.display = "block";
        this.category_name = datas.Category_Name
        this.category_id = datas.id
        // console.log(this.category_name)
      },

      closeEditForm(){
        document.getElementById("EditForm").style.display = "none";
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
      .editIcon {
        width: 25px;
        height: 25px;
        font-size: 20px;
        border: none;
        color: white;
        background-color: yellowgreen;
      }
      .deleteIcon {
        width: 25px;
        height: 25px;
        font-size: 20px;
        border: none;
        color: white;
        background-color: red;
        border-radius: 5px;
      }

      /* input fields */
      .form-container input[type="text"],
      .form-container input[type="number"],
      .form-container input[type="file"] {
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
      .form-container input[type="file"]:focus {
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