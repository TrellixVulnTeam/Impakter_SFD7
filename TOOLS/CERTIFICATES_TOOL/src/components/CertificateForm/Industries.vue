<template>
  <div>
    <b-container>
      <b-row>
        <progress-bar :currentStep="3"> </progress-bar>
      </b-row>
      <b-row>
        <b-col> </b-col>
        <b-col cols="8">
          <b-form-group
            label="Please select all the industries applicable to this certificate"
            v-slot="{ ariaDescribedby }"
            label-size="lg"
          >
            <b-form-checkbox
              class="flex_and_start"
              v-model="allSelected"
              :indeterminate="indeterminate"
              @change="toggleAll"
            >
              <b>{{ allSelected ? "Un-select All" : "Select All" }}</b>
            </b-form-checkbox>
            <b-form-checkbox-group
              id="checkbox-group-1"
              v-model="selected"
              :options="industries"
              :aria-describedby="ariaDescribedby"
              name="flavour-1"
              stacked
            ></b-form-checkbox-group> </b-form-group
        ></b-col>

        <b-col> </b-col>
      </b-row>
      <b-row class="buttons_row">
        <b-button @click="back">Back</b-button>
        <b-button variant="primary" @click="next">Next</b-button>
      </b-row>
    </b-container>
    <!--<b-card class="mt-3" header="Form result so far">
      <pre class="m-0">{{ form }}</pre>
    </b-card>-->
  </div>
</template>

<script>
import IndustryMixin from "../../mixins/IndustryMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";
import ProgressBar from "../Shared/ProgressBar.vue";
export default {
  name: "FormIndustries",
  data() {
    return {
      selected: [],
      allSelected: false,
    };
  },
  methods: {
        toggleAll(checked) {
        this.selected = checked ? this.industries.map(x => {
          return x.value
        }): []
      },
    next() {
      this.selected.sort();
      this.$store.dispatch("addIndustries", this.selected);
      this.$router.push({ name: "formPage3-2" });
    },
    back() {
      this.$router.go(-1);
    },
  },
  mounted() {
    this.selected = this.form.industries;
  },
  mixins: [IndustryMixin, CertificateFormMixin],
  components: { ProgressBar },
};
</script>

<style scoped>
#checkbox-group-1 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
}
</style>
