<template>
  <div class="home">
    <v-img src="../assets/bg-5.png" style="margin-top: -50px;">
      <v-row align="end" class="lightbox black--text pa-2 fill-height">
        <v-col align="center">
          <v-btn outlined flat large color='black' href="/color">
            <div class="headline">이미지 분석 GO!<br></div>
          </v-btn>
        </v-col>
      </v-row>
    </v-img>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  components: {
  },
};
</script>
<style>
.borderdash {
  /*border: dashed gray;*/
}
.marginBottom {
  margin-bottom: 8px;
  margin-left: auto;
  margin-right: auto;
  width:50%
}
</style>
