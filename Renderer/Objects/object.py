from Renderer.Objects.Components.component import Component
from Renderer.Objects.Components.transform import Transform
from abc import ABC, abstractmethod
from log import Log


class Object(ABC):
    __objects = dict()

    @abstractmethod
    def __init__(self, id, position=(0, 0), active=True, components=list(), parent=None):
        self.__id = id
        Log.executionLog(f"Object \"{self.getId()}\" created.")
        self.__components = dict()
        self.__renderable = False
        self.__active = active
        self.__visibility = 255
        self.__parent = parent
        for component in components:
            self.addComponent(component)
        if not self.hasComponent("Transform"):
            self.addComponent(Transform(position))

        Object.__objects[self.__id] = self

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
            Log.executionLog(
                f"\n[!] Object \"{self.getId()}\" has no Component \"{componentType}\"\n")
            exit(1)

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
        return self.__active and self.getVisibility() > 0

    def setActive(self, active):
        self.__active = active

    def getId(self):
        return self.__id

    def getComponents(self):
        return self.__components

    def getVisibility(self):
        if self.getParent():
            visibility = self.__visibility / 255.0 * \
                self.getParent().getVisibility() / 255.0
            return int(visibility*255)
        return self.__visibility

    def setVisibility(self, visibility):
        self.__visibility = visibility

    def setParent(self, parent):
        self.__parent = parent

    def getParent(self):
        return self.__parent

    def get(id):
        if id not in Object.__objects.keys():
            raise Exception(f"There is no {id} object.")
        return Object.__objects[id]
