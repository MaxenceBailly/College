import random

a = 0
b = 100

i = 0
while i == 0:
    nb1 = random.randint(a, b)
    nb2 = random.randint(a, b)

    entry = eval(input(f"Calcul {nb1} x {nb2} >>"))
    if entry == nb1*nb2:
        print(f"Bravo cela fait bien {nb1*nb2}")
    else:
        print(f"Zut t'es trop nul ça fait pas {entry} mais ça fait {nb1*nb2}")
