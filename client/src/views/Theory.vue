<template>
  <div>
    <div class=""><h3 class="font-weight-bold">색채 이론</h3></div><br>
    <v-expansion-panels
      v-model="panel"
      :disabled="disabled"
      multiple
    >
      <v-expansion-panel>
        <v-expansion-panel-header
          color="pink darken -1" class="font-weight-bold">색상 계열</v-expansion-panel-header>
        <v-expansion-panel-content>
          <br>RGB와 CMY를 기본으로한 색상환을 사용하였습니다.<br>
          <v-img src="../assets/colors.png" width="300px" height="300px"></v-img>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header
          color="pink lighten-1" class="font-weight-bold">색상대비</v-expansion-panel-header>
        <v-expansion-panel-content>
          <br>두 가지 색을 동시에 볼 때 각 색상의 차이가 크게 느껴지는 현상을 말한다.<br>
          <ul>
            <li>1차색 : 빨강, 노랑, 파랑의 색상 대비, 화려함</li>
            <li>2차색 : 주황, 초록, 보라의 색상 대비, 차분함</li>
            <li>3차색 : 연두, 주황, 청자색의 색상 대비, 편안함</li>
          </ul>
          활용 : LEGO
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header
          color="pink lighten-2" class="font-weight-bold">보색대비</v-expansion-panel-header>
        <v-expansion-panel-content>
          <br>색상환에서 마주보는 위치의 색의 대비로 두 색이 혼합되면 검정이나 무채색으로 바뀐다.
          서로의 색을 방해하지 않고 가장 순수하고 생기 있게 느끼게 하는 효과가 있다.<br><br>
          활용 : 수술복
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header
          color="pink lighten-3" class="font-weight-bold">한난대비</v-expansion-panel-header>
        <v-expansion-panel-content>
          <br>색이 차고 따듯함에 따라 변화가 오는 현상으로 난색도 상대적으로 한난 대비가 있다.<br>
          <ul>
            <li>한색 : 더욱 차갑게 느껴진다.</li>
            <li>난색 : 더욱 따듯하게 느껴진다.</li>
            <li>중성색 : 중성색인 보라색과 녹색이 대비되면 보라색이 따듯하게 느껴지고, 중성색인 보라색과 난색인 빨간색이 대비되면 보라색이 차갑게 느껴진다.</li>
          </ul>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header
          color="pink lighten-4" class="font-weight-bold">면적대비</v-expansion-panel-header>
        <v-expansion-panel-content>
          <br>면적에 따라 채도가 다르게 보이는 효과가 있다.<br>
          <ul>
            <li>면적 大 : 채도가 높아 실제보다 밝고 맑게 보인다.</li>
            <li>면적 小 : 명도와 채도가 낮아져 실제보다 어둡고 탁하게 보인다.</li>
          </ul>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
export default {
  data() {
    return {
    
    };
  },
};
</script>
