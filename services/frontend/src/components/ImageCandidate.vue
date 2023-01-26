<template>
  <div class="card mb-4 box-shadow">
    <img class="card-img-top" :src="imageUrl" :data-id="imageId">
    <div class="card-body">
      <p class="card-text">Image ID: {{ imageId }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ImageCandidate',
  props: {
    imageId: String,
    imageUrl: String,
  }
}
</script>
