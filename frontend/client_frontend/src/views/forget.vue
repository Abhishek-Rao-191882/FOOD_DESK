<template>
    <div class="forget_page">
     <div class="forget">
       <div class="form">
         <h2 align="center" style="color:#fff;">Forget password</h2>
         <h5>
             Enter email here that you used on your account.We will send a link on your email to reset your password.
         </h5>
         <input type="text" name="username" placeholder="Enter your registered email" /><br /><br />
         <input type="button" value="Send"/><br /><br />
         <a href="#" style="">Go back to Home page</a><br /><br />
       </div>
     </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style  scoped>
.forget_page{
    width: 100%;
    height: 100vh;
    background-color:  #ff944d;

}
.forget
{
    background: rgba(44,62,80,0.7);
    padding: 40px;
    width: 25%;
    height: 75vh;
    border-radius: 20px;
    position: absolute;
    top: 50%;
    left: 50%;
    -moz-transform: translateX(-50%) translateY(-50%);
    -webkit-transform: translateX(-50%) translateY(-50%);
    transform: translateX(-50%) translateY(-50%);
    text-align: center;
}
h2
{
    margin-bottom: 28px;
    /* margin-left: 10px; */
}
h5{
    font-size:14px;
    color:yellow;
    margin-bottom: 35px;
}
a
{
    color: yellow;
    text-decoration: none;
    font-family: Tahoma, Geneva, sans-serif;
    text-align: center;
}
input[type=text]
{
    width: 240px;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    font-family: 'Play', sans-serif;
    font-size: 16px;
    font-weight: 200px;
    padding: 10px 0;
    transition: border 0.5s;
    text-align: left;
    padding: 10px;
    color: white;
}
input[type=button]
{
    border: none;
    background: white;
    color: black;
    font-size: 16px;
    line-height: 25px;
    padding: 10px 0;
    border-radius: 12px;
    cursor: pointer;
    width: 180px;
    margin-bottom: 40px;
}
input[type=button]:hover
{
    background: black;
    color: white;
}
::placeholder {
    color:aliceblue;
    opacity: 0.8; /* Firefox */
}
@media screen and (max-width: 1440px){
    .forget_page{
        width: 100%;
    }
    .forget{
    height: 70vh;
    width: 40%;
    margin: 0;
    padding: 40px;
    }
    input{
        width: 100%;
    }
    input[type=button]{
        width: 240px;
    }
}
@media screen and (max-width: 768px) {
    .forget_page{
        width: 100%;
    }
    .forget{
        height: 90vh;
        width: 80%;
        margin: 0;
        padding: 40px;
    }
    input{
        width: 100%;
    }
    input[type=button]{
        width: 240px;
    }
}
@media screen and (max-width: 428px) {
    .forget_page{
        width: 100%;
    }
    .forget{
        height: 90vh;
        width: 80%;
        margin: 0;
        padding: 10px;
    }
    input{
        width: 230px;
    }
    input[type=button]{
        width: 200px;
    }
}

</style>