import { defineStore } from "pinia";

import Utils from "@/utils/"

export const usePlaceStore = defineStore('place', {
    state: () => ({
        list_of_places: [],
        last_data_created_place: null
    }),
    getters: {
        getListPlaces: (state) => state.list_of_places,
        getLastDataCreatedPlace: (state) => state.last_data_created_place
    },
    actions: {
        async fetchListPlaces(){
            await Utils.fetch.request("/places", "GET").then(({ data }) => {
                this.list_of_places = data
            })
        },
        async fetchCreatePlace(form){
            await Utils.fetch.request("/create-place", "POST", form).then(({ data }) => {
                this.last_data_created_place = data
            })
        }
    }
})