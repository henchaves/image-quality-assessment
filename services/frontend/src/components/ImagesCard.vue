<template>
  <div class="card mb-4 container">

    <div class="row">
      <!-- create card to wrap everything-->

      <div class="col-sm">
        <Image :imageId="images[0].image_id" :imageUrl="images[0].image_url" />
      </div>
      <div class="col-sm">
        <Image :imageId="images[1].image_id" :imageUrl="images[1].image_url" />
      </div>

      <div v-if="!duplicateValidated" class="check-duplicate col-sm d-flex flex-column justify-content-center" hidden>
        <p>Are these two photos duplicates?</p>
        <button class="btn btn-success" @click="handleDuplicated">Yes</button><br>
        <button class="btn btn-danger" @click="handleNotDuplicated">No</button>
      </div>

      <div v-if="duplicateValidated && isDuplicate && !qualityValidated" class="check-quality col-sm d-flex flex-column justify-content-center">
        <p>Which photo has the best quality?</p>
        <button class="btn btn-primary" @click="vote(1)">First photo (ID: {{ images[0].image_id }})</button><br>
        <button class="btn btn-primary" @click="vote(2)">Second photo (ID: {{ images[1].image_id }})</button>
      </div>

      <div v-if="(duplicateValidated && !isDuplicate) || (duplicateValidated && qualityValidated)" class="feedback col-sm d-flex flex-column justify-content-center">
        <h4>Thank you for your feedback!</h4>
        <div class="mb-4 mt-4">
          <b>Model results:</b>
          <p>Probability of duplicated: {{ score }}</p>
          <p>Quality of first photo: {{ images[0].mean_score_prediction.toFixed(2) }}</p>
          <p>Quality of second photo: {{ images[1].mean_score_prediction.toFixed(2) }}</p>
        </div>
        <button class="btn btn-primary" @click="handleNext">Next pair</button>
      </div>


    </div>
  </div>

</template>

<script>
import Image from './Image.vue';

export default {
  name: 'ImagesCard',
  components: {
    Image,
  },
  props: {
    images: {
      type: Array,
      required: true,
    },
    score: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      duplicateValidated: false,
      qualityValidated: false,
      isDuplicate: false,
    };
  },
  methods: {
    handleDuplicated() {
      this.duplicateValidated = true;
      this.isDuplicate = true;
    },
    handleNotDuplicated() {
      this.duplicateValidated = true;
      this.isDuplicate = false;
    },
    vote(imageId) {
      this.qualityValidated = true;
      console.log('vote', imageId);
    },
    handleNext() {
      this.$router.go();
    },

  },
}
</script>