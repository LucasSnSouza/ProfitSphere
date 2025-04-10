<template>

    <div class="validate-view-wrapper w-full h-full p-xlg bg-color-brand-one flex flex-column y-end x-center gap-xlg">

        <div 
            class="flex flex-column bg-color-brand-four w-half p-xlg rounded-md color-brand-two gap-lg"
        >

            <div class="flex">
                <div class="p-md bg-color-brand-three rounded-sm">
                    <MiscIcon
                        class="bg-color-brand-two"
                        icon="settings-icon"
                        :size="[26,26]"
                    />
                </div>
            </div>
            <div class="flex flex-column">
                <h1 class="font-md">Enterprise Connect</h1>
                <p class="font-sm o-half w-half">
                    Connect to manage your businesses, 
                    expand your empire, and interact with a dynamic world.
                </p>
            </div>
            <div v-if="type_form_selected == 'SINGIN'" class="flex flex-column gap-lg w-half">
                <InputBasic
                    class="bg-color-brand-one p-lg rounded-sm flex"
                    input-class="color-brand-two"
                    placeholder="Access code..."
                    v-model="form_local_singin['access']"
                    :value="form_local_singin['access']"
                >
                    <MiscIcon
                        class="bg-color-brand-two"
                        style="margin-right: 1px;"
                        icon="into-icon"
                        :size="[22,22]"
                    />    
                </InputBasic>

                <MiscDivision></MiscDivision>

            </div>
            <div v-else class="flex flex-column gap-lg w-half">
                <InputBasic
                    class="bg-color-brand-one p-lg rounded-sm flex"
                    input-class="color-brand-two"
                    placeholder="Business name ..."
                    v-model="form_local_singup['name']"
                    :value="form_local_singup['name']"
                />
                <InputText
                    class="bg-color-brand-one p-lg rounded-sm flex"
                    input-class="color-brand-two"
                    placeholder="Business description ..."
                    v-model="form_local_singup['description']"
                    :value="form_local_singup['description']"
                />
                <InputBasic
                    class="bg-color-brand-one p-lg rounded-sm flex"
                    input-class="color-brand-two"
                    placeholder="Access code..."
                    v-model="form_local_singup['access']"
                    :value="form_local_singup['access']"
                />

                <MiscDivision></MiscDivision>

            </div>
            <div 
                class="flex gap-md"
            >
                <div v-if="type_form_selected == 'SINGIN'" class="flex gap-md">
                    <ButtonBasic
                        class="p-lg rounded-md bg-color-brand-three color-brand-two pointer"
                        style="padding-left: 32px;padding-right: 32px;"
                        @click="getEnterpriseByAccess()"
                    >
                        <p>Connect</p>
                    </ButtonBasic>
                    <ButtonBasic
                        class="p-lg rounded-md color-brand-three ghost pointer"
                        style="padding-left: 32px;padding-right: 32px;"
                        @click="type_form_selected = 'SINGUP'"
                    >
                        <p class="color-brand-two">Create Business</p>
                    </ButtonBasic>
                </div>
                <div v-else class="flex gap-md">
                    <ButtonBasic
                        class="p-lg rounded-md bg-color-brand-three color-brand-two pointer"
                        style="padding-left: 32px;padding-right: 32px;"
                        @click="createEnterprise()"
                    >
                        <p>Create</p>
                    </ButtonBasic>
                    <ButtonBasic
                        class="p-lg rounded-md color-brand-three ghost pointer"
                        style="padding-left: 32px;padding-right: 32px;"
                        @click="type_form_selected = 'SINGIN'"
                    >
                        <p class="color-brand-two">Go Connect</p>
                    </ButtonBasic>
                </div>
                <ButtonBasic
                    class="p-lg bg-color-brand-three rounded-md pointer"
                    @click="toggleTheme()"
                >
                    <MiscIcon
                        class="bg-color-brand-two"
                        icon="theme-icon"
                        :size="[20,20]"
                    />
                </ButtonBasic>
            </div>
        </div>

    </div>
    
</template>

<script>

import { useSystemStore } from '@/stores/system.js'
import { usePlaceStore } from '@/stores/place.js'
import { useEnterpriseStore } from '@/stores/enterprise.js'

import Utils from '@/utils/';
import Defaults from '@/defaults/';

import * as Button from "@/components/Button"
import * as Input from "@/components/Input"
import * as Misc from "@/components/Misc"
import * as Modal from "@/components/Modal"
import * as Title from "@/components/Title"

export default{
    data(){
        return{
            type_form_selected: "SINGIN",
            form_local_singin: {},
            form_local_singup: {}
        }
    },
    components: {
        ...Button,
        ...Input,
        ...Misc,
        ...Modal,
        ...Title
    },
    computed:{
    },
    methods:{
        toggleTheme(){
            useSystemStore().toggleTheme();
        },
        createEnterprise(){
            useEnterpriseStore().fetchCreateEnterprise(this.form_local_singup)
        },
        async getEnterpriseByAccess(){
            try{
                await useEnterpriseStore().fetchEnterpriseByAccess(this.form_local_singin?.access)
                this.$router.push({ path: "dashboard" })
            }
            catch (error){
                
            }
        }
    },
    async created(){

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