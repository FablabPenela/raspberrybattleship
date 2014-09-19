import cv2

webcam = cv2.VideoCapture(0)
webcam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

if webcam.isOpened():
	success, frame = webcam.read()
	if success == True:
		cv2.imwrite('snapshot.png', frame)
		print 'sucesso!'
	else:
		print 'falhou!'
webcam.release()

