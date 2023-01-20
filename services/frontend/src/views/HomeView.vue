<template>
  <div class="home">
    <NavBar />
    <ImagesCard v-if="images" :image1Id="images[0].image_id" :image1Url="images[0].image_url" :image2Id="images[1].image_id" :image2Url="images[1].image_url" />


  </div>
</template>

<script>
// @ is an alias to /src

import ImagesCard from '@/components/ImagesCard.vue'
import NavBar from '@/components/NavBar.vue';
import axios from 'axios';

// const images = [
//   {
//     id: '1',
//     url: 'https://i.travelapi.com/hotels/57000000/56980000/56971500/56971471/e97b6e21_z.jpg'
//   },
//   {
//     id: '2',
//     url: 'https://i.travelapi.com/hotels/57000000/56980000/56971500/56971471/36de3432_z.jpg'
//   }
// ]

export default {
  name: 'HomeView',
  components: {
    ImagesCard,
    NavBar
  },
  created() {
    axios.get('http://localhost:5000/pair_images')
      .then((response) => {
        this.images = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  data() {
    return {
      images: []
    }
  }
}
</script>
