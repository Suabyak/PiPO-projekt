from component import Component
from transform import Transform


class Object:
    def __init__(self, id, active=True, components=list()):
        self.__id = id
        self.__components = dict()
        self.__renderable = False
        self.__active = active
        self.addComponent(Transform(0, 0))
        for component in components:
            self.addComponent(component)

    def addComponent(self, component):
        if issubclass(component.__class__, Component):
            if component.getType() == "Image":
                self.__renderable = True
            self.__components[component.getType()] = component

    def getComponent(self, componentType):
        try:
            return self.__components[componentType]
        except KeyError as e:
            print(f"Ten obiekt nie ma komponentu typu {e}")
            exit(1)

    def isRenderable(self):
        return self.__renderable

    def isActive(self):
        return self.__active

    def getId(self):
        return self.__id
