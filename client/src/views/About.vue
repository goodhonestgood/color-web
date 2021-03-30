<template>
  <div>
    <Gallery></Gallery>
    <br><br>
    <!--
    <div>
      <v-pagination
        v-model="page"
        :length="15"
        :total-visible="7"
        circle
      ></v-pagination>
    </div>
    -->
  </div>
</template>

<script>
import Gallery from '../components/gallery2.vue';

export default {
  name: 'About',
  components: {
    Gallery,
  },
  data() {
    return {
      page: 1,
    };
  },
};
</script>
<style>
</style>
