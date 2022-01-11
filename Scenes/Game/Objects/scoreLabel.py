from Renderer.Objects.label import Label


class ScoreLabel(Label):
    def __init__(self):
        super().__init__("ScoreLabel", "Wynik: 0", 32, position=(50, 50))

    def setScore(self, score):
        self.getComponent("Text").setText(f"Wynik: {score}")
