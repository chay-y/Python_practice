import numpy as np
import cv2

# 얼굴과 눈을 찾을 수 있는 xml 파일 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# 파일 읽어오기. 8비트 형식으로 데이터를 불러옴
ff = np.fromfile(r'모자이크.jpg',np.uint8)

# 이미지를 디코딩하여 읽어온 데이터를 이미지 형식으로 변환
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

# 이미지 크기 조정
# INTER_LINEAR : 선형 보간법을 이용
img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 컬러이미지를 흑백이미지로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지에서 얼굴을 탐지
faces = face_cascade.detectMultiScale(gray, 1.2,5)


# 찾은 얼굴의 위치와 크기를 가져옴
# x, y : 얼굴의 왼쪽 상단 모서리
# w, h : 얼굴의 크기
for (x,y,w,h) in faces :

    # 얼굴 위치에 사각형을 그림(BGR)
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    face_img = img[y:y+h, x:x+w]
    face_img = cv2.resize(face_img, dsize=(0,0), fx=0.1, fy=0.1)
    face_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
    img[y:y+h, x:x+w] = face_img

# 화면에 출력
cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()