 self.cap = cv2.VideoCapture(0)

self.timer = QTimer()
self.timer.timeout.connect(self.update_frame)
self.timer.start(30)
def update_frame(self):
    ret, frame = self.cap.read()

    if ret:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb.shape

        img = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)

        self.label.setPixmap(QPixmap.fromImage(img))
