class Czlowiek:
    def __init__(self):
        pass

    def speak(self):
        print('Mowie prawde')
        pass

    def count_bmi(self):
        pass

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

# a = Czlowiek()
# a.speak()
b = Polityk()
# b.recive_bribe()
b.speak()
