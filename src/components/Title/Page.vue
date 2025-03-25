<template>

    <div class="title-page-wrapper w-full flex y-center gap-xlg justify-between">

        <div class="color-brand-two flex flex-column gap-md ">
            <div 
                class="flex flex-column gap-xsm p-lg rounded-sm bg-color-brand-four"
                style="padding-left: 16px; padding-right: 32px;"
            >
                <h1 
                    style="font-size: 11pt;"
                >
                    {{ title }}
                </h1>
                <p v-if="description" class="font-sm o-half">{{ description }}</p>

            </div>
            <!-- <MiscDivision></MiscDivision> -->
        </div>

        <div class="flex gap-md">
            <ButtonBasic
                class="p-lg bg-color-brand-four rounded-sm pointer"
            >
                <MiscIcon
                    class="bg-color-brand-two"
                    icon="find-icon"
                    :size="[20,20]"
                />
            </ButtonBasic>
            <InputBasic
                class="p-md bg-color-brand-four rounded-sm"
                input-class="color-brand-two"
                style="padding-left: 20px; padding-right: 20px;"
                placeholder="Search"
            />
            <ButtonBasic
                class="p-lg bg-color-brand-four rounded-sm pointer"
            >
                <MiscIcon
                    class="bg-color-brand-two"
                    icon="bell-icon"
                    :size="[20,20]"
                />
            </ButtonBasic>
            <ButtonBasic
                class="p-lg bg-color-brand-four rounded-sm pointer"
                @click="toggleTheme()"
            >
                <MiscIcon
                    class="bg-color-brand-two"
                    icon="theme-icon"
                    :size="[20,20]"
                />
            </ButtonBasic>
            <ButtonBasic
                class="p-lg bg-color-brand-four rounded-sm pointer"
            >
                <MiscIcon
                    class="bg-color-brand-two"
                    icon="exit-icon"
                    :size="[20,20]"
                />
            </ButtonBasic>
        </div>
        
    </div>

</template>

<script>

import { useSystemStore } from '@/stores/system.js'

import * as Button from "@/components/Button"
import * as Input from "@/components/Input"
import * as Misc from "@/components/Misc"

export default{
    data(){
        return{
        }
    },
    components: {
        ...Button,
        ...Input,
        ...Misc,
    },
    props:{
        title: {
            type: String
        },
        description: {
            type: String,
            default: null
        }
    },
    methods:{
        toggleTheme(){
            useSystemStore().toggleTheme();
        },
    },  
    created(){
    }
}

</script>