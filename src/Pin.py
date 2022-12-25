

class Pin:
    max_position = map_length = 40

    def __init__(self, color, position) -> None:
        self.color = color
        self.position = position 

    def advance(self, distance):
        self.position = (self.position + distance) % self.max_position
        