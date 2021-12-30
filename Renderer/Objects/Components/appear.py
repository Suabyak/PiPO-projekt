from Renderer.Objects.Components.animation import Animation


class Appear(Animation):
    def __init__(self, time, active=False, action=None):
        super().__init__(time, active)
        self.__action = action

    def getAlpha(self):
        return int(self.getClock()/self.getTime()*255)

    def takeEffect(self):
        self.getParent().setVisibility(self.getAlpha())
        self.getParent().setActive(True)

    def reset(self):
        super().reset()

    def finish(self):
        super().finish()
        if self.__action:
            self.__action()
