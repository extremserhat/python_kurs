class Roboter:
    def __init__(self, name, baujahr):
        self.name = name
        self.baujahr = baujahr

        
    def sagehallo(self):
        print("hallo mein Name ist ", self.name + "mein baujahr ", self.baujahr)


    def setzename(self, name):
        self.name = name

    def setzebaujahr(self, baujahr):
        self.baujahr = baujahr

x = Roboter("Marvin ", 1990)
y = Roboter("Caliban", 2003)

x.sagehallo()
y.sagehallo()
