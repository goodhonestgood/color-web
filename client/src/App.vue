<template>
  <v-app>
    <v-app-bar
      app
      color="black"
      dark
      dense
      hide-on-scroll
    >
      <div class="d-flex align-center">
        <v-img
          alt="Logo"
          class="shrink mr-2"
          contain
          src="./assets/rainbow.png"
          transition="scale-transition"
          width="40"
        />
      </div>

      <v-tabs align-with-title slider-color="purple lighten-3">
        <v-tab route :to="{name:'Home'}">Home</v-tab>
        <v-tab route :to="{name:'Color'}">Color</v-tab>
        <v-tab route :to="{name:'Theory'}">Theory</v-tab>
        <v-tab route :to="{name:'About'}">About</v-tab>
      </v-tabs>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <v-container
        class="fill-width"
        fluid
      >
        <router-view></router-view>
      </v-container>
    </v-content>
    <v-footer
      color="black"
      app
      dark
    >
      <span class="white--text">&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {

  },

  data: () => ({

  }),
  methods: {
  },
};
</script>
<style>
@import url(http://fonts.googleapis.com/earlyaccess/nanumgothic.css);
*{
  font-family: 'Nanum Gothic', sans-serif;
}
</style>
