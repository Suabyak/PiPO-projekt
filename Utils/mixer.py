from pygame import mixer
from os import listdir


class Mixer:
    __tracks = dict()

    def __init__(self):
        for path in listdir("data"):
            if path not in Mixer.__tracks.keys() and ".mp3" in path:
                path = path.replace(".mp3", "")
                Mixer.__tracks[path] = mixer.Sound(f"data\\{path}.mp3")

    def playSound(self, game, event):
        loops = -1
        if "loops" in event.dict.keys():
            loops = event.dict["loops"]
        Mixer.getTrack(event.dict["name"]).play(loops)

    def stopSound(self, game, event):
        Mixer.getTrack(event.dict["name"]).stop()

    def getTrack(name):
        return Mixer.__tracks[name]
