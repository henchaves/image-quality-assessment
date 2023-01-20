<template>
  <div class="home">
    <NavBar />
    <ImagesCard :image1Id="images[0].id" :image1Url="images[0].url" :image2Id="images[1].id" :image2Url="images[1].url" />


  </div>
</template>

<script>
// @ is an alias to /src

import ImagesCard from '@/components/ImagesCard.vue'
import NavBar from '@/components/NavBar.vue';

const images = [
  {
    id: '1',
    url: 'https://i.travelapi.com/hotels/57000000/56980000/56971500/56971471/e97b6e21_z.jpg'
  },
  {
    id: '2',
    url: 'https://i.travelapi.com/hotels/57000000/56980000/56971500/56971471/36de3432_z.jpg'
  }
]

export default {
  name: 'HomeView',
  components: {
    ImagesCard,
    NavBar
  },
  data() {
    return {
      images: images
    }
  }
}
</script>
