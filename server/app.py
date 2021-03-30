from flask import Flask, jsonify, request
from flask_cors import CORS
import PIL.Image as pilimg
import numpy as np
from collections import Counter
import re as regex
import io
import pymysql
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform
import os
import pyimgur


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
cors = CORS(app, resources={r'/*': {'origins': '*'}})

# imgur api setting
CLIENT_ID = ""

path = "C:\Windows\Fonts\malgun.ttf"

if platform.system() == "Darwin" :
    rc('font', family="AppleGothic")
elif platform.system() == "Windows" :
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system')

# database setting
connection= pymysql.connect(
    host='',
    port=,
    user='',
    passwd='',
    db='',
    charset='utf8')

filename = ''
@app.route('/addFile', methods=['GET', 'POST'])
def file_store():
    response = {'state' : 'success'}
    if request.method == 'POST':
        re = request.files['file']
        path = '../client/src/store'
        path = os.path.join(path , re.filename)
        re.save(path)

        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(path, title=re.filename)
        print(uploaded_image.title)
        print(uploaded_image.link)
        a = uploaded_image.link
        a = a.split('/')
        new_filename = a[-1]
        global filename
        filename = new_filename
        response['filename'] = filename
    else :
        response['filename'] = filename
    return jsonify(response)



@app.route('/addDB', methods=['GET', 'POST'])
def reqres_data():
    DB_RESULT = []
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        req_color1 = post_data.get('color1')
        req_color2 = post_data.get('color2')
        req_color3 = post_data.get('color3')
        req_colored = post_data.get('colored')
        req_filename = post_data.get('filename')
        req_contents = post_data.get('contents')
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `result` (`FILENAME`, `COLORCODE1`, `COLORCODE2`, `COLORCODE3`, `COLORED`, `CONTENTS`) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (req_filename, req_color1, req_color2, req_color3, req_colored, req_contents))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            # connection.close()
            response_object['message'] = 'Tuple inserted!'
    else:
        try:
            with connection.cursor() as cursor:
                sql = "SELECT MAX(id) FROM `result`"
                cursor.execute(sql)
                max = cursor.fetchone()
                print(max[0])
            if max[0] != '':
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "SELECT `COLORCODE1`, `COLORCODE2`, `COLORCODE3`, `COLORED`, `CONTENTS`, `FILENAME` FROM `result` WHERE `id` > %s"
                    cursor.execute(sql, (max[0] - 9))
                    result = cursor.fetchall()
                    print(result)
                    
                    for el in result:
                        DB_RESULT.append({
                            'colorcode1': el[0],
                            'colorcode2': el[1],
                            'colorcode3': el[2],
                            'colored': el[3],
                            'contents': el[4],
                            'filename': el[5],
                        })    
        finally:
            # connection.close()
            response_object['result'] = DB_RESULT
            print(response_object)
        
    return jsonify(response_object)

IMAGES = [
    {
        'number': 1,
        'color': '#000000' 
    },
    {
        'number': 2,
        'color': '#ffffff'
    }
]

def redrange(r):
    list1 = [ i*48 for i in range(6)]
    result = [0,0,0]
    for a in list1:
        if r[0][0] >= a and r[0][0] < (a + 24):
            result[0] = a
        elif r[0][0] >= (a+24) and r[0][0] < (a + 48):
            result[0] = a + 48
    for a in list1:
        if r[0][1] >= a and r[0][1] < (a + 24):
            result[1] = a
        elif r[0][1] >= (a+24) and r[0][1] < (a + 48):
            result[1] = a + 48
    for a in list1:
        if r[0][2] >= a and r[0][2] < (a + 24):
            result[2] = a
        elif r[0][2] >= (a+24) and r[0][2] < (a + 48):
            result[2] = a + 48
    return result

@app.route('/ping', methods=['GET', 'POST'])
def ping_pong():
    obj = {'status': 'success'}
    if request.method == 'POST':
        IMAGES.clear()
        re = request.files['file']
        image = pilimg.open(re)
        print(image.size)
        # 이미지 리사이즈
        width, height = image.size
        if width > 1280:
            height = int(height * 1280 / width)
            image = image.resize((1280, height))
        print(image.size)

        pix = np.array(image)
        code = []
        for idz in range(len(pix)):
            for idx in range(len(pix[idz])):
                color_r = pix[idz][idx][0]
                color_g = pix[idz][idx][1]
                color_b = pix[idz][idx][2]
                code.append((color_r, color_g, color_b))

        result = Counter(code)
        print(len(result))
        secResult = result.most_common(len(result))
        print(len(secResult))
        thResult = [i for i in secResult if i[1] > 1]
        print(len(thResult))

        resultlist = []

        for r in thResult:
            resultlist.append(redrange(r))
        print(len(resultlist))

        i = 0
        indexlist = []
        for r in resultlist:
            for r2 in resultlist:
                if r == r2 or r2 == [224,224,224] or r2 == [0,0,0] or (r[0] == r2[0] and r[1] == r2[1]) or (r[0] == r2[0] and r[2] == r2[2]) or (r[2] == r2[2] and r[1] == r2[1]):
                    indexlist.append(i)
                i += 1
            i = 0
            indexlist.reverse()
            for a in indexlist:
                if a != resultlist.index(r):
                    resultlist.pop(a)
                    thResult.pop(a)
            indexlist = []

        thResult2 = []
        for tr in thResult:
            thResult2.append(['#{:02x}{:02x}{:02x}'.format(tr[0][0], tr[0][1], tr[0][2]), tr[1]])
        print(thResult2)

        # obj 리스트에 결과를 넣기
        for idy in range(len(thResult2)):
            IMAGES.append({
                'number': idy,
                'color': thResult2[idy][0],
                'counts': thResult2[idy][1],
            })
        obj['message'] = 'Image added!'
    else:
        obj['colors'] = IMAGES
    return jsonify(obj)


if __name__ == '__main__':
    app.run()
