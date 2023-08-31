number = 0

while True:
    print(f"A szám jelenlegi értéke {number}")
    bevitel = input("mennyivel változtassuk a számot? [k = kilépés] ")
    if bevitel == "k":
        break
    else:
        number += int(bevitel)
print(f"A szám végső értéke {number}")