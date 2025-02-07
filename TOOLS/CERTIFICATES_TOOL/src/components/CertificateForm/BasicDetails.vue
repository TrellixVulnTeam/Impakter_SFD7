<template>
  <div>
    <b-container>
      <b-row>
        <progress-bar :currentStep="1"> </progress-bar>
      </b-row>
      <b-row class="main_row">
        <b-col></b-col>
        <b-col cols="8">
          <b-form @submit="onSubmit" @reset="onReset">
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Name of the Certificate:"
              label-for="name"
              label-align-sm="left"
              description="Ex: Rain Forest Alliance"
            >
              <b-form-input
                id="name"
                v-model="form.name"
                placeholder="Name"
                required
              ></b-form-input>
            </b-form-group>
            <br />

            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Description of the Certification"
              label-for="description"
              label-align-sm="left"
              id="desc"
            >
              <b-form-textarea
                id="description"
                v-model="form.description"
                placeholder="Please describe what this certificate is all about..."
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </b-form-group>
            <b-tooltip target="desc__BV_label_" triggers="hover" variant="secondary" placement="lefttop">
              Please describe your certificate in around 500 words approx.
            </b-tooltip>

            <br />
            <!--
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Please upload the certificate logo"
              label-for="description"
              label-align-sm="left"
            >
              <input type="file" />
              <input
                type="file"
                id="file"
                ref="file"
                v-on:change="onFileChange()"
              /><b-button v-on:click="submitFile()">Upload!</b-button>
            </b-form-group>-->
            <br />
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Priority level:"
              label-for="priority"
              label-align-sm="left"
              id="prio"
            >
              <b-form-select
                id="priority"
                v-model="form.priority"
                :options="scale"
              ></b-form-select>
            </b-form-group>
            <b-tooltip target="prio__BV_label_" triggers="hover" variant="secondary" placement="lefttop">
              How important is it to attain this certificate for a given company?
            </b-tooltip>
            <br />
            <b-form-group
              id="input-group-4"
              v-slot="{ ariaDescribedby }"
              label="What is the level of engagement with the UN Sustainable Development Goals?"
              label-for="rating"
              label-align-sm="left"
            >
              <b-form-radio-group
                class="pt-2"
                v-model="form.sdgEngagement"
                :options="sdgEngagementOptions"
                id="rating"
                :aria-describedby="ariaDescribedby"
                stacked
              >
              </b-form-radio-group>
            </b-form-group>
            <b-form-group
              label-align-sm="left"
              description="As you selected other, please specify"
              v-if="form.sdgEngagement == '5'"
            >
              <b-form-input
                id="name"
                v-model="form.sdgEngagementOther"
                placeholder="Other"
                required
              ></b-form-input>
            </b-form-group>
            <br />
            <b-row class="buttons_row">
            <b-button type="reset" variant="danger">Reset</b-button>
            <b-button type="submit" variant="primary">Proceed to SDGs</b-button>
            </b-row>
          </b-form>
        </b-col>
        <b-col></b-col>
      </b-row>
      <!--<b-card class="mt-3" header="Form result so far">
      <pre class="m-0">{{ form }}</pre>

    </b-card>-->
    </b-container>
  </div>
</template>

<script>
import CertificateFormMixin from "@/mixins/CertificateFormMixin";
import FormGuardMixin from "@/mixins/FormGuardMixin";
import ProgressBar from "../Shared/ProgressBar.vue";

export default {
  data() {
    return {
      file: "",
      sdgEngagementOptions: [
        {
          value: 1,
          text:
            "We have analyzed and identified specific Sustainable Development Goals and their underlying targets that are most relevant to our business",
        },
        {
          value: 2,
          text:
            "We have aligned our ongoing sustainability reporting metrics to the SDGs",
        },
        {
          value: 3,
          text:
            "We have set specific improvement goals to help achieve the SDGs (including goals set in the SDG Action Manager)",
        },
        {
          value: 4,
          text:
            "We have conducted internal training across our organization to educate our employees about the SDGs and our strategy to contribute to them",
        },
        {
          value: 5,
          text: "Other",
        },
      ],
      sdgEngagementOther: null,
    };
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();
      //alert(JSON.stringify(this.form));
      if (this.form.sdgEngagement == "5") {
        this.form.sdgEngagement = this.sdgEngagementOther;
      }
      if (this.form.rating == "P3") {
        this.form.rating = this.ratingOther;
      }

      await this.$store.dispatch("changeCertificate", this.form);
      this.permitNavigation = true;
      this.$router.push({ name: "formPage2-1" });
    },
    onReset() {
      this.$store.dispatch("resetCertificate");
      this.$store.dispatch("resetComputed");
    },
    onFileChange() {
      this.file = this.$refs.file.files[0];
      if (this.file) {
        this.$store
          .dispatch("upload/fetchSignatureAndPolicy", {
            name: this.file.name,
            type: this.file.type,
          })
          .then(() => {
            let policy = this.$store.state.uploadPolicy;
            var formData = new FormData();
            formData.append("key", policy.key);
            formData.append("acl", policy.acl);
            formData.append("Content-Type", this.file.type);
            formData.append(
              "success_action_status",
              policy.success_action_status
            );
            formData.append("policy", policy.policy);
            formData.append("x-amz-credential", policy["x-amz-credential"]);
            formData.append("x-amz-algorithm", policy["x-amz-algorithm"]);
            formData.append("x-amz-date", policy["x-amz-date"]);
            formData.append(
              "x-amz-security-token",
              policy["x-amz-security-token"]
            );
            formData.append("x-amz-signature", policy["x-amz-signature"]);
            formData.append("file", this.file);
            this.$store.dispatch("upload/upload", formData).then(() => {});
          });
      }
    },
  },
  mixins: [CertificateFormMixin, FormGuardMixin],
  components: { ProgressBar },
};
</script>

<style scoped>

#rating {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
}

#rating {
  margin-bottom: 10px !important;
}
</style>