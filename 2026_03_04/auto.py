class AUTO:
    def __init__(self, marka_, tipus_, gyartasiev_, fogyasztas_, uzemanyag_=50):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasiev = gyartasiev_
        self.sebesseg = 0
        self.fogyasztas = fogyasztas_
        self.uzemanyag = uzemanyag_

    def __str__(self):
        return f'{self.marka} {self.tipus} ({self.gyartasiev}), sebesség: {self.sebesseg} km/h. Az üzemanyag: {self.uzemanyag}'
    
    def gyorsit(self, gyorsulas):
        self.sebesseg += gyorsulas
        if self.sebesseg > 200:
            self.sebesseg = 200

    def fekez(self, fekezes):
        self.sebesseg -= fekezes
        if self.sebesseg < 0:
            self.sebesseg = 0

    def tankol(self, tankolas):
        self.uzemanyag += tankolas
        if self.uzemanyag > 50:
            self.uzemanyag = 50

    def utazik(self, tavolsag):
        elfogyasztott_uzemanyag = (tavolsag/100) * self.fogyasztas
        if elfogyasztott_uzemanyag > self.uzemanyag:
            print('REFILL FUELTANK')
        else:
            self.uzemanyag -= elfogyasztott_uzemanyag
            print(f'{elfogyasztott_uzemanyag} liter üzemanayagot fogasztott el')
        
        