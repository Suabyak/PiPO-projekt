from Renderer.Objects.Components.text import Text
from Renderer.colors import colors
from pygame import Surface


class ColouredText(Text):
    def __init__(self, text, size, color=(255, 255, 255),
                 origin=(0, 0)):
        super().__init__(text, size, color, origin)

    def render(self):
        text = self.getText()
        font = Text.getFont(self.getFontSize())
        surface = Surface(font.size(text))

        toRender = text.split("/")
        pointer = 0
        for i in range(len(toRender)):
            textToRender = toRender[i]
            if i % 2 == 0:
                color = self.getColor()
            else:
                color = colors[textToRender[0]]
                textToRender = textToRender[1:]
            print(textToRender, color)
            renderedText = super().render(textToRender, color)[0]
            surface.blit(renderedText, (pointer, 0))
            pointer += renderedText.get_size()[0]
        print()
        return surface, self.getOrigin()
