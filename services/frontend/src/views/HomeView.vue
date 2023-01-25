<template>
  <div class="home">
    <NavBar />
    <ImagesCard v-if="images" :images="images" :score="score" />
  </div>
</template>

<script>

import ImagesCard from '@/components/ImagesCard.vue'
import NavBar from '@/components/NavBar.vue';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    ImagesCard,
    NavBar
  },
  created() {
    axios.get('http://localhost:5000/pair_images')
      .then((response) => {
        this.images = response.data.images;
        this.score = response.data.score;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  data() {
    return {
      images: [],
      score: 0
    }
  }
}
</script>
