import Vue from 'vue'
import VueRouter from 'vue-router'
import SellerLogin from '../views/Seller_Login.vue'
import Products from '../views/Products.vue'
import Home from '../views/Home.vue'
import Categories from '../views/Categories.vue'
import Orders from '../views/orders.vue'
import Active_Orders from '../views/active_orders.vue'
import Rejected_Orders from '../views/rejected_orders.vue'





import Axios from 'axios'



Vue.use(VueRouter)

function guardMyroute(to, from, next)
{

 if(localStorage.getItem('token')) 
 {
   const token = localStorage.getItem('token')
  Axios.post(process.env.VUE_APP_SERVER+'/accounts/sellerlogin',{"token":token})
          .then((response)=>{
            const msg = "Only Hotels Are Allowed"

            // console.log("Second")
            if(msg==response.msg)
                next("/")
            else
              next()
          }
            )
        .catch( ()=>{
          localStorage.removeItem('token')
          console.log("Second 2")
          next("/")
        } 
        )
 } 
 else
 {
  next('/'); // go to '/login';
 }
}
// function LoginPageGuard(to, from, next)
// {

//  if(localStorage.getItem('token')) 
//  {
//    console.log("working")
//    const token = localStorage.getItem('token')
//    Axios.post('http://localhost:8000/seller/sellerlogin',{"token":token})
//           .then(()=>{
//             next('/home')
//           }
//             )
//         .cache( ()=>{
//           next("/")
//         } 
//         )
//  } 
// }

  const routes = [
  {
    path: '/',
    name: 'SellerLogin',
    // afterEnter: LoginPageGuard,
    component: SellerLogin
  },
  {
    path: '/home',
    name: 'Home',
    beforeEnter: guardMyroute,
    component: Home,
    children:[
      {
        path: '/products',
        name: 'Products',
        component: Products,
        props: true,
        // beforeEnter: (to, from, next) => {
        //   // ...
        //   if(localStorage.getItem("token"))
        //   {
        //     Axios.post()
        //       .then(()=>{
        //         next();
        //       }
        //         )
        //     .cache()
            
        //   }
        //   to("/login");
        // }
      },
      {
        path: '/categories',
        name: 'Categories',
        component: Categories,
        props: true,
      },
      {
        path: '/orders',
        name: 'Orders',
        component: Orders,
        props: true,
      },
      {
        path: '/active_orders',
        name: 'Active_Orders',
        component: Active_Orders,
        props: true,
      },
      {
        path: '/Rejected_Orders',
        name: 'Rejected_Orders',
        component: Rejected_Orders,
        props: true,
      },
    ]
  },
  
  {
    path: '/*',
    name: 'Home',
    component: Home
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
