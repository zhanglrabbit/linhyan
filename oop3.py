class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

class Timer(object):
    def run(self):
        print('Start...')

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(b, Dog))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(type(a))
print(type(b))
print(type(c))
print(type(object))
print(type(abs))


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())