from Renderer.Objects.object import Object
from Renderer.Objects.Components.text import Text


class Label(Object):
    def __init__(self, id, text, size, position=(0, 0),
                 color=(255, 255, 255), origin=(0, 0),
                 active=True):
        super().__init__(id, position, active=active)
        self.addComponent(Text(text, size, color, origin))
