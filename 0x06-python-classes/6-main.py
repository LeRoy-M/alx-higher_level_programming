#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
# -----------------------------
my_square01 = Square(3, "Position")
my_square01.my_print()

print("--")

my_square02 = Square(3, (1,))
my_square02.my_print()

print("--")

my_square03 = Square(3, (1, -3))
my_square03.my_print()

print("--")

my_square04 = Square(3, (1, "3"))
my_square04.my_print()

print("--")
