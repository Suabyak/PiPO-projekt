from Renderer.Objects.Components.text import Text
from Renderer.colors import colors
from pygame import Surface


class ColouredText(Text):
    def __init__(self, text, size, color=(255, 255, 255),
                 origin=(0, 0)):
        super().__init__(text, size, color, origin)

    def render(self):
        text = self.getText()
        renders = list()
        toRender = text.split("/")
        pointer = 0
        width = 0
        for i in range(len(toRender)-1):
            textToRender = toRender[i]
            if i % 2 == 0:
                color = self.getColor()
            else:
                color = colors[textToRender[0]]
                textToRender = textToRender[1:]
            renderedText = super().render(textToRender, color)[0]
            renders.append((renderedText, (pointer, 0)))
            width += renderedText.get_size()[0]
            pointer = width
        surface = Surface((width, renderedText.get_size()[1]))
        for renderedText, position in renders:
            surface.blit(renderedText, position)
        return surface, self.getOrigin()
