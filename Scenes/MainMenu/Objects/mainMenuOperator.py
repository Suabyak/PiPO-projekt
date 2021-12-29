from Renderer.Objects.object import Object
from Renderer.Objects.Components.animationSequence import AnimationSequence
from Renderer.Objects.Components.appear import Appear


class MainMenuOperator(Object):
    def __init__(self):
        super().__init__("MainMenuOperator")

        self.addComponent(Appear(3*60))
        self.setVisibility(0)
