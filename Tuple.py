# coding: utf-8

Person1 = ("Gaël", "Monlouis", 1997)

(FirstName, LastName, BirthYear) = Person1
person2 = FirstName, LastName, BirthYear

print(f"{FirstName} {LastName} est né(e) en {BirthYear}, il a donc {2021-BirthYear} ans")

print()

a = "Bonjour"
b = "Au revoir"
# c = a
# a = b
# b = c
(a, b) = (b, a)
print(a,b)