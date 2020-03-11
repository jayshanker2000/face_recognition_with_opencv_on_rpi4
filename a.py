import cv2

# For diiferent types of classifiers.
# Ensure that the files are downloaded form official repository of github &
# are in the same folder as that of the .py file.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),3)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		eyes = eye_cascade.detectMultiScale(roi_gray)
		smiles = smile_cascade.detectMultiScale(roi_gray, 1.3, 5) 

		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
		for (sx, sy, sw, sh) in smiles: 
            		cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)

	cv2.imshow('img',img)

	
	if cv2.waitKey(30) & 0xff == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
