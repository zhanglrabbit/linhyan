#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal1):     #传入的参数是一个实例对象，只要实例有run方法就行  oop多态
    animal1.run()
    animal1.run()

run_twice(Animal())
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

class Rabbit(Animal):
    def run(self):
        #print('Tortoise is running slowly...')
        pass

run_twice(Rabbit())


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)