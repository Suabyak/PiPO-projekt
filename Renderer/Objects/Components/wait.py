from Renderer.Objects.Components.animation import Animation


class Wait(Animation):
    def __init__(self, time, action=None, active=False):
        super().__init__(time, active)
        self.__action = action

    def takeEffect(self):
        if self.getTime() <= self.getClock() and self.__action:
            self.__action()

    def reset(self):
        super().reset()
