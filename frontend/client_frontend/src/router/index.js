import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/Products'
import Search from '../views/search'

import Navbar from '../views/navbar2.vue'
import Cart from '../views/cart.vue'
import Sign_Up from '../views/Sign_Up.vue'
import Login from '../views/login.vue'
import User_Settings from '../views/user_settings.vue'


import Address from '../views/address.vue'
import product_details from '../views/Product_Details.vue'

import transaction_status from '../views/transaction_status.vue'





Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/sign_up',
    name: 'Sign_Up',
    component: Sign_Up
  },

  

  
  

  {
    path: '/',
    name: 'Home',
    
    component: Navbar,
    children:[
      {
        path: '/',
        name: 'home',
        component: Home,
        props: true,
    
      },
      {
        path: '/user/user_settings',
        name: 'User_Settings',
        component: User_Settings
      },
     {
        path: '/products',
        name: 'Products',
        component: Product,
        props: true,
    
      },
      {
        path: '/products',
        name: 'Products',
        component: Product,
        props: true,
    
      },
      {
        path: '/search',
        name: 'Search',
        component: Search,
        props: true,
    
      },
      {
        path: '/cart',
        name: 'Cart',
        component: Cart,
        props: true,
    
      },
      {
        path: '/address',
        name: 'Address',
        component: Address,
        props: true,
    
      },
      {
        path: '/product_details',
        name: 'Product_Details',
        component: product_details,
        props: true,
    
      },
     
      {
        path: '/transaction_status',
        name: 'Transaction_Status',
        component: transaction_status,
        props: true,
    
      },
    ]
  },
  
  
  {
    path: '/*',
    name: 'Home',
    component: Navbar
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
export default router
