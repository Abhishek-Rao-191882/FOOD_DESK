<template>
    <div class="reset_page">
        <div class="reset">
        <div class="form">
         <h2>Reset password</h2>
         <input type="password" name="username" placeholder="Old password" /><br /><br />
         <input type="password" name="username" placeholder="New password" /><br /><br />
         <input type="password" name="username" placeholder="Confirm new password" /><br /><br />
         <input type="button" value="Save" /><br /><br />
         <a href="#">Go back to Home page</a><br /><br />
        </div>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style  scoped>
.reset_page{
    width: 100%;
    height: 100vh;
    background-color: #ff944d;
}

.reset
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
a
{
    color: yellow;
    text-decoration: none;
    font-family: Tahoma, Geneva, sans-serif;
}
h2
{
   text-align: center; 
   color: #fff;
   margin-bottom: 35px;
}
input[type=password]
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
    margin-bottom: 25px;

}
input[type=button]:hover
{
    background: black;
    color: white;
}
::placeholder {
    color:aliceblue;
    opacity: 0.8; 
}
@media screen and (max-width: 1440px){
    .reset_page{
        width: 100%;
    }
    .reset{
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
    .reset_page{
        width: 100%;
    }
    .reset{
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
    .reset_page{
        width: 100%;
    }
    .reset{
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