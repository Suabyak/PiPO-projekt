from Renderer.Objects.Components.colouredText import ColouredText
from Renderer.Objects.object import Object


class ColouredLabel(Object):
    def __init__(self, id, text, size, position=(0, 0),
                 color=(255, 255, 255), origin=(0, 0)):
        super().__init__(id, position)
        self.addComponent(ColouredText(text, size, color, origin))
