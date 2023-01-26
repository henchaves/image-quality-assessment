<template>
  <div class="card mb-4 container">

    <div class="row">
      <!-- create card to wrap everything-->

      <div class="col-sm">
        <ImageCandidate :imageId="images[0].image_id" :imageUrl="images[0].image_url" />
      </div>
      <div class="col-sm">
        <ImageCandidate :imageId="images[1].image_id" :imageUrl="images[1].image_url" />
      </div>

      <div v-if="!duplicateValidated" class="check-duplicate col-sm d-flex flex-column justify-content-center" hidden>
        <p>Are these two photos duplicates?</p>
        <button class="btn btn-success" @click="handleDuplicated">Yes</button><br>
        <button class="btn btn-danger" @click="handleNotDuplicated">No</button>
      </div>

      <div v-if="duplicateValidated && isDuplicate && !qualityValidated" class="check-quality col-sm d-flex flex-column justify-content-center">
        <p>Which photo has the best quality?</p>
        <button class="btn btn-primary" @click="vote(0)">First photo (ID: {{ images[0].image_id }})</button><br>
        <button class="btn btn-primary" @click="vote(1)">Second photo (ID: {{ images[1].image_id }})</button>
      </div>

      <div v-if="(duplicateValidated && !isDuplicate) || (duplicateValidated && qualityValidated)" class="feedback col-sm d-flex flex-column justify-content-center">
        <h4>Thank you for your feedback!</h4>
        <div class="mb-4 mt-4">
          <h5>Model results:</h5>
          <p>Probability of duplicated: <b>{{ (score * 100).toFixed(2) }}%</b></p>
          <p>Quality of first photo (ID {{ images[0].image_id }}): <b>{{ images[0].mean_score_prediction.toFixed(2) }}</b></p>
          <p>Quality of second photo (ID {{ images[1].image_id }}): <b>{{ images[1].mean_score_prediction.toFixed(2) }}</b></p>
        </div>
        <button class="btn btn-primary" @click="handleNext">Next pair</button>
      </div>


    </div>
  </div>

</template>

<script>
import axios from 'axios';
import ImageCandidate from './ImageCandidate.vue';

export default {
  name: 'ImagesCard',
  components: {
    ImageCandidate,
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
      bestImage: null,
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

      axios.post('http://localhost:5000/human_result', {
        image_1: this.images[0].image_id,
        image_2: this.images[1].image_id,
        duplicated: this.isDuplicate,
        best_image: "",
        group_id: this.images[0].group_id
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    vote(imageId) {
      this.qualityValidated = true;
      this.bestImage = this.images[imageId];

      axios.post('http://localhost:5000/human_result', {
        image_1: this.images[0].image_id,
        image_2: this.images[1].image_id,
        duplicated: this.isDuplicate,
        best_image: this.bestImage.image_id,
        group_id: this.bestImage.group_id
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    handleNext() {
      this.$router.go();
    },

  },
}
</script>