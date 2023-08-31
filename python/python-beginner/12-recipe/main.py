osszetevok = []
uj_osszetevo = ""

print("Összetevők megadása - kilépéshez haználd a kilépés szót")

while uj_osszetevo != "kilépés":
    uj_osszetevo = input("Adj meg egy összetevőt: ")
    
    if uj_osszetevo != "" and uj_osszetevo != "kilépés":
        osszetevok.append(uj_osszetevo)
        print(osszetevok)
        
print()
print("végső összetevők listája")
print(osszetevok)