<template>
  <div class="centered borderdash">
    <div
    class="text-center borderdash"
    style="margin-bottom:30px;width:100%;">
      <h2 class="font-weight-bold">이미지로 분석하기</h2>
    </div>
    <div class="marginBottom borderdash" style="width:90%;">
      <div class="marginBottom text-center borderdash">
        <input
        type="file" name="file" id="file" ref="file"
        @change="change();resetData();"
        style="width:100%;">
      </div>
        <div class="marginBottom borderdash text-center" style="width:35%;">
          <v-btn type="button" outlined color="blue" @click="onSubmit">제출</v-btn>
        </div>
    </div>
    <hr>
    <div class="marginBottom borderdash" style="width:50%;">
      <div class="previewimage">
        <img :src="source" alt="Image"/>
      </div>
    </div>
    <hr>
    <div class="marginBottom borderdash text-center" style="width:320px;">
      <v-row
        class="borderdash"
        v-for="(color, idx) in [color1,color2,color3]"
        :key="idx"

        align="center"
      >
        <v-col
          class="borderdash"
          align="center"
          v-for="(value,index) in color"
          :key="index"
        >
          <v-card
            class="borderdash"
            :style="{'background-color': value.color}"
            style="height:80px;width:80px"
          >
            {{value.color}}
          </v-card>
        </v-col>
      </v-row>
      <p class="text-center">{{message}}</p>
    </div>
    <hr>
    <div class="resultButton marginBottom borderdash text-center"
      style="width:30%; display:none;">
      <v-btn
        @click="blocking()"
        outlined color="orange"
      >
        {{informbutton}}
      </v-btn>
    </div>

    <div class="inform marginBottom borderdash text-center"
      :style="{'display':informdisplay}"
      style="width:75%">
      <h4>Color Analysis Information</h4>
      <div class="firstinform">
        이미지 &#91;{{filename[filename.length-1]}}&#93;의 분석 결과,<br>
        <span v-for="(key,value) in deSeries" :key="value">
        {{key}}<span v-if="value != deSeries.length-1">, </span></span>
        계열의 색상이 사용되었습니다.<br><br>
      </div>
      <div class="marginBottom" style="width:60%">
        <v-row
          v-for = "colorarray in [color1,color2,color3]"
          :key="colorarray"
          justify = "center"
          align = "start"
        >
          <v-col
            v-for="arrvalue in colorarray"
            :key="arrvalue"
          >
            <div
              :style="{'background-color': arrvalue.color,
                'color': sb[arrvalue.number][1] < 38 ? 'white' : 'black'}"
              style="padding:3px"
            >
              {{arrvalue.color}}<br>
              {{colorSeries[arrvalue.number]}}<br>
              {{sb[arrvalue.number][0]}}% / {{sb[arrvalue.number][1]}}%
            </div>
          </v-col>
        </v-row>
      </div><br>
      <div class="secinform text-left">
        <div>
          <p>배색은 어떤 특별한 목적과 기능에 합치된 미적 효과를 얻기 위하여 두 가지 이상의 색이 조화를 이루도록 만드는 것이고
          다양한 배색을 기초로 하여 삼원색처럼 규정한 뒤 색을 섞거나 명암을 조절하여 배색의 조화를 이끌어냅니다.</p>
          <p>위에서 나온 색 중 최고 <span>{{color1.length}}</span>가지색을 혼합하여 나온색들을 이미지에 추가하면 더욱 효과적입니다.</p>
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
          <inform :color="informvalue"/>
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
    <div>
      <br><br>
      <br><br><br><br><br>
    </div>
  </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script>
import axios from 'axios';
import RingLoader from 'vue-spinner/src/RingLoader.vue'
import inform from './inform.vue'

export default {
  name: 'ImageColor',
  components: {
   RingLoader,
   inform,
  },
  data() {
    return {
      // color1 = [[{color: '#000000', number: 0}],[color: '#111111', number: 1], ...]
      color1: [],
      color2: [],
      color3: [],
      // 이미지 미리보기 주소
      source: '',
      // onSubmit 했을 때 message 바뀌고, 결과보기 버튼이 눌리면 informdisplay -> block
      message: '사용 방법 : 파일 선택 후 제출 버튼을 누르면 분석된 결과가 보여집니다',
      informdisplay: 'none',
      informbutton: '결과 보기',
      // 이미지 이름
      filename: '',
      // 얻은 색상 계열
      colorSeries: [],
      // 중복 없는 색상 계열
      deSeries: [],
      aInform: [],
      // 채도와 명도 sb = [[50,50],[20,100],...]
      sb: [],
      // 배색 colored = ['#000000','#111111','#222222']
      colored: [],
      spcolor: '#cc181e',
      spcolor1: '#5bc0de',
      spsize: '45px',
      spmargin: '2px',
      spradius: '2px',
      loading : false,
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
        let joinstr2 = '';
        let joinstr3 = '';
        let joinstr4 = '';
        for (let idx = 0; idx < this.color1.length; idx += 1) {
          joinstr1 += this.color1[idx].color;
        }
        for (let idx = 0; idx < this.color2.length; idx += 1) {
          joinstr2 += this.color2[idx].color;
        }
        for (let idx = 0; idx < this.color3.length; idx += 1) {
          joinstr3 += this.color3[idx].color;
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
          color2: joinstr2,
          color3: joinstr3,
          colored: joinstr4,
          filename: names,
          contents: content,
        };
        this.loading = true;
        const path = 'http://localhost:5000/addDB';
        axios.post(path, payload)
          .then(() => {
            console.log('success');
            this.loading = false;
          })
          .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          });
      });
    },
    // submit
    onSubmit() {
      const file = this.$refs.file.files[0];
      const formData = new FormData();
      formData.append('file', file);
      console.log(file);
      axios.post('http://localhost:5000/ping', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }).then((res) => {
        console.log(res);

        // 파일리스트에서 파일 제거
        const index = this.$refs.file.files[0];
        if (index > -1) {
          this.$refs.file.files.splice(index, 1);
        }
        // 결과 가져오기
        this.getColors();
        // 결과 보기 버튼 -> block
        document.getElementsByClassName('resultButton')[0].style.display = 'block';
      }).catch((err) => {
        console.log(err);
      });
    },
    // 색상코드 데이터 얻기
    getColors() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          // resData = [{"color": "#5e5e5f", "number": 0}, {"color": "#555555", "number": 1}, ...]
          const resData = res.data.colors;
          const lenData = (resData.length > 9) ? 9 : resData.length;
          for (let idx = 0; idx < lenData; idx += 1) {
            // 색상계열 얻기
            this.whatColor(this.codeR(resData[idx].color),
              this.codeG(resData[idx].color), this.codeB(resData[idx].color));
            // 변수 color1,2,3에 데이터 넣기
            if (idx < 3) {
              this.color1.push(resData[idx]);
            } else if (idx < 6) {
              this.color2.push(resData[idx]);
            } else if (idx < 9) {
              this.color3.push(resData[idx]);
            } else {
              break;
            }
          }
          this.message = '※ 왼쪽 위부터 차례대로 면적 크기 순서입니다';
          // 배색 컬러 얻기
          this.coloration();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    codeR(code) {
      const strarray = Array.from(code);
      const redcode = strarray[1] + strarray[2];
      const dec = parseInt(redcode, 16); // 16진수 -> 10진수
      return dec;
    },
    codeG(code) {
      const strarray = Array.from(code);
      const greencode = strarray[3] + strarray[4];
      const dec = parseInt(greencode, 16);
      return dec;
    },
    codeB(code) {
      const strarray = Array.from(code);
      const bluecode = strarray[5] + strarray[6];
      const dec = parseInt(bluecode, 16);
      return dec;
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
          txt.push('red-cyan');
        }
      }
      if (array.includes('green')) {
        if (array.includes('magenta')) {
          txt.push('green-magenta');
          txt.push('gm-neut');
        }
      }
      if (array.includes('blue')) {
        if (array.includes('yellow')) {
          txt.push('blue-yellow');
        }
      }
      if (array.includes('red')) {
        if (array.includes('yellow')) {
          if (array.includes('blue')) {
            txt.push('first');
          }
        }
      }
      if (!array.includes('magenta') && !array.includes('blue')
        && !array.includes('green') && !array.includes('cyan')
        && array.includes('red') && array.includes('yellow')) {
        txt.push('warm');
      }
      if (!array.includes('magenta') && array.includes('blue')
        && !array.includes('green') && array.includes('cyan')
        && !array.includes('red') && !array.includes('yellow')) {
        txt.push('cool');
      }
      this.aInform = txt;
      console.log(this.aInform);
    },
    // 배색
    coloration() {
      const r = [];
      const g = [];
      const b = [];
      for (let idx = 0; idx < this.color1.length; idx += 1) {
        r.push(this.codeR(this.color1[idx].color));
        g.push(this.codeG(this.color1[idx].color));
        b.push(this.codeB(this.color1[idx].color));
      }
      if (this.color1.length === 3) {
        this.colored.push(`#${this.toHex(r[0], r[1])
        + this.toHex(g[0], g[1]) + this.toHex(b[0], b[1])}`);
        this.colored.push(`#${this.toHex(r[0], r[2])
        + this.toHex(g[0], g[2]) + this.toHex(b[0], b[2])}`);
        this.colored.push(`#${this.toHex(r[1], r[2])
        + this.toHex(g[1], g[2]) + this.toHex(b[1], b[2])}`);
      } else if (this.color1.length === 2) {
        this.colored.push(`#${this.toHex(r[0], r[1])
        + this.toHex(g[0], g[1]) + this.toHex(b[0], b[1])}`);
      } else if (this.color1.length === 1) {
        this.colored.push('한 가지 색상은 배색 결과를 제공하지 않습니다.');
      }
    },
    // 10->16
    toHex(a, b) {
      let hex = (Math.round((a + b) / 2)).toString(16);
      if ((hex.split('')).length === 1) { // toString 메서드는 01 을 1로 반환해서
        hex = `0${hex}`;
      }
      return hex;
    },
    // 결과 보기 버튼을 눌렀을 때
    blocking() {
      this.informdisplay = (this.informdisplay === 'none') ? 'block' : 'none';
      this.informbutton = (this.informbutton === '결과 보기') ? '-' : '결과 보기';
    },
    // 사용자의 이미지 입력이 바뀌었을 때
    change() {
      console.log('change');
      const image = this.$refs.file.files[0];
      this.source = URL.createObjectURL(image);
      const name = document.getElementById('file').value;
      this.filename = name.split('\\');
    },
    // 초기화
    resetData() {
      document.getElementsByClassName('resultButton')[0].style.display = 'none';
      this.informdisplay = 'none';
      this.informbutton = '결과 보기';
      this.message = '사용 방법 : 파일 선택 후 제출 버튼을 누르면 분석된 결과가 보여집니다';
      this.color1 = [];
      this.color2 = [];
      this.color3 = [];
      this.colorSeries = [];
      this.deSeries = [];
      this.aInform = [];
      this.colored = [];
      this.sb = [];
    },
  },
  created() {
    // this.getColors();
  },
};
</script>
<style scoped>
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
.rect {
  margin: auto;
  width: 100%;
}
.inform {
  margin:10px;
  display: none;
}
.marginBottom {
  margin-bottom: 8px;
  margin-left: auto;
  margin-right: auto;
  width:50%
}
.borderdash {
  /* border: dashed gray; */
}
.informborder {
  margin-bottom: 8px;
  margin-left: auto;
  margin-right: auto;
  padding: 7px;
}
</style>
