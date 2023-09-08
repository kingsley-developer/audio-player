from audioplayer import AudioPlayer
class Audio:
    def __init__(self, file_path):
        self.file = AudioPlayer(file_path)

    def play(self):
        self.file.play(block=True)

