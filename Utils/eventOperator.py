from pygame import event as Event, constants


class EventOperator:
    """Klasa do obsługi eventów."""

    def createEvent(id, values):
        """Stworzenie eventu i umieszczenie go w kolejce
        do obsłużenia później."""
        Event.post(Event.Event(id+100000, values))

    def __init__(self, main):
        """Przekazanie do obiektu odniesienia do głównej klasy."""
        self.__main = main
        self.__initEventOperators()

    def operateEvents(self):
        """Tutaj są wywoływane funkcje obsługujące eventy,
        te które nie mają funkcji obsługującej
        są wypisywane w konsoli."""
        for event in Event.get():
            try:
                self.__operatableEvents[event.type](event)
            except:
                print(event)

    def __initEventOperators(self):
        """Tutaj dodajemy obsługę wszystkich eventów
        które chcemy obsługiwać.
        Działa to w ten sposób że do słownika
        Przypisujemy jakiś typ eventu jako key
        i jakąś funkcje jako value.
        Funkcje obsługujące eventy muszą mieć 2 argumenty
        pierwszy self a drugi event który jest
        w tym momencie obsługiwany."""
        self.__operatableEvents = dict()
        self.__operatableEvents[constants.QUIT] = self.__main.quit