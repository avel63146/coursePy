class Thing():
    pass

Th = Thing()
print(Thing)
print(Th)

class Thing2():
    letters = 'abc'
print(Thing2.letters)

class Thing3():
    letters = 'wyz'
Th3 = Thing3
print(Th3.letters)

class Elements():
    dict_H = {
        'Name': 'Hydrogen',
        'symbol': 'H',
        'number': '1'}
    def dump(self, value):
        self.__value = value
        print(value)
        
class hydrogen(Elements):
    pass

print(hydrogen.dict_H)

dict_H = Elements.dict_H
hydrogen = Elements()
hydrogen.dump(dict_H.values())
print(hydrogen)
print(hydrogen)


class animals():
    def eats(self):
        print('animals eats ever!')

class Bear(animals):
    def eats(self):
        print('Bear eats berreis')
class Rabbit(animals):
    def eats(self):
        print('Rabbits eats campers')
class Octopus(animals):
    def eats(self):
        print('Octopus eats fish')

bear = Bear.eats(None)
rabbit = Rabbit.eats(None)
octopus = Octopus.eats(None)

class Claw():
    def does(self, crush):
        return crush
class Laser():
    def does(self, disint):
        return disint
class SmartPhone():
    def does(self, ring):
        return ring

class Robot():
    def does(self):
        return Claw.does(None, 'ww'), Laser.does(None, '2ww'), SmartPhone.does(None, 'qq')

print(Robot.does(None))