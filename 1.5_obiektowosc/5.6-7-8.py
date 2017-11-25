import json

run_ratio = 500
bike_ratio = 600
hobby_raito = 250
chess_ratio = 150
chocolate_ratio = 450
potato_ratio = 80

class Czlowiek:
    bmi = 0
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.correct_weight = 0
        self.diff = 0

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
                self.diff = abs(self.correct_weight - self.weight)
                print(self.diff)
            else:
                self.correct_weight = (self.height**2)*norm_b
                self.diff = self.weight - self.correct_weight
                print(abs(self.diff))
        return self.diff

    def save_data(self):
        with open('{}.json'.format(self.name),'w')as file:
            json.dump(self.__dict__,file)

    def to_burn(self):
        ratio = 6000
        if self.diff > 0:
            self.cals = self.diff*ratio
            self.run = self.cals/run_ratio
            self.bike = self.cals/bike_ratio
            self.hobby = self.cals/hobby_raito
            self.chess = self.cals/chess_ratio
            print('należy biegać {}, jeździć {},uprawiać hobby {} lub grać w szachy {} godzin'.format(self.run, self.bike, self.hobby, self.chess))

    def to_eat(self):
        ratio = 6000
        if self.diff < 0:
            self.cals = abs(self.diff*ratio)
            print(self.cals)
            self.chocolate = (self.cals/chocolate_ratio)*10
            self.potato = (self.cals/potato_ratio)*10
            print('należy zjeść {}kg czekolady lub {}kg ziemniaków'.format(self.chocolate, self.potato))
        else:
            print('jest ok')

    def what_to_do(self):
        self.count_bmi()
        self.diff_to_norm()
        if self.diff < 0:
            print('należy przytyć {}kg'.format(self.diff))
        elif self.diff > 0:
            print('należy zgubić {}'.format(abs(self.diff)))
        else:
            print('jest spoko')

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

a = Czlowiek('Teusz',1.90,99)
a.what_to_do()
# a.diff_to_norm()
# a.save_data()
# a.to_burn()
# a.to_eat()
# a.speak()
# b = Polityk()
# b.recive_bribe()
# b.speak()
