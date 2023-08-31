pyton telepitése:
python.org vagy windows store

ellenörzés hogy települt e: cmd python paranccsal nézzük meg

PyCharm vagy vscode használata.

print = console.log

python változók:

python adattípusok:

komment írása: #-el lehetséges

input bekérés:
input()

template literál használata: f string
pl (f "valalalalla" {valtozo} "blblblbb")

műveletek számokkal:

típusváltás:
#adatípus meghatározás
print(type(variable))

0, és az üres az hamis 

4 függvényt lehet haszálni:
int,float,bool,str kovertáláshoz
nem minden adatot lehet átkonverálni "11" ből lehet 11 szám

relációs és logikai operátorok:
and or használjuk illetve a not-ot

feltételek ellenőrzése if
: használjuk nem pedig {}
fontos a tabulátor ha az if része akkor beljebb irjuk
if (a == b):
    print("a és b egyenlő")

elif = else if
else

ha egy dolgot ellenőrzünk akkor if
ha több opció van akkor jön be az elif
a legvégén pedig ha egy feltétel se igaz akkor else használata

Listák:

logikailag egy halmazba tartozó elemeket lehet összegyüjteni egy listába
lista = tömb
ugyanugy index alapján keressük az elemeket
len függvény az megegyezik a length-el len(xy)

tuples-okot nem lehet változtatni így adjuk meg xy() nem lehet rajta változtatni a memóriában kisebb helyet foglal el. 

ciklusok:
while: addig fut amig valami be nem teljesül
alávonás használnak cammel case helyett
append függvény használatával rakunk a listába új elemet

függvények:
def kulcsó haználatával kell def = function

for ciklusok:
megadjuk hányszor fusson le
range() fügvényt használjuk
pl: for szorzo in range(1,11): # 1-10
    print(f"{szorzo } x {szorzando} = {szorzo * szorzando} ")

for ciklus listával és szövegadattal:
for gyumolcs in gyumolcsok:
    print(gyumolcs)

osztályok és objektumok:
osztály létrehozása
class xy:
def __init__(self, name, age)
    self.name = name
    self.age = age
ezután már csak példányosítani kell
fontos hogy a self az állandó

importálás exportálás:
ha egy mappába vannak akkor nem kell semmi csak annyi hogy import xy

modulok:
.isnumeric() szám e az adott érték?
beépített modulok pl:
import random, import time