class AUTO:
    def __init__(self, marka_, tipus_, gyartasiev_, sebesseg_):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasiev = gyartasiev_
        self.sebesseg = sebesseg_

    def __str__(self):
        return f'{self.marka} {self.tipus} ({self.gyartasiev}), sebesség: {self.sebesseg} km/h.'
    
    def gyorsit(self, gyorsulas):
        self.sebesseg += gyorsulas
        if self.sebesseg > 200:
            self.sebesseg = 200

    def fekez(self, fekezes):
        self.sebesseg -= fekezes
        if self.sebesseg < 0:
            self.sebesseg = 0