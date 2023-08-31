szorzando = int(input("Add meg a szorzandót: "))

print()
print(f"*    A {szorzando} szorzótábla    *")
print()

for szorzo in range(1,11): # 1-10
    print(f"{szorzo } x {szorzando} = {szorzo * szorzando} ")