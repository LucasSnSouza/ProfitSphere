<template>

    <div class="validate-view-wrapper w-full h-full p-xlg bg-color-brand-one flex flex-column x-center gap-xlg">

        <div 
            class="flex flex-column bg-color-brand-four w-half p-xlg rounded-md color-brand-two gap-lg"
        >
            <h1 class="font-md">{{ informations_form[information_index].title }}</h1>
            <p class="font-sm o-half w-half">{{ informations_form[information_index].description }}</p>
            <div 
                class="flex gap-md"
                style="margin-top: 24px;"
            >
                <ButtonBasic
                    v-if="information_index != 0"
                    class="p-md rounded-md color-brand-three ghost pointer"
                    style="padding-left: 32px;padding-right: 32px;"
                    @click="information_index--"
                >
                    <p class="color-brand-two">Return</p>
                </ButtonBasic>
                <ButtonBasic
                    class="p-md rounded-md bg-color-brand-three color-brand-two pointer"
                    style="padding-left: 32px;padding-right: 32px;"
                    @click="setNextFrame"
                >
                    <p>{{ informations_form[information_index].button }}</p>
                </ButtonBasic>
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
            information_index: 0,
            informations_form: [
                {
                    title: "Começo da Jornada",
                    description: `Comece em um terreno vazio e descubra como transformar o espaço em um império. 
                    Construa sua primeira empresa e aprenda a administrar seus recursos.`,
                    button: "Next"
                },
                {
                    title: "Expansão e Diversificação",
                    description: `Ao conquistar seu primeiro sucesso, você poderá expandir e diversificar seus negócios. 
                    Abra novas empresas, seja uma fazenda ou um aeroporto, e gerencie diferentes setores.`,
                    button: "Next"
                },
                {
                    title: "Enfrentando Desafios",
                    description: `O caminho do empreendedorismo não é fácil. Desafios climáticos e mudanças 
                    no mercado testarão suas habilidades de gerenciamento e adaptação.`,
                    button: "Next"
                },
                {
                    title: "Conectando-se com Outros Empresários",
                    description: `Expanda sua rede criando parcerias com empresas de outros jogadores, 
                    trocando recursos e explorando novas oportunidades de negócios no mundo online.`,
                    button: "Get Start"
                }
            ]
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
        computed_places(){
            return usePlaceStore().getListPlaces
        }
    },
    methods:{
        toggleTheme(){
            useSystemStore().toggleTheme();
        },
        setNextFrame(){
            if(this.information_index > this.informations_form.length - 2){
                this.$router.push({ path: "/validate" })
                return;
            }
            this.information_index++
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