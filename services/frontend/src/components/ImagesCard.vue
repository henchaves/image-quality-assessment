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
      <div class="col-sm d-flex flex-column justify-content-center">
        <!-- align middle -->
        <button class="btn btn-primary" @click="vote">Duplicated</button><br>
        <button class="btn btn-primary" @click="vote">Not duplicated</button>

      </div>
      <!-- <div class="images row">
      <Image :imageId="image1Id" :imageUrl="image1Url" />
      <Image :imageId="image2Id" :imageUrl="image2Url" />
    </div> -->
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
  }
}
</script>