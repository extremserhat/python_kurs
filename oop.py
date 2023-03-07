class Roboter:
    def sagehallo(self):
        print("Hallo mein Name ist " + self.name)
    def setzename(self, name):
        self.name =name
    def setzebaujahr(self, baujahr):
        self.baujahr = baujahr
x = Roboter()
x.setzename("Marvin")
x.setzebaujahr(1990)
y = Roboter()
y.setzename("Caliban")
y.setzebaujahr(1993)

x.sagehallo()
y.sagehallo()
