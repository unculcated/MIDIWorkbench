import subprocess


class MidiPlayer:
    def __init__(self):
        self.process = None

    def play(self, midi_file):
        self.stop()

        soundfont = "/Users/ss/Downloads/GeneralUser-GS/GeneralUser-GS.sf2"

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