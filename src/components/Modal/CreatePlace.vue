<template>

    <div 
        class="modal-sidebar-place bg-color-brand-four absolute h-full p-xlg flex flex-column gap-lg color-brand-two"
        style="top: 0; right: 0;"
    >
        <div class="flex y-end gap-lg">
            <div class="bg-color-brand-three p-md rounded-sm">
                <MiscIcon
                    class="bg-color-brand-two"
                    icon="into-icon"
                    :size="[23,23]"
                />
            </div>
            <h1 class="font-sm">Create Place</h1>
        </div>

        <div class="flex flex-column gap-lg">

            <h1 class="font-sm">Commons</h1>
            <MiscDivision></MiscDivision>

            <InputBasic
                class="bg-color-brand-one p-lg rounded-sm"
                input-class="color-brand-two"
                placeholder="Name your place"
                v-model="form_place_modal['name']"
                :value="form_place_modal['name']"
            />

            <InputText
                class="bg-color-brand-one p-lg rounded-sm"
                input-class="color-brand-two"
                placeholder="Description this Place"
                v-model="form_place_modal['description']"
                :value="form_place_modal['description']"
            />

            <div 
                v-if="form_place_modal['tags'].length != 0"
                class="flex gap-sm"
            >
                <ButtonBasic
                    v-for="(item, index) in form_place_modal['tags']"
                    class="p-sm bg-color-brand-three rounded w-auto color-brand-two pointer"
                    style="padding-left: 12px;padding-right: 12px;"
                    :key="index"
                >
                    <p>{{ item.label }}</p>
                </ButtonBasic>
            </div>

            <h1 class="font-sm">Place Localization</h1>
            <MiscDivision></MiscDivision>

            <div class="flex w-full gap-md">
                <InputBasic
                    class="bg-color-brand-one p-lg rounded-sm"
                    input-class="color-brand-two"
                    placeholder="Postal Code"
                    v-model="form_place_modal['postalcode']"
                    :value="form_place_modal['postalcode']"
                />

                <InputBasic
                    class="bg-color-brand-one p-lg rounded-sm"
                    input-class="color-brand-two"
                    placeholder="State"
                    v-model="form_place_modal['state']"
                    :value="form_place_modal['state']"
                />

                <InputBasic
                    class="bg-color-brand-one p-lg rounded-sm"
                    input-class="color-brand-two"
                    placeholder="City"
                    v-model="form_place_modal['city']"
                    :value="form_place_modal['city']"
                />
            </div>

            <InputBasic
                class="bg-color-brand-one p-lg rounded-sm"
                input-class="color-brand-two"
                placeholder="Street"
                v-model="form_place_modal['street']"
                :value="form_place_modal['street']"
            />

            <h1 class="font-sm">References</h1>
            <MiscDivision></MiscDivision>

            <InputBasic
                class="bg-color-brand-one p-lg rounded-sm"
                input-class="color-brand-two"
                placeholder="Tags places"
                v-model="project_tags['text']"
                :value="project_tags['text']"
            />

            <div 
                v-if="project_tags['actual'].length != 0"
                class="flex gap-sm"
            >
                <ButtonBasic
                    v-for="(item, index) in project_tags['actual']"
                    class="p-sm bg-color-brand-three rounded w-auto ghost color-brand-three pointer"
                    style="padding-left: 12px;padding-right: 12px;"
                    :key="index"
                    @click="form_place_modal['tags'].push(item), project_tags['actual'] = [], project_tags['text'] = null"
                >
                    <p>{{ item.label }}</p>
                </ButtonBasic>
            </div>

        </div>

        <div class="flex gap-md w-half">
            <ButtonBasic
                class="p-md bg-color-brand-three rounded-md w-full color-brand-two pointer"
                @click="$emit('form', form_place_modal)"
            >
                <p>Create</p>
            </ButtonBasic>
            <ButtonBasic
                class="p-md bg-color-brand-three rounded-md w-full ghost color-brand-three pointer"
                @click="$emit('exit', true)"
            >
                <p class="color-brand-two">Cancel</p>
            </ButtonBasic>
        </div>
    </div>
    
</template>

<script>

import { useSystemStore } from '@/stores/system.js'

import Defaults from '@/defaults/'

import * as Button from "@/components/Button"
import * as Input from "@/components/Input"
import * as Misc from "@/components/Misc"

export default{
    data(){
        return{
            project_tags: {
                storage: Defaults.tags,
                actual: [],
                text: ""
            },
            form_place_modal: {
                tags: []
            }
        }
    },
    components: {
        ...Button,
        ...Input,
        ...Misc,
    },
    watch: {
        "project_tags.text": function(value){
            this.project_tags.actual = this.project_tags.storage.filter(item => item.label.includes(this.project_tags.text))
        }
    },
    methods:{
    },  
    created(){
    }
}

</script>

<style lang="scss">

.modal-sidebar-place{
    width: 400px;
}

</style>