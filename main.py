import os
import sys

from player import MidiPlayer

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
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

        self.player = MidiPlayer()

        self.setWindowTitle("🎹 MIDI Workbench")
        self.resize(1100, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        # Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        open_action = toolbar.addAction("📂 Open Folder")
        open_action.triggered.connect(self.open_folder)

        toolbar.addSeparator()
        toolbar.addAction("🎼 SoundFont")

        body = QHBoxLayout()
        layout.addLayout(body)

        self.files = QListWidget()
        self.files.currentItemChanged.connect(self.show_file_info)
        body.addWidget(self.files, 1)

        self.info = QTextEdit()
        self.info.setReadOnly(True)
        body.addWidget(self.info, 2)

        controls = QHBoxLayout()
        layout.addLayout(controls)

        self.play_button = QPushButton("▶ Play")
        self.play_button.clicked.connect(self.play)
        controls.addWidget(self.play_button)

        self.stop_button = QPushButton("■ Stop")
        self.stop_button.clicked.connect(self.stop)
        controls.addWidget(self.stop_button)

        controls.addStretch()

        self.status = QLabel("Ready")
        controls.addWidget(self.status)

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Choose MIDI Folder"
        )

        if not folder:
            return

        self.files.clear()

        midi_files = []

        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith((".mid", ".midi")):
                    midi_files.append(os.path.join(root, file))

        midi_files.sort()

        for file in midi_files:
            self.files.addItem(file)

        self.status.setText(f"{len(midi_files)} MIDI files")

        self.info.setPlainText(
            f"Folder:\n{folder}\n\n"
            f"MIDI Files Found: {len(midi_files)}"
        )

    def show_file_info(self, current, previous):
        if current is None:
            return

        path = current.text()
        size = os.path.getsize(path)
        size_kb = size / 1024
        filename = os.path.basename(path)

        self.info.setPlainText(
            f"""Filename:
{filename}

Full Path:
{path}

Size:
{size_kb:.1f} KB
"""
        )

    def play(self):
        current = self.files.currentItem()

        if current is None:
            self.status.setText("No MIDI selected")
            return

        self.player.play(current.text())
        self.status.setText("Playing...")

    def stop(self):
        self.player.stop()
        self.status.setText("Stopped")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()