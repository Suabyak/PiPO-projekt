from Renderer.Objects.object import Object
from Renderer.Objects.Components.appear import Appear
from Renderer.Objects.Components.fade import Fade


class MainMenuOperator(Object):
    def __init__(self, action):
        super().__init__("MainMenuOperator")

        self.addComponent(Appear(3*60))
        self.addComponent(Fade(0.5*60, action=action))
        self.setVisibility(0)
