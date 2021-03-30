<template>
  <div>
    <div class="tabs">
      <a @click="activetab1=true; activetab2=false;" :class="{active : activetab1}">전체 분석</a>
      <a @click="activetab2=true; activetab1=false" :class="{active : activetab2}">선택 분석</a>
    </div>
    <div class="content">
      <div class="tabcontent" v-if="activetab1 === true">
        <ImageColor></ImageColor>
      </div>
      <div class="tabcontent" v-if="activetab2 === true">
        <ImagePick></ImagePick>
      </div>
    </div>
  </div>
</template>

<script>

import ImageColor from '../components/imagecolor.vue';
import ImagePick from '../components/imagepick.vue';

export default {
  name: 'Color',
  components: {
    ImageColor,
    ImagePick,
  },
  data() {
    return {
      activetab1: true,
      activetab2: false,
    };
  },
};
</script>
<style>
/* RESET */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.container {
    max-width: 1520px;
    min-width: 500px;
    margin: 0 auto;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.9em;
}

/* Style the tabs */
.tabs {
  overflow: hidden;
  margin-left: 20px;
  margin-bottom: -2px;
}

.tabs ul {
    list-style-type: none;
    margin-left: 20px;
}

.tabs a{
    float: left;
    cursor: pointer;
    padding: 12px 24px;
    transition: background-color 0.2s;
    border: 1px solid #ccc;
    border-right: none;
    background-color: #ccc;
    border-radius: 10px 10px 0 0;
    font-weight: bold;
}

/* Change background color of tabs on hover */
.tabs a:hover {
}

/* Styling for active tab */
.tabs a.active {
    background-color: rgb(52, 51, 90);
    border-bottom: 2px solid rgb(45, 100, 97);
    color: whitesmoke;
    cursor: pointer;
}

/* Style the tab content */
.tabcontent {
    padding: 30px;
    border: 1px solid #ccc;
    border-radius: 10px;
  box-shadow: 3px 3px 6px #e1e1e1
}
</style>
