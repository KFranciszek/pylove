class Czlowiek:
    bmi = 0
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.correct_weight = 0

    def speak(self):
        print('Mowie prawde')
        pass

    def count_bmi(self):
        self.bmi = (self.weight / self.height**2)
        print(self.bmi)

    def diff_to_norm(self):
        pass
    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    def __init__(self):
        self.check = False

    def speak(self):
        if not self.check:
            print('Klamie bo moge')
        else:
            super().speak()
        pass

    def recive_bribe(self):
        self.check = True
        pass

a = Czlowiek('Teusz',1.90,100)
a.count_bmi()
a.diff_to_norm()
# a.speak()
# b = Polityk()
# b.recive_bribe()
# b.speak()
