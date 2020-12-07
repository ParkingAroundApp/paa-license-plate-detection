from model.recognition import E2E
import cv2
import argparse
import time
from flask import Flask, request
import base64
import numpy as np

import json

app = Flask(__name__)
def get_arguments():
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--image_path', help='link to image', default='./images/40.jpg')

    return arg.parse_args()

@app.route('/')
def index():
    return 'hi';


@app.route('/findlp', methods=[ 'POST'])
def findLPwithImg2():
    req_data = request.get_json()
    imageStr = req_data['license-img']
    image = imageStr[23:]

    decoded_data = base64.b64decode(image)
    np_data = np.fromstring(decoded_data, np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)


    # scale_percent = 30
    # width = int(img.shape[1] * scale_percent / 100)
    # height = int(img.shape[0] * scale_percent / 100)
    # dsize = (width, height)
    # img = cv2.resize(img, dsize)

    # start
    start = time.time()

    # load model
    model = E2E()

    # recognize license plate
    image = model.predict(img)
    # print("License Plate Text: " + image)

    # end
    end = time.time()
    print('Model process on %.2f s' % (end - start))
    return json.dumps(
        {
            "firstLine":image['first_line'],
            "secondLine": image["second_line"],
            "timeResponse": end-start,
        }
    );

