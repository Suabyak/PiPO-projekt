from Renderer.Objects.Components.animation import Animation


class Fade(Animation):
    def __init__(self, time, active=False):
        super().__init__(time, active)

    def getAlpha(self):
        return int((self.getTime() - self.getClock())/self.getTime()*255)

    def takeEffect(self):
        self.getParent().setVisibility(self.getAlpha())

    def reset(self):
        super().reset()
        self.getParent().setActive(False)
