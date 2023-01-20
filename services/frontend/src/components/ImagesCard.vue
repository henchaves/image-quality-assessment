<template>
  <div class="card mb-4 container">

    <div class="row">
      <!-- create card to wrap everything-->

      <div class="col-sm">
        <Image :imageId="image1Id" :imageUrl="image1Url" />
      </div>
      <div class="col-sm">
        <Image :imageId="image2Id" :imageUrl="image2Url" />
      </div>

      <div v-if="!duplicateValidated" class="check-duplicate col-sm d-flex flex-column justify-content-center" hidden>
        <p>Are these two photos duplicates?</p>
        <button class="btn btn-success" @click="handleDuplicated">Yes</button><br>
        <button class="btn btn-danger" @click="handleNotDuplicated">No</button>
      </div>

      <div v-if="duplicateValidated && isDuplicate && !qualityValidated" class="check-quality col-sm d-flex flex-column justify-content-center">
        <p>Which photo has the best quality?</p>
        <button class="btn btn-primary" @click="vote(1)">First photo (ID: {{ image1Id }})</button><br>
        <button class="btn btn-primary" @click="vote(2)">Second photo (ID: {{ image2Id }})</button>
      </div>

      <div v-if="(duplicateValidated && !isDuplicate) || (duplicateValidated && qualityValidated)" class="feedback col-sm d-flex flex-column justify-content-center">
        <p>Thank you for your feedback!</p>
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
    image1Id: String,
    image1Url: String,
    image2Id: String,
    image2Url: String,
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