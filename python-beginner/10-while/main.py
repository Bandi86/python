number = 0

while number < 100:
    print(f"A szám értéke: {number}")
    number += int(input("mennyivel növeljük?"))
print(f"A szám végső értéke {number}")