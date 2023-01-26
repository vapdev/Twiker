<template>
    <div class="sticky top-0 left-0 px-2 h-screen max-lg:hidden">
        <div class="flex flex-col justify-between h-full">
            <div>
                <form method="get" action="">
                    <div class="flex flex-row p-2 my-2 border-solid border-2 border-gray-100 dark:border-gray-700 rounded-full">
                        <div>
                            <input class="text-sm h-fit w-full outline-none bg-white dark:bg-slate-900" type="text" name="query" placeholder="Search">
                        </div>
                        <div>
                            <button><i class="p-1 fa-solid fa-magnifying-glass"></i></button>
                        </div>
                    </div>
                </form>
            </div>
            <div class="relative w-full my-3" @click="toggle">
                <div class="flex justify-between w-full hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full">
                    <div class="flex p-1">
                        <img class="rounded-full h-12 w-12 m-auto" src="">
                        <h1 class="ml-1 font-semibold ">{{ user.username }}</h1>
                    </div>
                    <div class="flex m-3">
                        <i class="m-auto text-xl fa-solid fa-bars"></i>
                    </div>
                </div>
                <transition
                enter-active-class="transition ease-out duration-100"
                enter-from-class="transform opacity-0 scale-95"
                enter-to-class="transform opacity-100 scale-100"
                leave-active-class="transition ease-in duration-75"
                leave-from-class="transform opacity-100 scale-100"
                leave-to-class="transform opacity-0 scale-95"
                >
                    <div id="rSidebar_menu" v-show="active" class="absolute w-48 h-fit flex flex-col bottom-16 right-2 min-w-max bg-white dark:bg-slate-900 shadow-[0_0px_5px_2px_rgba(255,255,255,0.2)] rounded-md">
                        <div class="flex hover:bg-gray-200 dark:hover:bg-gray-700">
                            <a class="flex font-semibold text-lg p-1" onclick="">
                                <div class="flex w-11 h-11">
                                    <i class="text-xl m-auto fa-solid fa-moon"></i>
                                </div>
                                <span class="m-auto mx-3 max-[850px]:hidden">
                                    Dark mode
                                </span>
                            </a>
                        </div>
                        <div class="flex hover:bg-gray-200 dark:hover:bg-gray-700">
                            <router-link to="/edit" class="flex font-semibold text-lg p-1">
                                <div class="flex w-11 h-11">
                                    <i class="text-lg m-auto fa-solid fa-user-pen"></i>
                                </div>
                                <span class="m-auto mx-3 max-[850px]:hidden">
                                    Editar Profile
                                </span>
                            </router-link>
                        </div>
                        <div class="flex hover:bg-gray-200 text-red-500 dark:hover:bg-gray-700">
                            <router-link to="" class="flex font-semibold text-lg p-1">
                                <div class="flex w-11 h-11">
                                    <i class="text-xl m-auto rotate-180 fa-solid fa-right-from-bracket"></i>
                                </div>
                                <span class="m-auto mx-3 max-[850px]:hidden">
                                    Logout
                                </span>
                            </router-link>
                        </div>
                    </div>
                </transition>
            </div>
        </div>
    </div>        
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            active: false,
            user: '',
        }
    },
    mounted() {
        this.getUser()
    }, 
    methods: {
        toggle() {
            this.active = !this.active;
        },   
        async getUser(){
            await axios.get(``,) 
            .then(response => {
                this.user = response.data
            }).catch(error => {
                console.log('error' + error)
            })
        },
    }
}
</script>
