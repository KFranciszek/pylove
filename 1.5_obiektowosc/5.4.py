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
        norm_t = 25
        norm_b = 18.5
        if not norm_b < self.bmi < norm_t:
            if norm_b < self.bmi:
                self.correct_weight = (self.height**2)*norm_t
                print(abs(self.correct_weight - self.weight))
            else:
                self.correct_weight = (self.height**2)*norm_b
                print(abs(self.weight - self.correct_weight))
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
