from Renderer.Objects.object import Object


class Camera(Object):
    def __init__(self):
        super().__init__("Camera")

    def move(self, offset):
        self.getComponent("Transform").move(offset)
