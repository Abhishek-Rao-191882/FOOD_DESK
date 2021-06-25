<template>
<div class="sign_up_page">
    <div class="signup">
    <div id="error_message" v-if="error_message">
        {{error_message}}
    </div>
    

 <!-- <form  id="myform"> -->
    <h2 style="color: #fff;">Sign Up</h2>
    <input type="alphabet" id="name" placeholder="First Name" required v-model="user.first_name"><br><br>
    <input type="alphabet" id="name" placeholder="Last Name" required v-model="user.last_name"><br><br>
    <input type="number" id="phone" placeholder="Mobile No." v-model="user.mobile_number"><br><br>
    <input type="email" id="email" placeholder="Email" v-model="user.email"><br><br>    
    <input type="password" id="password" placeholder="Password" v-model="user.password"><br><br>   
    <input type="password" id="confirmpassword" placeholder="Confirm Password" v-model="user.re_password"><br><br>  
    <input type="textarea" id="address" placeholder="Address" required v-model="user.address"><br><br>
    <button class="signupbutton" @click="validate" >Sign up</button><br><br>
 <!-- </form> -->
 <div class="already">
    Already have account?<router-link to="/login" style="text-decoration: none; font-family: 'Play', sans-serif; color: yellow;">&nbsp;Log In</router-link>
 </div>
</div>
</div>
    
</template>

<script>

import API from '../API/API'



export default {
    data() {
        return {
        
            user:{
                first_name:'',
                last_name:'',
                email:'',
                mobile_number:'',
                password:'',
                re_password:'',
                address:'',
            },
            error_message:''
        }
    },
    methods:{
        validate()
        {
            var regxE = /^([a-z A-z 0-9 \.]+)@([a-z A-Z 0-9 -]+).([a-z]{2,8})(.[a-z]{2,8})?$/;
            var regxM = /[6-9]\d{9}/;
            this.error_message=" ";
            if(this.user.first_name && this.user.last_name && this.user.email && this.user.password && this.user.re_password && this.user.mobile_number)
            {
                if(!regxE.test(this.user.email))
                {
                    this.error_message="Invalid Email Address";
                    return;
                } 
                if(!regxM.test(this.user.mobile_number))
                {
                    this.error_message="Invalid Mobile Number";
                    return;
                }
                if(this.user.password != this.user.re_password)
                {
                    this.error_message="Password And Confirmed Password Should Be Same.";
                    return;
                }
                if(this.user.password != this.user.re_password)
                {
                    this.error_message="Password And Confirmed Password Should Be Same.";
                    return;
                }
                
                //    Submit Form
                this.sign_up();
                this.error_message="SUBMITTED. To Confirm your account please verify it from your mail. ";
                return;
            }
            this.error_message="all fields are required";

        },


        sign_up(){
            API.sign_up(this.user)
            .then(()=>{
                console.log('Successfull')
            })
            .catch(()=>{
                console.log('Failed')
            })
        },

    }
}
</script>

<style scoped>

.sign_up_page{
    background-color: #ff944d;
    width: 100%;
    height: 100vh;
    padding-top: 8vh;
}
body
{
    background: #fff;
    font-family: Tahoma, Geneva, sans-serif;
    color: #fff;
    background-size: cover;
}
.signup
{
    background:rgba(44, 62, 80, 0.7);
	padding: 1vh 5vh 3vh 4vh;
    width:30%;
    border-radius: 20px;
	height: 85vh;
	margin:0 auto;
    /* margin-top:13vh; */
    /* padding-top: 13vh; */
    text-align: center;
}
#error_message{
    margin-bottom: 0.5vh;
    background: green;
    padding: 0;
    text-align: center;
    font-size: 14px;
    transition: all 0.5s ease;
  }
form
{
    width: 30vh;
    text-align: center;
    padding: 0 20px;
}
input
{
    
    width: 34vh;
    text-align: center;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    font-family: 'Play', sans-serif;
    font-size: 16px;
    font-weight: 200px;
    padding: 1.5vh 0;
    transition: border 0.5s;
    outline: none;
    color: #fff;
}
.signupbutton
{
    border: none;
    width: 28vh;
    background: white;
    color: #000;
    font-size: 16px;
    line-height: 2.8vh;
    padding: 10px 0;
    border-radius: 15px;
    cursor: pointer;
}
.signupbutton:hover
{
    color: #fff;
    background-color: black;
}
h2
{
    color: #000;
    padding: 0;
    
}
::placeholder {
    color:aliceblue;
    opacity: 0.8; /* Firefox */
}
/* #msg {
    visibility: hidden;
    min-width: 250px;
    background-color:yellow;
    color: #000;
    text-align: center;
    border-radius: 2px;
    padding: 16px;
    position: fixed;
    z-index: 1;
    right: 30%;
    top: 30px;
    font-size: 17px;
	margin-right:30px;
}

#msg.show {
    visibility: visible;
    -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
    animation: fadein 0.5s, fadeout 0.5s 2.5s;
} */

@-webkit-keyframes fadein {
    from {top: 0; opacity: 0;} 
    to {top: 30px; opacity: 1;}
}

@keyframes fadein {
    from {top: 0; opacity: 0;}
    to {top: 30px; opacity: 1;}
}

@-webkit-keyframes fadeout {
    from {top: 30px; opacity: 1;} 
    to {top: 0; opacity: 0;}
}

@keyframes fadeout {
    from {top: 30px; opacity: 1;}
    to {top: 0; opacity: 0;}
}
 
@media all and (max-width: 1000px){
    
    .signup{
        width: 100%;
        height: 112%;
        margin: 0;
        font-size: 10px;
       text-align: center; 

    }
    form{
        width: 100%;
        text-align: center;
    }
    form h2{
        margin-top: 0vh;
        font-size: 60px;
        font-weight: bolder;

    }
    input{
        width: 90%;
        font-size:20px;
        font-weight: bolder;
        border-bottom: 3px solid #fff;
    }
    input[type=submit]{
        width: 30vh;
        height: 6vh;
        font-size: 15px;
    }
    input[type=submit]:hover
    {
        color: #fff;
        background-color: black;
    }
/* #msg {
    font-size: 40px;
    margin-left:100px;
    width: 600px;
} */
    .already{
        font-size: 10px;
    }
    #error_message{
        background: #e90d14;
        padding: 0px;
        text-align: center;
        font-size: 12px;
        transition: all 0.5s ease;
    }

}    
   
</style>