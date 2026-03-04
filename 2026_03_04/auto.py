class AUTO:
    def __init__(self, marka_, tipus_, gyartasiev_):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasiev = gyartasiev_

    def __str__(self):
        return f'{self.marka} {self.tipus} ({self.gyartasiev})'
