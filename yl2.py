# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)
# P = 2 * Pi * r, S = Pi * r * r

from math import pi

r = int(input('Sisesta raadius: '))

p = 2 * pi * r
s = pi * r ** 2

print('Ümbermõõt on:', round(p, 3))
print('Pindala on:', round(s, 3))