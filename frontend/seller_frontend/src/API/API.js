import axios from "axios";
var instance=axios.create({
    baseURL:process.env.VUE_APP_SERVER
})

export default {
    login()
    {   
        return instance.post("/login");
    },

    authenticate(username,password)
    {
        // console.log({"username":username,"password":password})
        return axios.post(process.env.VUE_APP_SERVER+'/accounts/login',{"username":username,"password":password})
    },

    UserInfo(){
        const token = localStorage.getItem('token')
        return axios.post('http://localhost:8000/accounts/sellerlogin',{"token":token})
    },

    logout(){
        const token = localStorage.getItem('token')
        return axios.post('http://localhost:8000/accounts/logout',{"token":token})
    },

    getProducts(id){
        // const id = user_id
        return axios.get(`http://localhost:8000/seller/products/${id}`)
    },

    EditProducts(product_id,formData2){
        return axios.put(`http://localhost:8000/seller/products/${product_id}`,formData2)
    },

    DeleteProducts(data){
        return axios.delete(`http://localhost:8000/seller/products/${data.id}`)
    },

    getCategories(id){
        return axios.post('http://localhost:8000/seller/categories',{"userId":id})
    },

    AddCategories(id,category_name){
        return axios.post('http://localhost:8000/seller/categoriesOperations/',{'Seller':id,'Category_Name':category_name})
    },

    EditCategories(id,category_id,category_name){
        return axios.put(`http://localhost:8000/seller/categoriesOperations/${category_id}/`,{'Seller':id,'Category_Name':category_name})
    },

    DeleteCategories(id){
        return axios.delete(`http://localhost:8000/seller/categoriesOperations/${id}`)
    },

    getOrders(id,type){
        return axios.get(`http://localhost:8000/orders/seller_get_orders/${id}/${type}`)
    },
    
    acceptOrder(id,user_id,acceptance_status){
        return axios.post("http://localhost:8000/orders/seller_get_orders/",{'id':id,'Seller_id':user_id,'Acceptance_Status':acceptance_status})
    }
    // login(data,token)
    // {
    //     return instance.post("/login");
    // },
    // register()
    // {
    //     return instance.post();
    // }
}

