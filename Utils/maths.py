class Vector2:
    """Zmienna przechowująca dwie wartości x i y.
    Można utworzyć wprowadzając jedną wartość jak lista lub
    tuple albo wprowadzając 2 wartości po przecinkach."""

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], Vector2):
                self.x = args[0].x
                self.y = args[0].y
            else:
                self.x = float(args[0][0])
                self.y = float(args[0][1])
        elif len(args) == 2:
            self.x = float(args[0])
            self.y = float(args[1])
        else:
            print(f"Nie da się stworzyć Vector2 wartościami {args}")
            exit(1)

    def __add__(self, vector):
        if not isinstance(vector, Vector2):
            print(f"Nie można do Vector2 dodać {vector.__class__.__name__}")
            exit(1)
        self.x += vector.x
        self.y += vector.y
        return self

    def __sub__(self, vector):
        if not isinstance(vector, Vector2):
            print(f"Nie można od Vector2 odjąć {vector.__class__.__name__}")
            exit(1)
        self.x -= vector.x
        self.y -= vector.y
        return self


def getGreater(val1, val2):
    if val1 > val2:
        return val1
    return val2


def getLesser(val1, val2):
    if val1 < val2:
        return val1
    return val2


def getMinAndMax(val1, val2):
    return getLesser(val1, val2), getGreater(val1, val2)


def isBetween(min, max, val):
    return min <= val and val < max
