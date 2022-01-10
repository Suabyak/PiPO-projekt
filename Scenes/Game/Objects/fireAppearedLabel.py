from Renderer.Objects.label import Label
from Renderer.Objects.Components.fade import Fade


class FireAppearedLabel(Label):
    def __init__(self, screenSize):
        super().__init__("FireAppearedLabel", "Wybuchł Pożar!",
                         64, (screenSize[0]/2, 100),
                         (220, 155, 40), (0.5, 0.5), active=False)
        self.addComponent(Fade(600))
