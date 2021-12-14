class Vector2:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = int(args[0][0])
            self.y = int(args[0][1])
        elif len(args) == 2:
            self.x = int(args[0])
            self.y = int(args[1])
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
