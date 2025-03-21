<template>

    <div class="places-view-wrapper w-full h-full p-xlg bg-color-brand-one flex flex-column gap-xlg scroll-y">

        <TitlePage
            :title="$route.meta.title"
            :description="$route.meta.description"
        />
    
    </div>
    
</template>

<script>

import { useSystemStore } from '@/stores/system.js'

import Utils from '@/utils/';
import Defaults from '@/defaults/';

import * as Button from "@/components/Button"
import * as Input from "@/components/Input"
import * as Misc from "@/components/Misc"
import * as Title from "@/components/Title"

export default{
    data(){
        return{
            places: Defaults.places
        }
    },
    components: {
        ...Button,
        ...Input,
        ...Misc,
        ...Title
    },
    methods:{
    },  
    created(){
    }
}

</script>

<style lang="scss">

.white{
    background: white;
}

.card{
    max-width: 20vw;
}

</style>