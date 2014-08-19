# -*- coding: utf-8 -*-
import os

import cv2
import numpy as np
from flask import Flask, jsonify, Blueprint, request
from flask.views import MethodView


PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
app = Flask(__name__)


class Faced(object):

    def __init__(self, haarcascade_xml_path='lib/haarcascade_frontalface_alt.xml'):
        path = os.path.join(PROJECT_DIR,haarcascade_xml_path)
        self.cascade = cv2.CascadeClassifier(path)

    def opencv_image_from_stream(self, img_stream, cv2_img_flag=0):
        img_stream.seek(0)
        img_array = np.asarray(bytearray(img_stream.read()), dtype=np.uint8)
        return cv2.imdecode(img_array, cv2_img_flag)

    def detect(self, img_stream):
        img = self.opencv_image_from_stream(img_stream)
        if img is None:
            return False
        rects = cascade.detectMultiScale(img, 1.2, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
        return len(rects)


class DetectView(MethodView):
    methods = ['POST']

    def post(self):
        if 'file' not in request.files:
            return jsonify({'error': {'message': '`file` is required.'}}), 400
        faced = Faced()
        count = faced.detect(request.files['file'])
        if count is None:
            count = 0
        return jsonify({'count': count}), 200


bp = Blueprint('faced', __name__, url_prefix='/')
bp.add_url_rule('/detect', view_func=DetectView.as_view('detect'))


if __name__ == '__main__':
    app.run()
