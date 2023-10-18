youtube link: https://www.youtube.com/watch?v=0sOvCWFmrtA
repo link: https://github.com/Sanjeev-Thiyagarajan/fastapi-course

# NOTES

django, flask, fastapi framework itt a fastapi-t fogjuk használni
fast api automatikusan elkészíti az api dokumentációt.

telepítés macbookra:
telepítés windowsra:

virtual environments
ha két különböző verzió számú projekt így tudunk 2 olyan projektet csinálni ami más verziószámot használ így mindkettőt tudjuk futtatni

https://www.mingw-w64.org/
https://learnpython.com/blog/python-requirements-file/

hogy csináljunk meg: python -m venv venv
.\venv\Scripts\python.exe
ezt mindig be kell tallózni amikor a projekten dolgozunk

can reinstall all of the needed packages with the command:
pip install -r requirements.txt

./venv/Scripts/activate.bat
source venv/Scripts/activate /bash

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

update:
put methódust használva updateljük a postot jelen esetben

dokumentáció automatikus készítése fast apival
http://localhost:8000/docs swagger ui
http://localhost:8000/redoc redoc ezt is lehet haszálni 

app folder kell csinálni egy __init__.py file-t
uvicorn app.main:app --reload

Database hozzáadása a projekthez:
DBMS rendszert használjuk

Ebben a projektben PostgreSQL-fogunk használni

installáció:
alapértelmezetten létre fog hozni egy db-t postgres néven
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
PORT alap 5432

táblákkal fogounk dolgozni mint users products purchases
ezek kapcsolatban fognak állni egymással

ezen belül lesznek sorok és oszlopok

adattípusok fontosak: int,decimal varchar,text boolean array
Primary key-t kell definálni ami definiálja a hovatartozást csak egyet lehet használni
unique használata
null használata by default
port 5433 ?

PG ADMIN:
Séma table
id-t a serial tulajdonássgal fog automatikusan generálni
F6 al el tudjuk menteni a kézzel felvitt adatokat
timestamp készítése:
timestamp with timezone default értéke NOW() lesz
query tool jobb klikk az adatbázis nevére

SELECT * from products; mindent kilistáz a products táblából
F5el lehet frissiteni a kérések között
nem számit a kis és nagybetű de jobb ha a sql parancsokat nagy betüvel írjuk

rename colum:
SELECT id AS products_id FROM products; // AS keyworddal lehet megtenni

10es id kiválasztása: SELECT * FROM products WHERE id = 10;

névre keresés: SELECT * FROM products WHERE name = 'Tv';

operátorok haználata kisebb nagyobb jeleket kell csak hozzáadni név érték vagy lehet használni a != operátort

AND kulcsszo hasznalataval kapcsolhatjuk ossze a lekerdezest
IN operator pl:
SELECT * FROM xy WHERE id IN (1,2,3)

LIKE operator:
SELECT * FROM xy WHERE xy name LIKE 'tv%'
lehet kombinalni a NOT-al 

orderezes:
ORDER BY defaultban ASC 
DESC nagytol kicsire
recent products kerese: 
ORDER BY created_at DESC

LIMIT
OFFSET

uj letrehozasa INSERT INTO products (name, price, stock) VALUES ('tortila', 4, 1000), RETURNING *

returninggel adjuk vissza a letrehozott itemet

delete entries 

DELETE FROM products WHERE id = 10 RETURNING *

tobb elem torlese:

DELETE FROM products WHERE stock = 0

update:

UPDATE products SET name = 'viragos tortila', price = 40 WHERE id = 25 RETURNING *

tobb elem frissitese: 

UPDATE products SET is_sale = true WHERE id = 15 RETURNING *

psycopg postgre sql database adapter for python
https://www.psycopg.org/docs/

pip install pscyopg2
pip install psycopg2-binary

import psycopg2
from psycopg2.extras import RealDictCursor

ezutan try:
conn = psycopg2.connect()
parameterek:
host, database, user, password, 
cursor_factory=RealDictCursor

cursor = conn.cursor()

import time
time.sleep(2) // 2 seckent ujra probalkozik a server inditassal

4:10