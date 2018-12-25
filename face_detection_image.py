import cv2

filename = 'young_couple.jpg'

def detect(filename):
	face_cascade =cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
	img = cv2.imread(filename)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	#cv2.namedWindow('Face')
	cv2.imshow('Face', img)
	cv2.imwrite('./young_couple.jpg', img)
	cv2.waitKey(0)

detect(filename)
