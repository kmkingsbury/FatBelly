#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""Example of Flask and qrcode.

NOTE: by requirements image in memory!
"""

__author__ = 'Daniel Leybovich <setarckos@gmail.com>'
__version__ = (0, 0, 1)


import os
import sys
import flask
import qrcode
import cStringIO
from random import randint


app = flask.Flask(__name__)


def random_qr(url='www.google.com'):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    return img


@app.route('/get_qrimg')
def get_qrimg():
    img_buf = cStringIO.StringIO()
    myrand = randint(215278791477000, 215278791477986)
    print "Rand: " + str(myrand)
    img = random_qr(url=myrand)
    img.save(img_buf)
    img_buf.seek(0)
    return flask.send_file(img_buf, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
