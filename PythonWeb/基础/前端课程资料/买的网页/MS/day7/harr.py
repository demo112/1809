# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv

fd = cv.CascadeClassifier('face.xml')
ed = cv.CascadeClassifier('eye.xml')
nd = cv.CascadeClassifier('nose.xml')
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]
    faces = fd.detectMultiScale(frame, 1.3, 5)
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        cv.ellipse(frame, (l + a, t + b), (a, b), 0, 0, 360, (255, 0, 255), 2)
    face = frame[t:t + h, l:l + w]
    eyes = fd.detectMultiScale(frame, 1.3, 5)
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        cv.ellipse(frame, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 0), 2)
    eye = ed.detectMultiScale(face,)

    cv.imshow('VideoCapture', frame)
    if cv.waitkey(33) == 27:
        break
vc.release()
cv.destroyAllwindows()
