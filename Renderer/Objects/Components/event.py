from Renderer.Objects.Components.component import Component


class Event(Component):
    def __init__(self, actions):
        self.__actions = actions

    def run(self, action, **args):
        if action in self.__actions.keys():
            self.__actions[action]()
