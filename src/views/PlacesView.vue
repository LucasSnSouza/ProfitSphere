<template>

    <div class="places-view-wrapper w-full h-full p-xlg bg-color-brand-one flex flex-column gap-xlg scroll-y">

        <TitlePage
            :title="$route.meta.title"
            :description="$route.meta.description"
        />
    
        <div class="w-full flex flex-column gap-lg">

            <div class="flex gap-lg wrap">
                <div
                    v-for="(item, index) in places"
                    class="flex flex-column card gap-md"
                    :key="index"
                >
                    <ButtonBasic
                        class="animation-scale-active color-brand-two bg-color-brand-four rounded-md p-lg flex flex-column gap-md pointer"
                        @click="item.opened = !item.opened"
                    >
                        <div class="flex flex-column text-start color-brand-two gap-sm">
                            <h1 class="font-sm">{{ item?.title }}</h1>
                            <p class="font-xsm o-half">{{ item?.description }}</p>
                        </div>
                        <div class="flex gap-md">
                            <ButtonBasic
                                v-for="(tag, tag_index) in item.tags"
                                :key="tag_index"
                                class="bg-color-brand-three rounded-sm p-sm"
                                style="padding-left: 12px;padding-right: 12px;"
                            >
                                <p class="font-xsm color-brand-one">{{ tag }}</p>
                            </ButtonBasic>
                        </div>
                    </ButtonBasic>
                    <div 
                        v-if="item?.opened"
                        class="w-full flex gap-md"
                    >
                        <ButtonBasic
                            class="animation-scale-active color-brand-two bg-color-brand-three rounded-md p-md flex flex-column gap-md pointer"
                        >
                            <MiscIcon
                                class="white"
                                icon="play-icon"
                                :size="[14,14]"
                            />
                        </ButtonBasic>
                        <ButtonBasic
                            class="animation-scale-active color-brand-two bg-color-brand-three rounded-md p-md flex flex-column gap-md pointer"
                        >
                            <MiscIcon
                                class="white"
                                icon="edit-icon"
                                :size="[14,14]"
                            />
                        </ButtonBasic>
                    </div>
                </div>
            </div>
            
        </div>

        <ButtonBasic
            class="animation-scale-active bg-color-brand-three absolute rounded-sm p-md shadow-sm pointer"
            style="bottom: var(--scale-brand-xlg); right: var(--scale-brand-xlg);"
        >
            <MiscIcon
                class="white"
                icon="plus-icon"
                :size="[18,18]"
            />
        </ButtonBasic>

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
        this.places = this.places.map(item => ({
            ...item,
            opened: false
        }))
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