 self.face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
