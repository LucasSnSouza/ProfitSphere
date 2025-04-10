<template>

    <div 
        :class="theme"
        class="app-wrapper flex w-full h-full bg-color-brand-one oclude"
    >
        <div 
            v-if="$route.meta.sidebar"
            class="sidebar-frame flex flex-column gap-md h-full bg-color-brand-four p-md"
            style="padding-right: 0px;"
        >
            
            <ButtonBasic
                v-for="(item, index) in sidebar_buttons"
                :class="{'bg-color-brand-one': item.selected, 'bg-color-brand-four': !item.selected}"
                class="pointer aspect-ratio p-md flex x-center y-center"
                style="
                    border-top-left-radius: var(--scale-brand-md); 
                    border-bottom-left-radius: var(--scale-brand-md);
                "
                :key="index"
                @click="setSidebarSelect(index), $router.push( { path: item.navigation } )"
            >
                <div
                    :class="{'bg-color-brand-three': item.selected, 'bg-color-brand-four': !item.selected}" 
                    class="p-md bg-color-brand-three rounded-sm"
                >
                    <MiscIcon
                        :class="{'bg-color-brand-two': item.selected, 'bg-color-brand-three': !item.selected}" 
                        :icon="item?.icon"
                        :size="[28,28]"
                    />
                </div>
            </ButtonBasic>

        </div>
        <div class="view-frame w-full h-full">
            <RouterView/>
        </div>
    </div>

</template>

<script>

import { RouterLink, RouterView } from 'vue-router'

import { useSystemStore } from '@/stores/system.js'

import * as Button from "@/components/Button"
import * as Input from "@/components/Input"
import * as Misc from "@/components/Misc"
import * as Modal from "@/components/Modal"

export default {
    data(){
        return{
            debug: false,
            modal_login_type: "SINGIN",
            sidebar_buttons: [
                {
                    selected: true,
                    text: "Dashboard",
                    icon: "book-icon",
                    navigation: "/dashboard",
                },
                {
                    selected: false,
                    text: "Places",
                    icon: "place-icon",
                    navigation: "/places",
                },
                {
                    selected: false,
                    text: "Calendar",
                    icon: "calendar-icon",
                    navigation: "/calendar",
                }              
            ]
        }
    },
    components: {
        ...Button,
        ...Input,
        ...Misc,
        ...Modal
    },
    methods: {
        setView(value){
            this.$router.push({ path: value });
        },
        toggleTheme(){
            useSystemStore().toggleTheme();
        },
        toggleSidebar(){
            useSystemStore().toggleSidebar();
        },
        toggleLoggedState(value){
            useSystemStore().toggleLoggedState();
        },
        setSidebarSelect(item_index){
            this.sidebar_buttons.forEach((item, index) => {
                item.selected = false
            })
            this.sidebar_buttons[item_index].selected = true;
        }
    },
    computed: {
        title() {
            return this.$route.meta?.title;
        },
        theme() {
            return useSystemStore().getTheme;
        },
        sidebar(){
            return useSystemStore().getSidebar;
        },
        logged(){
            return useSystemStore().getLogged;
        }
    },
    created(){

    }
}

</script>

<style lang="scss">

.sidebar-frame{
    min-width: 70px;
}

.routeview-content{
    &.unfocus{
        filter: blur(20px);
    }
}

.app-layout-buttons{
    padding-bottom: 0px;
}

.title-app-wrapper{
    min-height: 180px;
    transition: .5s;
}

</style>
