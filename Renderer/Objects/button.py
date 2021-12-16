from Renderer.Objects.object import Object
from Renderer.Objects.Components.collider import Collider
from Renderer.Objects.Components.event import Event


class Button(Object):
    def __init__(self, id, mainComponent, action, position=(0, 0)):
        if mainComponent.getType() not in ["Image", "Text", "Rect"]:
            print("Głównym komponentem może być tylko zdjęcie, "
                  "\"rect\" lub napis.")
            exit(1)
        self.__mainComponent = mainComponent.getType()
        super().__init__(id, position, components=[mainComponent])
        self.addComponent(
            Collider(self.getComponent(self.__mainComponent).getSize(),
                     self.getComponent(self.__mainComponent).getOrigin()))
        self.addComponent(Event({"Click": action}))
