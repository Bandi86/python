a = 10
b = 20

if (a == b):
    print("a és b egyenlő")
    
print("hello")

#fh ki akar a lépni?
#3 lehetőség lesz
valasz = input("kilépés a fiókból? [igen/nem] ")    

if valasz == "igen":
    print("kilépés")
elif valasz == "nem":
    print("maradás")
else:
    print("érvénytelen válasz")          