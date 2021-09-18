import mpv

class MPVManager:
    def __init__(self):
        self.isPlaying = False
        self.isInitialized = False
    def begin(self):
        if not self.isInitialized:
            self.player = mpv.MPV(ytdl=True, video=False)
            self.isInitialized = True

    def play(self, audioFile):
        if not self.isInitialized:
            return
        self.player.play(audioFile)
        self.isPlaying = True

    def stop(self):
        if not self.isInitialized:
            return
        self.player.command('stop')
        self.isPlaying = False

    def exit(self):
        if not self.isInitialized:
            return
        self.player.command('stop')
        self.isPlaying = False
        self.isInitialized = False

    def setVolume(self, value):
        if not self.isInitialized:
            return
        self.player.volume = value

    def mute(self, value):
        if not self.isInitialized:
            return
        self.player.mute = value
