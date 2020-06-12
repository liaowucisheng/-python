#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/1 17:41
# File: 面向對象-編程熟悉3

from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, pet_name):
        self._pet_name = pet_name

    @abstractmethod
    def make_voice(self):
        pass


class Cat(Pet):
    def make_voice(self):
        print('%s: miaooooooo' % self._pet_name)


class Dog(Pet):
    def make_voice(self):
        print('%s: wangangang' % self._pet_name)


"""
"""


class Animal(object):
    def __init__(self, name):
        self._name = name

    def run(self):
        print('%s is running' % self._name)


class Cat1(Animal):
    def run(self):
        print('%s is running and miao~miao~miao~' % self._name)

    def run_twice(animal):
        animal.run()


def main():
    pets = [Cat('小咪'), Dog('小天'), Cat('小琳')]
    for pet in pets:
        pet.make_voice()
    print(isinstance(pets[0], Cat))
    print(isinstance(pets[1], Dog))
    print(isinstance(pets[0], Pet))

    tiger = Animal('腦斧')
    tiger.run()
    cat = Cat1('貓姐')
    cat.run()
    cat.age = 16
    print(cat._name, 'is', cat.age, 'years old, and it\'s die')
    Cat1.run_twice(Cat1('xiaomao'))
    print(type(cat.age))
    print(isinstance(tiger, Animal))
    print(isinstance(cat, Pet))
    print(isinstance(pet, Pet))
    print(isinstance(pets[1], Pet))
    print(hasattr(Animal, 'self._name'))
    print(dir(Animal))
    print(hasattr(Animal, 'run'))
    print(getattr(Animal, 'run'))
    fn = getattr(Animal, 'run')
    print(fn)


if __name__ == "__main__":
    main()
