<template>
    <div class="centered">
      <div
        class="text-center borderdash"
        style="margin-bottom:30px;width:100%;">
        <h2 class="font-weight-bold">색을 선택하여 분석하기</h2>
      </div>
      <div class="marginBottom borderdash" style="width:60%;">
        <input
        type="file" name="file" id="file" ref="file"
        @change="change();"
        style="width:100%;">
      </div>
      <div class="marginBottom borderdash" style="width:50%;">
        <div class="previewimage">
          <img id="my-image" class="clickevent" :src="source" alt="Image"/>
        </div>
      </div>
      <hr>
      <div class="marginBottom borderdash text-center" style="width:320px;">
        <v-row
          class="borderdash"
          align="center"
        >
          <v-col
            class="borderdash"
            align="center"
            v-for="color in datalist"
            :key="color"
          >
            <v-card
              class="borderdash"
              :style="{'background-color': `rgba(${color.join(',')})`}"
              style="height:65px;width:65px"
            >
            </v-card>
          </v-col>
        </v-row>
      </div>
      <hr v-if="filename.length > 0">
      <div class="marginBottom borderdash text-center"
        style="width:35%;" v-if="datalist.length === 3">
        <v-btn type="button" outlined color="blue" @click="pickSubmit">제출</v-btn>
      </div>
      <br>
      <div
        class="resultButton marginBottom borderdash text-center"
        style="width:30%; display:none;">
        <v-btn
          @click="
            informbutton = (informbutton === '결과 보기') ? '-' : '결과 보기';
            informdisplay = (informdisplay === 'none') ? 'block' : 'none';
          "
          outlined color="orange"
        >
        {{informbutton}}
        </v-btn>
      </div>
      <hr>
      <div class="inform marginBottom borderdash text-center"
        v-if="informdisplay === 'block'"
        style="width: 80%">
        <h4>Color Analysis Information</h4>
        <div class="firstinform">
          이미지 분석 결과,<br>
          <span v-for="(key,value) in deSeries" :key="value">
          {{key}}<span v-if="value != deSeries.length-1">, </span></span>
          계열의 색상이 사용되었습니다.<br><br>
        </div>
        <div class="marginBottom" style="width:80%">
          <v-row align="center">
            <v-col
              align="center"
              v-for="(co,i) in color"
              :key= "i"
            >
              <v-card
                :style="{'background-color': co,
                  'color': sb[i][1] < 38 ? 'white' : 'black'}"
                style="width: 80px; height: 80px;"
              >
                {{co}}<br>
                {{colorSeries[i]}}<br>
                {{sb[i][0]}}% / {{sb[i][1]}}%
              </v-card>
            </v-col>
          </v-row>
        </div><br>
        <div class="secinform text-left">
          <div>
            <p>배색은 어떤 특별한 목적과 기능에 합치된 미적 효과를 얻기 위하여 두 가지 이상의 색이 조화를 이루도록 만드는 것이고
            다양한 배색을 기초로 하여 삼원색처럼 규정한 뒤 색을 섞거나 명암을 조절하여 배색의 조화를 이끌어냅니다.</p>
            <p>위 3가지색을 혼합하여 나온색들을 이미지에 추가하면 더욱 효과적입니다.</p>
            ※합리적인 배색을 위해 고려해야 할 것은 ?
            <ul>
              <li>형태나 위치</li>
              <li>면적과 재료</li>
              <li>조명의 연색성 (빛)</li>
              <li>개인의 기호나 심리상태</li>
              <li>많은 조건과 복잡하게 관련되어 반응이 나타나므로 배색의 결과가 항상 성공적일 수 없음</li>
              <li>배색을 통해 색깔을 정해놓으면 시간이 지나면서 많은 사람들에게 익숙한 색깔로 작용함</li>
            </ul>
          </div>
          <div class="marginBottom" style="width:70%;">
            <v-row class="borderdash" align="center">
              <v-col v-for="coloredvalue in colored"
                :key="coloredvalue"
                class="borderdash"
                align="center"
              >
                <v-card class="text-center"
                  :style="{'background-color': coloredvalue}"
                  style="width: 75px; height: 75px; border-radius: 50%">
                  <br>{{coloredvalue}}<br><br>
                </v-card>
              </v-col>
            </v-row>
          </div><br>
          <div>이 이미지에서는 이러한 대비가 일어납니다.</div><hr>
          <div class="informborder"
            v-for="informvalue in aInform"
            :key="informvalue"
          >
            {{typeof informvalue == 'string' ?
              colorInformation[informvalue] : contrastInformation[informvalue]}}
            <hr>
          </div>
        </div>
        <div>
          <v-btn
            @click="toDB()"
            outlined color="pink"
          >
            저장
          </v-btn>
        </div>
      </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      source: '',
      filename: '',
      datalist: [],
      color: [],
      number: 0,
      colorSeries: [],
      sb: [],
      deSeries: [],
      aInform: [],
      colored: [],
      informbutton: '결과 보기',
      informdisplay: 'none',
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
  methods: {
    toDB() {
      const path2 = 'http://localhost:5000/addFile';
      const file = this.$refs.file.files[0];
      const formData = new FormData();
      formData.append('file', file);
      console.log(file);
      axios.post(path2, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }).then((res) => {
        console.log(res.data.filename);
        const names = res.data.filename;
        let joinstr1 = '';
        let joinstr4 = '';
        for (let idx = 0; idx < this.color.length; idx += 1) {
          joinstr1 += this.color[idx];
        }
        for (let idx = 0; idx < this.colored.length; idx += 1) {
          joinstr4 += this.colored[idx];
        }
        const carray = this.aInform;
        console.log(carray);
        const content = carray.toString();
        console.log(content);
        const payload = {
          color1: joinstr1,
          color2: '',
          color3: '',
          colored: joinstr4,
          filename: names,
          contents: content,
        };
        const path = 'http://localhost:5000/addDB';
        axios.post(path, payload)
          .then(() => {
            console.log('success');
          })
          .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          });
      });
    },
    pReset() {
      this.source = '';
      this.filename = '';
      this.color = [];
      this.colorSeries = [];
      this.sb = [];
      this.deSeries = [];
      this.aInform = [];
      this.colored = [];
      this.informbutton = '결과 보기';
      this.informdisplay = 'none';
      this.datalist = [];
      this.number = 0;
      document.querySelector('.clickevent').addEventListener('mousedown', this.mouseIsMoving);
    },
    change() {
      this.pReset();
      console.log('change');
      const image = this.$refs.file.files[0];
      this.source = URL.createObjectURL(image);
      const name = document.getElementById('file').value;
      this.filename = name;
    },
    mouseIsMoving(e) {
      const x = e.offsetX;
      const y = e.offsetY;
      console.log(x, y);
      const img = document.getElementById('my-image');
      const canvas = document.createElement('canvas');
      canvas.width = img.width;
      canvas.height = img.height;
      canvas.getContext('2d').drawImage(img, 0, 0, img.width, img.height);
      const pixeldata = canvas.getContext('2d').getImageData(x, y, 1, 1).data;
      console.log(pixeldata);
      this.datalist.push(pixeldata);
      this.number += 1;
      if (this.number !== 0) {
        if (this.number % 3 === 0) {
          document.querySelector('.clickevent').removeEventListener('mousedown', this.mouseIsMoving);
        }
      }
    },
    pickSubmit() {
      for (let i = 0; i < 3; i += 1) {
        this.whatColor(this.datalist[i][0], this.datalist[i][1], this.datalist[i][2]);
      }
      for (let j = 0; j < 3; j += 1) {
        console.log(j);
        this.color.push(this.toHex([
          this.datalist[j][0],
          this.datalist[j][1],
          this.datalist[j][2]]));
      }
      this.pcoloration();
      document.getElementsByClassName('resultButton')[0].style.display = 'block';
      console.log('pickSubmit');
    },
    // 색상계열 얻기
    whatColor(r, g, b) {
      // 순색 얻기
      const pureColor = this.what(r, g, b);
      const red = pureColor[0];
      const green = pureColor[1];
      const blue = pureColor[2];

      if (red === 255) {
        if (green === 0) {
          // (255, 0, b)
          if (blue >= 0 && blue <= 127) {
            this.colorSeries.push('red');
          } else if (blue >= 128 && blue <= 255) {
            this.colorSeries.push('magenta');
          }
        } else if (blue === 0) {
          // (255, g, 0)
          if (green >= 0 && green <= 127) {
            this.colorSeries.push('red');
          } else if (green >= 128 && green <= 255) {
            this.colorSeries.push('yellow');
          }
        }
      } else if (green === 255) {
        if (red === 0) {
          // (0, 255, b)
          if (blue >= 0 && blue <= 127) {
            this.colorSeries.push('green');
          } else if (blue >= 128 && blue <= 255) {
            this.colorSeries.push('cyan');
          }
        } else if (blue === 0) {
          // (r, 255, 0)
          if (red >= 0 && red <= 127) {
            this.colorSeries.push('green');
          } else if (red >= 128 && red <= 255) {
            this.colorSeries.push('yellow');
          }
        }
      } else if (blue === 255) {
        if (red === 0) {
          // (0, g, 255)
          if (green >= 0 && green <= 127) {
            this.colorSeries.push('blue');
          } else if (green >= 128 && green <= 255) {
            this.colorSeries.push('cyan');
          }
        } else if (green === 0) {
          // (r, 0, 255)
          if (red >= 0 && red <= 127) {
            this.colorSeries.push('blue');
          } else if (red >= 128 && red <= 255) {
            this.colorSeries.push('magenta');
          }
        }
      } else if (red === blue && blue === green) {
        this.colorSeries.push('grey');
      }
      // colorSeries 중복 제거
      this.deDuplicate();
    },
    // 순색 얻기
    what(r, g, b) {
      let red = 0;
      let green = 0;
      let blue = 0;
      const max = Math.max(r, g, b);
      const min = Math.min(r, g, b);
      if (r === g && g === b) {
        this.sb.push([0, Math.round((r / 255) * 100)]);
        red = r;
        green = g;
        blue = b;
      } else if (r !== 255 && g !== 255 && b !== 255) { // R, G, B 모두 255가 아닐 때
        if (r === max) {
          if (g === min) {
            green = (g * 255) / r;
            blue = (b * 255) / r;
            blue = ((blue - green) * 255) / (255 - green);
            red = 255;
            green = 0;
            this.sb.push([Math.round((1 - (g / r)) * 100), Math.round((r / 255) * 100)]);
          } else if (b === min) {
            blue = (b * 255) / r;
            green = (g * 255) / r;
            green = ((green - blue) * 255) / (255 - blue);
            red = 255;
            blue = 0;
            this.sb.push([Math.round((1 - (b / r)) * 100), Math.round((r / 255) * 100)]);
          }
        } else if (g === max) {
          if (r === min) {
            red = (r * 255) / g;
            blue = (b * 255) / g;
            blue = ((blue - red) * 255) / (255 - red);
            green = 255;
            red = 0;
            this.sb.push([Math.round((1 - (r / g)) * 100), Math.round((g / 255) * 100)]);
          } else if (b === min) {
            blue = (b * 255) / g;
            red = (r * 255) / g;
            red = ((red - blue) * 255) / (255 - blue);
            green = 255;
            blue = 0;
            this.sb.push([Math.round((1 - (b / g)) * 100), Math.round((g / 255) * 100)]);
          }
        } else if (b === max) {
          if (r === min) {
            red = (r * 255) / b;
            green = (g * 255) / b;
            green = ((green - red) * 255) / (255 - red);
            blue = 255;
            red = 0;
            this.sb.push([Math.round((1 - (r / b)) * 100), Math.round((b / 255) * 100)]);
          } else if (g === min) {
            green = (g * 255) / b;
            red = (r * 255) / b;
            red = ((red - green) * 255) / (255 - green);
            blue = 255;
            green = 0;
            this.sb.push([Math.round((1 - (g / b)) * 100), Math.round((b / 255) * 100)]);
          }
        }
      } else if (r === 255) { // R이 255일 때
        if (g === 255) {
          red = 255;
          green = 255;
          blue = 0;
          this.sb.push([Math.round((1 - (b / 255)) * 100), 100]);
        } else if (b === 255) {
          red = 255;
          green = 0;
          blue = 255;
          this.sb.push([Math.round((1 - (g / 255)) * 100), 100]);
        } else if (g === min) {
          blue = ((b - g) * 255) / (255 - g);
          green = 0;
          red = 255;
          this.sb.push([Math.round((1 - (g / 255)) * 100), 100]);
        } else if (b === min) {
          green = ((g - b) * 255) / (255 - b);
          blue = 0;
          red = 255;
          this.sb.push([Math.round((1 - (b / 255)) * 100), 100]);
        }
      } else if (g === 255) { // G가 255일 때
        if (b === 255) {
          red = 0;
          green = 255;
          blue = 255;
          this.sb.push([Math.round((1 - (r / 255)) * 100), 100]);
        } else if (r === min) {
          blue = ((b - r) * 255) / (255 - r);
          red = 0;
          green = 255;
          this.sb.push([Math.round((1 - (r / 255)) * 100), 100]);
        } else if (b === min) {
          red = ((r - b) * 255) / (255 - b);
          blue = 0;
          green = 255;
          this.sb.push([Math.round((1 - (b / 255)) * 100), 100]);
        }
      } else if (b === 255) { // B가 255일 때
        if (r === min) {
          green = ((g - r) * 255) / (255 - r);
          red = 0;
          blue = 255;
          this.sb.push([Math.round((1 - (r / 255)) * 100), 100]);
        } else if (g === min) {
          red = ((r - g) * 255) / (255 - g);
          green = 0;
          blue = 255;
          this.sb.push([Math.round((1 - (g / 255)) * 100), 100]);
        }
      }
      return [red, green, blue];
    },
    // 중복 제거
    deDuplicate() {
      this.deSeries = Array.from(new Set(this.colorSeries));
      // 정보와 매칭하기
      this.matchInform();
    },
    matchInform() {
      const array = this.deSeries;
      const txt = [];

      // 색채 계열 정보
      array.forEach((element) => {
        txt.push(element);
      });
      // 색채 대비 정보
      if (array.includes('red')) {
        if (array.includes('cyan')) {
          txt.push(3);
        }
      }
      if (array.includes('green')) {
        if (array.includes('magenta')) {
          txt.push(4);
          txt.push(8);
        }
      }
      if (array.includes('blue')) {
        if (array.includes('yellow')) {
          txt.push(5);
        }
      }
      if (array.includes('red')) {
        if (array.includes('yellow')) {
          if (array.includes('blue')) {
            txt.push(1);
          }
        }
      }
      if (!array.includes('magenta') && !array.includes('blue')
        && !array.includes('green') && !array.includes('cyan')
        && array.includes('red') && array.includes('yellow')) {
        txt.push(6);
      }
      if (!array.includes('magenta') && array.includes('blue')
        && !array.includes('green') && array.includes('cyan')
        && !array.includes('red') && !array.includes('yellow')) {
        txt.push(7);
      }
      this.aInform = txt;
      console.log(this.aInform);
    },
    pcoloration() {
      const r = [];
      const g = [];
      const b = [];
      for (let j = 0; j < 3; j += 1) {
        r.push(this.datalist[j][0]);
        g.push(this.datalist[j][1]);
        b.push(this.datalist[j][2]);
      }
      this.colored.push(this.toHex([(Math.round((r[0] + r[1]) / 2)),
        (Math.round((g[0] + g[1]) / 2)), (Math.round((b[0] + b[1]) / 2))]));
      this.colored.push(this.toHex([(Math.round((r[0] + r[2]) / 2)),
        (Math.round((g[0] + g[2]) / 2)), (Math.round((b[0] + b[2]) / 2))]));
      this.colored.push(this.toHex([(Math.round((r[1] + r[2]) / 2)),
        (Math.round((g[1] + g[2]) / 2)), (Math.round((b[1] + b[2]) / 2))]));
    },
    // 10->16
    toHex(rgb) {
      const r = rgb[0];
      const g = rgb[1];
      const b = rgb[2];

      let hexR = r.toString(16);
      if (hexR.length === 1) { // toString 메서드는 01 을 1로 반환해서
        hexR = `0${hexR}`;
      }
      let hexG = g.toString(16);
      if (hexG.length === 1) { // toString 메서드는 01 을 1로 반환해서
        hexG = `0${hexG}`;
      }
      let hexB = b.toString(16);
      if (hexB.length === 1) { // toString 메서드는 01 을 1로 반환해서
        hexB = `0${hexB}`;
      }
      const hex = `#${hexR + hexG + hexB}`;
      return hex;
    },
    // 결과 보기 버튼을 눌렀을 때
    blocking() {
      this.informdisplay = (this.informdisplay === 'none') ? 'block' : 'none';
      this.informbutton = (this.informbutton === '결과 보기') ? '-' : '결과 보기';
    },
  },
  mounted() {
    document.querySelector('.clickevent').addEventListener('mousedown', this.mouseIsMoving);
  },
  computed: {
  },
  destroyed() {
    document.querySelector('.clickevent').removeEventListener('mousedown', this.mouseIsMoving);
  },
};
</script>
<style>
.centered {
  margin-left: auto;
  margin-right: auto;
  width:80%;
}
.previewimage {
  width:100%;
  background-color:gray;
  border-radius: 10px;
}
.previewimage > img {
  border-radius: 10px;
  margin: auto;
  padding: 5px;
  width: 100%;
}
.inform {
  margin:10px;
}
.marginBottom {
  margin-bottom: 8px;
  margin-left: auto;
  margin-right: auto;
  width:50%
}
.borderdash {
  /*border: solid 1px gray;*/
}
.informborder {
  margin-bottom: 8px;
  margin-left: auto;
  margin-right: auto;
  padding: 7px;
}
</style>
