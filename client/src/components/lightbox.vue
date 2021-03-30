<template>
  <div class="overlay">
    <v-row class="borderdash">
      <v-col class="borderdash" style="margin: 10px">
        <v-img class="inimg"
          :src = source></v-img>
      </v-col>
      <v-col class="borderdash informcontents" style="margin: 10px">
        <v-row class="borderdash">
          <span>(이미지)</span><a :href=source>{{source}}</a>
        </v-row><br>
        <v-row class="borderdash">
          <div><h2 class="font-weight-bold">색상 코드</h2>
            <div class="borderdash text-center">
              <v-row
                class="borderdash"
                v-for="carray in color"
                :key="carray"
                align="center"
              >
                <v-col
                  class="borderdash"
                  align="center"
                  v-for="cdata in carray"
                  :key="cdata"
                >
                  <v-card
                    class="borderdash"
                    :style="{'background-color': '#' + cdata}"
                    style="height:65px;width:65px"
                  >
                    #{{cdata}}
                  </v-card>
                </v-col>
              </v-row>
            </div>
          </div>
        </v-row>
        <v-row class="borderdash">
          <div><h2 class="font-weight-bold">배색 코드</h2>
            <div class="borderdash text-center">
              <v-row
                class="borderdash"
                align="center"
              >
                <v-col
                  class="borderdash"
                  align="center"
                  v-for="idc in 3"
                  :key="idc"
                >
                  <v-card
                    class="borderdash"
                    :style="{'background-color': '#' + colored[(idc) -1]}"
                    style="height:65px;width:65px"
                  >
                    #{{colored[(idc) -1]}}
                  </v-card>
                </v-col>
              </v-row>
            </div>
          </div>
        </v-row>
        <v-row class="borderdash">
          <h2 class="font-weight-bold">색채 대비</h2>
          <v-row
            class="pa-md-4 mx-lg-auto"
            v-for= "(value, idm) in inform"
            :key="idm"
          >
            {{value.length != 1 ?
            colorInformation[value] : contrastInformation[value]}}
          </v-row>
          <br>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>
<script>
export default {
  name: 'lightbox',
  props: {
    source: String,
    color: Array,
    colored: Array,
    inform: Array,
  },
  data() {
    return {
      // 색상 정보
      colorInformation: {
        red: `빨간색 계열은 심리적으로 정열, 흥분, 적극성을 향상 시킬 수 있고,
        주의를 끌거나 강조하고 싶을 때 많이 사용합니다. 하지만 너무 많이 사용하면 피로를 느끼고 산만할 수 있습니다. 그리고 생명력을 상징합니다.`,
        green: `초록색 계열은 심리적으로 긴장을 풀어주고 진정을 도와줍니다.
         눈에 편안한 색으로 병원 등에서 많이 사용하고 자연과 식물, 환경 및 성장, 번영을 상징합니다.`,
        blue: `파란색 계열은 통계적으로 사람들이 가장 선호하는 색이고, 심리적으로 상쾌함,
         차분함, 시원함, 이지적인 느낌을 주지만 반대로 차가운 느낌으로 지루하고 우울하게 느껴지기도 합니다. 미래적이고 신뢰감있으며 성장 이미지가 있어 기업의 CI에 자주 사용됩니다.`,
        magenta: `자홍색 계열은 빨강의 강인함과 파랑의 불안함을 동시에 내포하는 신비로운 색이며 고귀함과 권력을 상징합니다.
        심리적으로 정서불안, 우울함, 질투 등을 느낄 수 있고, 기분을 고조시키기도 하고 마음의 평온을 찾아주기도 합니다.`,
        cyan: '청록색 계열은 인간의 이성과 본성을 의사소통할 수 있게 하여 사람의 감정을 치유하고 통제할 수 있습니다.',
        yellow: `노란색 계열은 흰색 다음으로 밝은 색으로 아동과 봄을 상징합니다.
        심리적으로 생동감과 명랑함을 느끼게 하고 주위 색과 차이가 뚜렷하여 가장 눈에 쉽게 띄는 색입니다. 많이 사용하면 금방 질릴 수 있습니다.
        밝은 색조의 파스텔 색과 함께 환하고 캐주얼한 공간을 연출할 때 적당합니다.`,
        grey: '회색은 무채색으로 명도로 조절합니다. 주황색과 잘 어울립니다.',
      },
      // 색채대비별 정보
      contrastInformation: {
        1: '1차색인 빨강, 노랑, 파랑의 색상대비가 있습니다.',
        2: '2차색인 주황, 초록, 보라의 색상대비가 있습니다.',
        3: 'Red와 Cyan의 보색대비가 있습니다. 서로의 색을 방해하지 않고 가장 순수하고 생기 있게 느끼게 하는 효과가 있습니다.',
        4: 'Green과 Magenta의 보색대비가 있습니다. 서로의 색을 방해하지 않고 가장 순수하고 생기 있게 느끼게 하는 효과가 있습니다.',
        5: 'Blue와 Yellow의 보색대비가 있습니다. 서로의 색을 방해하지 않고 가장 순수하고 생기 있게 느끼게 하는 효과가 있습니다.',
        6: 'Red계열과 Yellow계열은 난색으로 따듯한 느낌을 갖고 있습니다.',
        7: 'Blue계열과 Cyan계열은 한색으로 시원한 느낌을 갖고 있습니다.',
        8: 'Green계열과 Magenta계열은 중성색입니다.',
      },
    };
  },
  destroyed() {
    // 초기화
    this.source = '';
    this.color = [];
    this.colored = [];
    this.inform = [];
    this.twoColor = [];
  },
};
</script>
<style scope>
.borderdash {
  /*border: solid 1px rgba(50, 205, 50, 0.39);*/
}
.overlay {
  margin: 10px 10px 10px 10px;
  font-family: 'Nanum Gothic', sans-serif;
}
.informcontents {
  overflow:auto;
  width:80%;
  height:530px;
}
.inimg {
  display: block;
  margin: 0px auto;
  max-width: 500px;
  max-height: 500px;
}
</style>
