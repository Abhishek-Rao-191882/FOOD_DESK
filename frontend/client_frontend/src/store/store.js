import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import API from '../API/API'

Vue.use(Vuex);

export default new Vuex.Store({

    state:{
        first_name:"",
        last_name:"",
        Mobile_No:"",
        address:"",
        client_id:"",
        email:"",
        token:localStorage.getItem("token"),
        
        prevArray:[],

        ordersArray:"",
        ordersAmount:"",
    },

    getters:{
        // get(state){
        //     var data={first_name:first_name:state.name,mobile_number:state.mobile_number}
        //     return data
        // },
        getPrevArray(state)
        {
            // console.log(state.prevArray);
            return state.prevArray;
        }
    },

    mutations:{
        NEW_STATE(state , message)
        {
            state.user.push({
                name:message
            })
            // console.log(this.state.user)

        },

        DELETE_STATE(state, message)
        {
            let index = state.user.indexOf(message);
            state.user.splice(index,1);
        },

        AuthState(state, Token)
        {
            // console.log(Token)
            state.token = Token            
            
        },
        ClientDataState(state, User_info)
        {
            state.first_name = User_info.user.first_name;
            state.last_name = User_info.user.last_name;
            state.Mobile_No = User_info.Mobile_No;
            state.address = User_info.address;
            state.client_id = User_info.user.id;
            state.email = User_info.user.email;

            // state.last_name = Lname;
        },
        getPrevArray(state, array)
        {
            for(var i=0;i<array.length;i++)
            {
                state.prevArray.push(array[i])
            }
        },
        OrdersArray(state, order){
            state.ordersArray = order['order']
            state.ordersAmount = order['amount']
        }


    },

    actions:{
        orders({commit}, order){
            // console.log(total)
            commit('OrdersArray', order)
        },

        getPrevArray({commit}, array){
            
            commit('getPrevArray', array)

        },
        AuthTokenState({commit},token){
            // console.log(token)
            commit('AuthState', token)
            
            // console.log("Second")
        },

        ClientData({commit}, Client_info){
            // console.log(Client_info)
            commit('ClientDataState', Client_info)
        },


        addState({commit},message){
            commit('NEW_STATE',message)
        },
        delete({commit},message){
            commit('DELETE_STATE',message)
        }
    }

})