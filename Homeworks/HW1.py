# -*- coding: utf-8 -*-
"""HW1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qL3uQTHUQ6nqkUmWvigcKAEbwV-gL7i6
"""

a = [23, 93, 31, 67, 33, 17, 95, 45, 91, 89]
b = [74, 66, 42, 34, 54, 46, 98, 92, 82, 44]
c = []
c.extend(a)
c.extend(b)
print("Liste:", c )
c.sort()
print("Küçükten büyüğe sıralanmış liste:", c)
print("Liste eleman sayısı:", len(c))
for q in range (len(c)):
  c[q] *= 2
print("Listedeki değerlerin 2 ile çarpılmış hali:", c)
