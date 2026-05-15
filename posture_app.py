class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PostureGuard")

        layout = QVBoxLayout()

        self.label = QLabel("Camera Loading...")
        layout.addWidget(self.label)

        self.setLayout(layout)
