from Renderer.Objects.Components.component import Component
from Renderer.Objects.Components.transform import Transform
from pygame.surface import Surface


class Object:
    def __init__(self, id, active=True, components=list()):
        self.__id = id
        self.__components = dict()
        self.__renderable = False
        self.__active = active
        for component in components:
            self.addComponent(component)
        if not self.hasComponent("Transform"):
            self.addComponent(Transform(0, 0))

    def addComponent(self, component):
        """Dodanie komponentu do obiektu jeżeli dziedzyczy z
        klasy Component."""
        if issubclass(component.__class__, Component):
            self.__components[component.getType()] = component

    def getComponent(self, componentType):
        if self.hasComponent(componentType):
            return self.__components[componentType]
        else:
            print(f"Ten obiekt nie ma komponentu typu \'{componentType}\'")
            exit(1)

    def hasComponent(self, componentType):
        return componentType in self.__components.keys()

    def isRenderable(self):
        return self.hasComponent("Image") or self.hasComponent("Label")

    def isActive(self):
        return self.__active

    def getId(self):
        return self.__id

    def getComponents(self):
        return self.__components
