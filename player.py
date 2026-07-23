import subprocess

from settings import load_settings


class MidiPlayer:
    def __init__(self):
        self.process = None

    def play(self, midi_file):
        self.stop()

        settings = load_settings()
        soundfont = settings["soundfont"]

        self.process = subprocess.Popen([
            "fluidsynth",
            "-i",
            soundfont,
            midi_file,
        ])

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process.wait()
            self.process = None