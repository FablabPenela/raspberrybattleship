import cv2

#cap = cv2.VideoCapture('sample.mp4')
cap = cv2.VideoCapture(0)
w = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
print w, h
#cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, w/2)
#cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, h/2)

while cap.isOpened():
    success, frame = cap.read()
    if success == 0:
        break
    cv2.imwrite('output.png', frame)

    #cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	break

cap.release()
cv.destroyAllWindows()

