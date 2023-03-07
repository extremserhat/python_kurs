class Roboter:
    def __init__(self, name, baujahr):
        self.name = name
        self.baujahr = baujahr

        
    def sagehallo(self):
        # kann auf name zugreifen weil es in der selben Klasse ist
        print("hallo mein Name ist ", self.name + "mein baujahr ", self.baujahr)

    def setzename(self, name):
        self.name = name

    def setzebaujahr(self, baujahr):
        self.baujahr = baujahr

    def holebaujahr(self):
        # Muss von Int auf Str übersetzt werden
        return str(self.baujahr) 

x = Roboter("Marvin ", 1990)
y = Roboter("Caliban", 2003)

for i in [x, y]:
    i.sagehallo()
    print("ich bin " + i.holebaujahr() + " erschaffen worden")
