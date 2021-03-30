<template>
  <mdb-container class="mt-5">
    <mdb-container>
      <mdb-row class="mdb-lightbox">
        <mdb-col
          v-for="(index, img) in imgs"
          :key="index"
          md="4"
          @click.native="showLightbox2(img)"
          style="text-align:center; "
        >
          <figure>
            <img :src=index class="img-fluid listimg" alt="">
          </figure>
        </mdb-col>
      </mdb-row>
    </mdb-container>
    <div
      class="lightbox"
      :class="{ active: visible2, nonactive: !visible2 }"
      @click="handleHide2()">
      <lightbox
        :source="resultdata2[index2]['source']"
        :color="resultdata2[index2]['colorarray']"
        :colored="resultdata2[index2]['colored']"
        :inform="resultdata2[index2]['contents']"
      ></lightbox>
    </div>
  </mdb-container>
</template>

<script>
import {
  mdbContainer, mdbRow, mdbCol,
} from 'mdbvue';
import axios from 'axios';
import lightbox from './lightbox.vue';

export default {
  name: 'GalleryPage',
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    lightbox,
  },
  data() {
    return {
      visible2: false,
      index2: 0,
      resultdata: [],
      resultdata2: [],
      imgs: [],
    };
  },
  methods: {
    showLightbox2(index2) {
      this.index2 = index2;
      this.visible2 = true;
    },
    handleHide2() {
      this.visible2 = false;
    },
    makeUp() {
      const data = this.resultdata;
      for (let idx = 0; idx < data.length; idx += 1) {
        let colorcode = `${data[idx].colorcode1}${data[idx].colorcode2}${data[idx].colorcode3}`; // 배열
        colorcode = colorcode.split('#');
        colorcode.splice(0, 1);
        const colorarray = [];
        if (colorcode.length < 4) {
          console.log('4');
          colorarray.push(colorcode.slice(0, colorcode.length));
        } else if (colorcode.length < 7) {
          console.log('7');
          colorarray.push(colorcode.slice(0, 3));
          colorarray.push(colorcode.slice(3, colorcode.length));
        } else if (colorcode.length < 10) {
          console.log('10');
          colorarray.push(colorcode.slice(0, 3));
          colorarray.push(colorcode.slice(3, 6));
          colorarray.push(colorcode.slice(6, colorcode.length));
        }
        console.log(colorarray);
        const colored = data[idx].colored.split('#'); // 배열
        colored.splice(0, 1);
        const contents = data[idx].contents.split(','); // 배열
        const source = `https://i.imgur.com/${data[idx].filename}`;
        this.resultdata2.push({
          colorarray,
          colored,
          contents,
          source,
        });
        this.imgs.push(source);
      }
      console.log('make up finish');
    },
  },
  created() {
    // get DB results table DATA
    const path = 'http://localhost:5000/addDB';
    axios.get(path)
      .then((res) => {
        for (let idx = 0; idx < res.data.result.length; idx += 1) {
          this.resultdata.push(res.data.result[idx]);
          console.log(this.resultdata);
        }
        this.makeUp();
      })
      .catch((error) => {
        console.error(error);
      });
  },
  destroyed() {
    // 초기화
    this.resultdata = [];
  },
};

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @media (min-width: 768px) {
    .carousel-multi-item-2 .col-md-3 {
      float: left;
      width: 25%;
      max-width: 100%; } }

    .carousel-multi-item-2 .card img {
      border-radius: 2px; }

    figure {
      cursor: pointer;
    }
  .lightbox {
    /** Position and style */
    position: fixed;
    z-index: 999;
    width: 80%;
    height: 80%;
    top: 10%;
    bottom: 10%;
    left: 10%;
    right: 10%;
    background: rgb(255, 255, 255);
    border-radius: 10px;
    border: solid 1px black;
  }
  .container {
    max-width: 1200px;
  }
  .active {
    display: block;
  }
  .nonactive {
    display: none;
  }
  .listimg {
    max-width: 100%;
    max-height: 350px;
    box-shadow: 3px 3px 3px rgb(167, 167, 167);
  }
</style>
