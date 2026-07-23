import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("🎹 MIDI Workbench")

        self.resize(1100,700)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        toolbar = QToolBar()

        self.addToolBar(toolbar)

        toolbar.addAction("📂 Open Folder")

        toolbar.addSeparator()

        toolbar.addAction("🎼 SoundFont")

        body = QHBoxLayout()

        layout.addLayout(body)

        self.files = QListWidget()

        body.addWidget(self.files)

        self.info = QTextEdit()

        self.info.setReadOnly(True)

        body.addWidget(self.info)

        controls = QHBoxLayout()

        layout.addLayout(controls)

        controls.addWidget(QPushButton("▶ Play"))

        controls.addWidget(QPushButton("■ Stop"))

        controls.addStretch()

        controls.addWidget(QLabel("Ready"))


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()