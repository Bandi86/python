youtube link: https://www.youtube.com/watch?v=0sOvCWFmrtA
repo link: https://github.com/Sanjeev-Thiyagarajan/fastapi-course

# NOTES

django, flask, fastapi framework itt a fastapi-t fogjuk használni
fast api automatikusan elkészíti az api dokumentációt.

telepítés macbookra:
telepítés windowsra:

virtual environments
ha két különböző verzió számú projekt így tudunk 2 olyan projektet csinálni ami más verziószámot használ így mindkettőt tudjuk futtatni

hogy csináljunk meg: py -m venv venv
.\venv\Scripts\python.exe
ezt mindig be kell tallózni amikor a projekten dolgozunk

./venv/Scripts/activate.bat

https://fastapi.tiangolo.com/
pip install fastapi[all]

pip freeze megmutatja milyen packokat tettük fel
a lib mappába teszi fel

from fastapi import FastAPI
app = FastAPI()

Ezután indítsuk el a szervert
uvicorn main:app
uvicorn main:app --reload ezzel mindig ujra indul a szerver úgy mint a nodemonnál

automatikusan átalakít json-re
dekorator fastapi @app.get("/")

mindig csak az első get fog lefutni ha több lenne ugyanarra az utvonalra
postman: a%SRJNe@_Y8t?VF

POST METHOD:

használjuk a beépített Body-t from fastapi.params import Body
aztán adjuk a függvény paraméterbe payload: dict = Body(...)

Miért van szükséges Schémára?
- ne kelljen minden értéket figyelni a body-ban
- a kliens bármit küldhet
- az adat nem validtált
- jobb ha a kliens olyat adatot küld amit a sémában mi definiálunk meg

Pydantic használata:
https://docs.pydantic.dev/latest/
ezzel fogjuk definiálni a sémát de nincs köze a fast apihoz

from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str

 ezután már használhatjuk a sémát.

 opcionális adat készítése:

 from typing import Optional
 rating: Optional[int] = None

 model_dump() használata
 Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

 random szám konverter:
 from random import randrange
 randrange(0, 100)

figyelni kell arra hogy ahol számot várunk ott alakítsuk át a stringet számmá 

validáció paraméterben adjuk meg hogy id: int

fontos az api route sorrendje mert nem mindegy melyik van előrébb ha a metódus és az utvonal ugyanaz

mi van akkor ha olyan id-ra keresek ami nem létezik akkor nullát fog visszaadni le kell kezelni

from fastapi import Response

from fastapi import status
használata pl:
 response.status_code = status.HTTP_404_NOT_FOUND

importálni kell a fastapi-ból
 raise HTTPException()
 két paraméter az első a status code mi legyen aztán a detail mint string válasz

 mindig amikor készítünk valamit mondjuk postot akkor az 201 kóddal lesz pl:
 @app.post("/posts", status_code=status.HTTP_201_CREATED)

 poszt törlése:
pop fügvénnyel ki tudjuk törölni a tömbből
204 statust kell vissza adni
le kell azt is kezelni amikor olyan id-t ad meg törlésre ami nem létezik
egy egyszerű if-el le kezeljük hogy ha az index none akkor dobjon egy exceptiont ahogy előzőleg

2:10