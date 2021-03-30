<template>
    <div>
        <div>
          <v-row align="center" no-gutters>
            <v-col
              align="center"
              cols="4"
            >
              <v-card
                class="text-center colorHeader"
                :style="{backgroundColor: color}"
                style="border-radius:50%">
                <br><strong>{{color}}</strong><br>계열은
              </v-card>
            </v-col>
            <v-col cols="8">
              <p>{{colorInformation[color]['desc']}}</p>
            </v-col>
          </v-row>
          <!--
          <v-row align="center">
            <v-col align="center">
              <v-slide-group
                v-model="model"
                class="pa-4"
                :prev-icon="prevIcon ? 'mdi-minus' : undefined"
                :next-icon="nextIcon ? 'mdi-plus' : undefined"
                :multiple="multiple"
                :mandatory="mandatory"
                :show-arrows="showArrows"
                :center-active="centerActive"
              >
                <v-slide-item
                  v-for="n in colorInformation[color]['imgs'].length"
                  :key="n"
                  v-slot:default="{ active, toggle }"
                >
                  <v-card
                    :color="active ? color : 'white'"
                    class="ma-4"
                    height="200"
                    width="200"
                    @click="toggle"
                  >
                    <v-img class="fill-height" :src="colorInformation[color]['imgs'][n-1]" v-if="!active"/>
                    <v-row
                      v-if="active"
                      align="center"
                      justify="center"
                    >
                      <v-col class="text-center">
                        <h3 color="white">{{}}</h3>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-slide-item>
              </v-slide-group>
            </v-col>
          </v-row>
          -->
        </div>
    </div>
</template>
<script>
export default {
  props: ['color'],
  data() {
    return {
      model: null,
      multiple: false,
      mandatory: false,
      showArrows: true,
      prevIcon: false,
      nextIcon: false,
      centerActive: true,
      // 색상 정보
      colorInformation: {
        red: {
          desc: `빨간색 계열은 심리적으로 정열, 흥분, 적극성을 향상 시킬 수 있고, 
          주의를 끌거나 강조하고 싶을 때 많이 사용합니다. 하지만 너무 많이 사용하면 피로를 느끼고 산만할 수 있습니다. 그리고 생명력을 상징합니다.`,
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        green: {
          desc: `초록색 계열은 심리적으로 긴장을 풀어주고 진정을 도와줍니다.
        눈에 편안한 색으로 병원 등에서 많이 사용하고 자연과 식물, 환경 및 성장, 번영을 상징합니다.`,
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        blue: {
          desc: `파란색 계열은 통계적으로 사람들이 가장 선호하는 색이고, 심리적으로 상쾌함,
        차분함, 시원함, 이지적인 느낌을 주지만 반대로 차가운 느낌으로 지루하고 우울하게 느껴지기도 합니다. 미래적이고 신뢰감있으며 성장 이미지가 있어 기업의 CI에 자주 사용됩니다.`,
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        magenta: {
          desc: `자홍색 계열은 빨강의 강인함과 파랑의 불안함을 동시에 내포하는 신비로운 색이며 고귀함과 권력을 상징합니다.
        심리적으로 정서불안, 우울함, 질투 등을 느낄 수 있고, 기분을 고조시키기도 하고 마음의 평온을 찾아주기도 합니다.`,
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        cyan: {
          desc: '청록색 계열은 인간의 이성과 본성을 의사소통할 수 있게 하여 사람의 감정을 치유하고 통제할 수 있습니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        yellow: {
          desc: `흰색 다음으로 밝은 색으로 아동과 봄을 상징합니다.
        심리적으로 생동감과 명랑함을 느끼게 하고 주위 색과 차이가 뚜렷하여 가장 눈에 쉽게 띄는 색입니다. 많이 사용하면 금방 질릴 수 있습니다.
        밝은 색조의 파스텔 색과 함께 환하고 캐주얼한 공간을 연출할 때 적당합니다.`,
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        grey: {
          desc: '회색은 무채색으로 명도로 조절합니다. 주황색과 잘 어울립니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        'first': {
          desc: '1차색인 빨강, 노랑, 파랑의 색상대비가 있습니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        'red-cyan': {
          desc: 'Red와 Cyan의 보색대비가 있습니다. 서로의 색을 방해하지 않고 가장 순수하고 생기 있게 느끼게 하는 효과가 있습니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        'green-magenta': {
          desc: 'Green과 Magenta의 보색대비가 있습니다. 서로의 색을 방해하지 않고 가장 순수하고 생기 있게 느끼게 하는 효과가 있습니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        'blue-yellow': {
          desc: 'Blue와 Yellow의 보색대비가 있습니다. 서로의 색을 방해하지 않고 가장 순수하고 생기 있게 느끼게 하는 효과가 있습니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        'warm': {
          desc: 'Red계열과 Yellow계열은 난색으로 따듯한 느낌을 갖고 있습니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        'cool': {
          desc: 'Blue계열과 Cyan계열은 한색으로 시원한 느낌을 갖고 있습니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
        'gm-neut': {
          desc: 'Green계열과 Magenta계열은 중성색입니다.',
          imgs: [require('@/assets/i.png'),require('@/assets/spring.png'),require('@/assets/eyes.png'),require('@/assets/pastel.jpg')],
        },
      },
    };
  },
};
</script>
<style scoped>
  .colorHeader {
    font-size: 25px;
    text-transform: capitalize;
    height: 150px;
    width: 150px;
    background-color: bisque;
  }
</style>
