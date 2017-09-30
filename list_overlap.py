#!/usr/bin/python3
import random

a = [random.randrange(10) for i in range(10)]
b = [random.randrange(10) for i in range(10)]

anb = []
anb += (i for i in a if i in b and i not in anb)

print (a, '\n', b , '\n', anb)
