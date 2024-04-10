#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__ (self, name, breed):
        if isinstance(name, str) and 1 <= len(name) <=25:
            self._name = name
        else:
            print('Name must be a string between 1 and 25 characters.')
    
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("The breed must be in the following list of dog breeds:")

