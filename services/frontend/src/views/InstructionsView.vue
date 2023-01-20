<template>
  <div class="instructions">
    <NavBar />

    <div class="container">
      <h1>Instructions</h1>
      <p>1. Click on the button "Yes" if the two images are duplicates, "No" if they are not.</p>
      <p>2. Click on the button "First photo" or "Second photo" to choose which photo has the best quality.</p>
      <p>3. Click on the button "Next" to go to the next images.</p>

      <h3 :style="styles"> Remarks: </h3>
      <p :style="styles"> Two images are considered the same if they want to represent the same thing. Cropped images or images with slighlty different angles can be considered the same. The image with best quality is the image where you can see more information, or the most steady image. </p>

      <button class="btn btn-primary" @click="handleStart">Start</button>
    </div>

  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';

const styles = {
  color: 'red',
};

export default {
  name: 'InstructionsView',
  components: {
    NavBar
  },
  methods: {
    handleStart() {
      this.$router.push('/');
    },
  },
  data() {
    return {
      styles,
    };
  },
}
</script>