from Renderer.Objects.object import Object
from Renderer.Objects.Components.collider import Collider
from Renderer.Objects.Components.event import Event


class Button(Object):
    def __init__(self, id, mainComponent, action, active=True,
                 position=(0, 0), parent=None):
        if mainComponent.getType() not in ["Image", "Text", "Rect"]:
            raise Exception("Głównym komponentem przycisku może być"
                            "tylko zdjęcie, \"rect\" lub napis.")

        self.__mainComponent = mainComponent.getType()
        super().__init__(id, position, active=active,
                         components=[mainComponent], parent=parent)
        self.addComponent(
            Collider(self.getComponent(self.__mainComponent).getSize(),
                     self.getComponent(self.__mainComponent).getOrigin()))
        self.addComponent(Event({"Click": action}))
