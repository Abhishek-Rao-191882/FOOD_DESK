import axios from 'axios'
var instance = axios.create({
    baseURL:process.env.VUE_APP_SERVER,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: "X-CSRFTOKEN",  
})
// axios.defaults.headers['x-csrf-token'] = localStorage.getItem('checks');
export default {
    reset(){
        // console.log(localStorage.getItem('checks'))
        // const headers = {"X-CSRFTOKEN": "uZGHk5WWk9cC3ILehSQER7EqYXWV6OZExuUVMmV7zjTBnbGgUCPXkOR8d0Xck2Ro"}
        return axios.post(process.env.VUE_APP_SERVER+'/accounts/reset_password/',{"email":'saraswatsourabh5@gmail.com'}
        // ,{//     headers: headers
        // }
        )
    },
    log_in(username,password){
        return axios.post(process.env.VUE_APP_SERVER+'/accounts/login',{"username":username,"password":password})
    },
    log_out(token){
        return axios.post('http://localhost:8000/accounts/logout',{"token":token})
    },

    update_info(f_name,l_name,mobile,address,email){
        return axios.put(process.env.VUE_APP_SERVER+'/accounts/update_client_info',{"first_name":f_name,"last_name":l_name,"Mobile_No":mobile,"address":address,"email":email})
    },

    sign_up(user){
        console.log(user)
        return axios.post(process.env.VUE_APP_SERVER+'/accounts/sign_up/',{"email":user.email,"password":user.password,"mobile":user.mobile_number,"address":user.address,"first_name":user.first_name,"last_name":user.last_name})
    },
    AddToCart(product_id,seller_id,client_id,quantity){
        return axios.post(process.env.VUE_APP_SERVER+'/client/cart/',{"Product_Id": product_id,"Seller": seller_id,"Client_Id": client_id,"Quantity":quantity})
    },
    GetCart(user_id){
        console.log(user_id)
        return axios.get(process.env.VUE_APP_SERVER+`/client/cart/?user_id=${user_id}`)
    },
    DeleteCart(cart_product_id){
        // console.log(cart_product_id+' sda')
        
        return axios.delete(process.env.VUE_APP_SERVER+`/client/cart/${cart_product_id}/`)
    },

    checkout(amount){
        return axios.post(process.env.VUE_APP_SERVER+'/paytm_gateway/payment/',{"amount":amount})
    },

    search(search_text){
        return axios.get(process.env.VUE_APP_SERVER+`/client/search/?search=${search_text}`)
    }
    
}






// {'verified': True, 'paytm': {'TXNID': '20200823111212800110168307401930305', 'BANKTXNID': '12889548728', 'ORDERID': 'eTJ9nz', 'TXNAMOUNT': '100.00', 'STATUS': 'TXN_SUCCESS', 'TXNTYPE': 'SALE', 'GATEWAYNAME': 'SBI', 'RESPCODE': '01', 'RESPMSG': 'Txn Success', 'BANKNAME': 'SBI', 'MID': 'zwfsDv38259108810773', 'PAYMENTMODE': 'NB', 'REFUNDAMT': '0.00', 'TXNDATE': '2020-08-23 16:45:38.0'}}
