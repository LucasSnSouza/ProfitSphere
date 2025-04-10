import { defineStore } from "pinia";

import Utils from "@/utils/"

export const useEnterpriseStore = defineStore('enterprise', {
    state: () => ({
        enterprise: null
    }),
    getters: {
        getEnterprise: (state) => state.enterprise
    },
    actions: {
        async fetchCreateEnterprise(form){
            await Utils.fetch.request("/create-local-enterprise", "POST", form).then(({ data }) => {
                this.enterprise = data
            })
        },
        async fetchEnterpriseByAccess(id){
            await Utils.fetch.request(`/enterprise/access/${id}`, "GET").then(({ data }) => {
                this.enterprise = data
            })
        }
    }
})