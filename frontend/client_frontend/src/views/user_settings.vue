<template>
    <div class="user_settings">

            <div class="container">
        
<center><div class="profile">
        <img src="../assets/user.png" alt="">
         </div>
         </center>
       <notifications position="top center" group="add_product"/>
       <notifications position="center" group="input_error"/>
       
            <center><div class="text"><h1>Personal Information</h1></div></center>
        <div class="details">
            <h2>Full Name</h2>
            <input type="text" id="f_name"  class="input" v-model="user_firstname" placeholder="Enter First Name" disabled>
            <button @click="toggle('f_name',edit,$event)" class="btn">Edit</button>
            <br><br>
            <input type="text" id="l_name" class="input" v-model="user_lastname" placeholder="Enter Last Name" disabled>
            <button @click="toggle('l_name',edit,$event)" class="btn">Edit</button>
            <br><br>
            <h2>Mobile Number</h2>
            <input type="number" id="mobile" class="input" v-model="mobile" placeholder="Enter mobile no." disabled>
            <button @click="toggle('mobile',edit,$event)" class="btn">Edit</button>
            <br><br>
            <h2>Email Id</h2>
            <input type="email" class="inputs" :value="email" placeholder="Enter your email" disabled>
            <br><br>
            <center><button class="btn"><a herf="re.html"> Change Password</a></button></center>
            <br><br>
            <h2>My Address</h2>
        
            <textarea class="inputs" id="address" v-model="address" placeholder="Enter Room no. and Floor" rows="4" disabled></textarea>
            <center><div class="button"><button @click="toggle('address',edit,$event)" class="btn">Edit</button>  </div></center>
            <br>
            <br>
           
           <center><button class="btn" @click="update_info"> Update Info. </button> </center>
            <!-- <button class="btn"><a href="addnew.html"> + Add a new address</a></button>-->
        
        
        </div>
    </div>


    </div>
</template>

<script>

import API from '../API/API'

export default {
    data(){
        return{
            user_firstname: '',
            user_lastname: '',
            mobile:'',
            address:'',
            email:'',
            toggler:false,
            edit:true,
            event:'',
            id:''
        }
    },
    created(){
        this.user_firstname = this.$store.state.first_name
        this.user_lastname = this.$store.state.last_name
        this.mobile = this.$store.state.Mobile_No
        this.address = this.$store.state.address
        this.email = this.$store.state.email

    },
    methods:{
        toggle(id,edit,event){
            if(this.event)
                {
                    if(this.event != event)
                    {
                        this.event.target.innerText = "Edit"
                        this.event.target.style.background = "#2ed573"
                        document.getElementById(String(this.id)).disabled = true
                    }
                }
            if(edit)
            {
                this.event = event
                this.edit = !this.edit
                console.log("edit")
                this.toggler = !this.toggler
                event.target.innerText = "Done"
                event.target.style.background = "#f9ca24"

                document.getElementById(String(id)).disabled = false
                this.id=id
            }
            else
            {
                console.log("done")
                this.edit = !this.edit
                this.toggler = !this.toggler
                event.target.innerText = "Edit"
                event.target.style.background = "#2ed573"
                document.getElementById(String(id)).disabled = true
                this.id=id
            }
            
        },

        update_info(){
            // console.log((this.user_firstname).length)
            if((this.user_firstname).length>0 && (this.user_lastname).length>0 && (this.address).length>0 && (this.mobile).length>0)
            {
                API.update_info(this.user_firstname,this.user_lastname,this.mobile,this.address,this.$store.state.email)
                .then(()=>{
                    this.$notify({ group: 'add_product',title: '<h3><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#fff" d="M20.285 2l-11.285 11.567-5.286-5.011-3.714 3.716 9 8.728 15-15.285z"/></svg>Successfull</h3>', text: '<h3>Your Information Updated Successfully</h3>' ,type:'success', width:'50%'})
                })
                .catch(()=>{
                    this.$notify({ group: 'add_product',title: '<h3><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#fff" d="M24 3.752l-4.423-3.752-7.771 9.039-7.647-9.008-4.159 4.278c2.285 2.885 5.284 5.903 8.362 8.708l-8.165 9.447 1.343 1.487c1.978-1.335 5.981-4.373 10.205-7.958 4.304 3.67 8.306 6.663 10.229 8.006l1.449-1.278-8.254-9.724c3.287-2.973 6.584-6.354 8.831-9.245z"/></svg> Error</h3>', text: '<h4>Error : Failed To Update , Please Check Your Internet Connection Or Try After Some Time</h4>' ,type:'error'})
                })
            }
            else
            {
                this.$notify({ group: 'input_error',title: '<h3><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="#fff" d="M24 3.752l-4.423-3.752-7.771 9.039-7.647-9.008-4.159 4.278c2.285 2.885 5.284 5.903 8.362 8.708l-8.165 9.447 1.343 1.487c1.978-1.335 5.981-4.373 10.205-7.958 4.304 3.67 8.306 6.663 10.229 8.006l1.449-1.278-8.254-9.724c3.287-2.973 6.584-6.354 8.831-9.245z"/></svg> Error</h3>', text: '<h4>Error : Please Fill All The Fields .</h4>' ,type:'error'})
            }
        }
    }


}
</script>

<style scoped>

*{
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}
.user_settings{
    background: linear-gradient(to right, #f9ca24,  #2ed573);
    overflow-x: hidden;
}
.container{
    background: #fff;
    width: 100vh;
    height: auto;
    margin: 0 auto;
    position: relative;
    margin-top: 3%;
    margin-bottom: 3%;
    box-shadow: 2px 5px 20px rgba(119,119,119,.5);
}
.profile img{
  margin: 20px 0;
  width: 150px;
  height: 150px;
  border-radius: 100%;
}
.details{
    padding-left: 10vh;

}
h1{
    font-family: "Montserrat", sans-serif;
    color: seagreen;
    margin-left: 4vh;
    margin-bottom: 7vh;
}
h2{
    color: #777;
    font-family: "Roboto", sans-serif;
    text-transform: uppercase;
    font-size: 18px;
    letter-spacing: 1px;
    margin-left: 2px;
    margin-bottom: 0;
}
.input,.inputs{
    border: 0;
    margin-bottom: 5px;
    border-bottom: 1px solid #3fb6a8;
    width: 60%;
    font-family: "Montserrat", sans-serif;
    font-size: 1em;
    padding: 7px 0;
    color: #070707;
    outline: none;
}
.btn{
    margin-left: 10px;
    font-family: "Roboto", sans-serif;
    text-transform: uppercase;
    font-size: 15px;
    border: 0;
    color: #fff;
    background: #45ca53;
    padding: 7px 15px;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.2);
    cursor: pointer;
}
@media all and (max-width:700px){
    .container{
        width: 100%;
        height: auto;
        
    }
    .button .btn{
        margin-top: 10px;
    }
    .inputs{
        width: 90%;
    }
    .details{
        padding-left: 7vh;
    }
}


</style>