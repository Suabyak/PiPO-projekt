from Renderer.Objects.colouredLabel import ColouredLabel
from Renderer.Objects.Components.fade import Fade
from Renderer.Objects.Components.appear import Appear
from Renderer.Objects.Components.wait import Wait
from Renderer.Objects.Components.animationSequence import AnimationSequence


class Title(ColouredLabel):
    __WAIT_TIME = 0.3
    __CHANGE_TIME = 5.5

    def __init__(self, screenSize, action):
        super().__init__("Title", "Strażak /bBam/-/rBam/",
                         64, origin=(0.5, 0.5), position=(screenSize[0]/2, screenSize[1]/2))
        self.setVisibility(0)

        sequence = AnimationSequence()
        self.addComponent(sequence)
        sequence.add(Wait(self.__WAIT_TIME*60))  # 0.3 seconds
        sequence.add(Appear(self.__CHANGE_TIME*60))  # 5.5 seconds
        sequence.add(Wait(self.__WAIT_TIME*60*2))  # 0.6 seconds
        sequence.add(Fade(self.__CHANGE_TIME*60))  # 5.5 seconds
        sequence.add(Wait(0, action))
        sequence.start()
