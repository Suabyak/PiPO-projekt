from Renderer.Objects.Components.component import Component
from Renderer.Objects.Components.transform import Transform
from abc import ABC, abstractmethod
from log import Log


class Object(ABC):
    @abstractmethod
    def __init__(self, id, position=(0, 0), active=True, components=list()):
        self.__id = id
        Log.executionLog(f"Object \"{self.getId()}\" created.")
        self.__components = dict()
        self.__renderable = False
        self.__active = active
        self.__visibility = 255
        for component in components:
            self.addComponent(component)
        if not self.hasComponent("Transform"):
            self.addComponent(Transform(position))

    def addComponent(self, component):
        """Dodanie komponentu do obiektu jeżeli dziedzyczy z
        klasy Component."""
        if issubclass(component.__class__, Component):
            component.setParent(self)
            self.__components[component.getType()] = component
            Log.executionLog(
                f"Component \"{component.getType()}\" added to Object \"{self.getId()}\"")

    def getComponent(self, componentType):
        if self.hasComponent(componentType):
            return self.__components[componentType]
        else:
            print(f"Ten obiekt nie ma komponentu typu \'{componentType}\'")
            Log.executionLog(
                f"\n[!] Object \"{self.getId()}\" has no Component \"{componentType}\"\n")
            exit(1)

    def getComponents(self):
        return self.__components.values()

    def hasComponent(self, componentType):
        return componentType in self.__components.keys()

    def hasAnyComponent(self, componentTypes):
        for componentType in componentTypes:
            if self.hasComponent(componentType):
                return True
        return False

    def isRenderable(self):
        return self.hasAnyComponent(("Image", "Text", "Rect", "ColouredText"))

    def isActive(self):
        return self.__active

    def setActive(self, active):
        self.__active = active

    def getId(self):
        return self.__id

    def getComponents(self):
        return self.__components

    def getVisibility(self):
        return self.__visibility

    def setVisibility(self, visibility):
        self.__visibility = visibility
