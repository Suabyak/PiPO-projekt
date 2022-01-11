from pygame import event as Event, constants


class EventOperator:
    """Klasa do obsługi eventów."""

    PLAY = Event.custom_type()
    STOP = Event.custom_type()

    def createEvent(id, values):
        """Stworzenie eventu i umieszczenie go w kolejce
        do obsłużenia później."""
        Event.post(Event.Event(id, values))

    def __init__(self, main):
        """Przekazanie do obiektu odniesienia do głównej klasy."""
        self.__main = main
        self.__initEventOperators()

    def operateEvents(self):
        """Tutaj są wywoływane funkcje obsługujące eventy,
        te które nie mają funkcji obsługującej
        są wypisywane w konsoli."""
        for event in Event.get():
            if event.type in self.__operatableEvents.keys():
                self.__operatableEvents[event.type](event)
            else:
                pass  # print(event)

    def __initEventOperators(self):
        """Tutaj dodajemy obsługę wszystkich eventów
        które chcemy obsługiwać.
        Działa to w ten sposób że do słownika
        Przypisujemy jakiś typ eventu jako key
        i jakąś funkcje jako value.
        Funkcje obsługujące eventy muszą mieć 2 argumenty
        pierwszy main a drugi event który jest
        w tym momencie obsługiwany."""
        self.__operatableEvents = {
            constants.QUIT: self.__main.quit,
            constants.MOUSEBUTTONDOWN: self.__main.mouseClick,
            constants.MOUSEMOTION: self.__main.mouseMotion,
            constants.KEYDOWN: self.__main.keyDown,
            constants.KEYUP: self.__main.keyUp,
            self.PLAY: self.__main.playSound,
            self.STOP: self.__main.stopSound
            }
