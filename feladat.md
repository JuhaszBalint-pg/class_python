2. feladatrész – Az autó „viselkedése” (metódusok)
Cél: Megérteni, hogyan adunk az osztályhoz metódusokat, amelyek az objektum állapotát (pl. sebesség) megváltoztatják.

1. Új attribútum hozzáadása

Bővítsd az Auto osztályt egy új attribútummal:
sebesseg – ez legyen az aktuális sebesség km/h-ban.
Az __init__ metódusban állítsd be az alapértelmezett sebességet:
Kezdő érték: 0.
2. gyorsit metódus

Készíts egy gyorsit nevű metódust az Auto osztályban.
A metódus kapjon egy paramétert, pl. ertek, ami azt mondja meg, hány km/h-val nőjön a sebesség.
Növeld a sebesseg értékét ezzel a paraméterrel.
Opcionálisan: ne engedd, hogy a sebesség 200 km/h fölé menjen (ha fölé menne, állítsd 200-ra).
3. fekez metódus

Készíts egy fekez nevű metódust az Auto osztályban.
A metódus szintén kapjon egy paramétert, pl. ertek, ami azt mondja meg, hány km/h-val csökkenjen a sebesség.
Csökkentsd a sebesseg értékét ezzel a paraméterrel.
Ne engedd, hogy a sebesség 0 km/h alá menjen (ha az alá esne, állítsd 0-ra).
4. __str__ frissítése

Egészítsd ki a __str__ metódust úgy, hogy az aktuális sebességet is megjelenítse, pl.:
"Toyota Corolla (2015), sebesség: 50 km/h"
5. Tesztelés a main.py-ben

A main.py-ban válassz ki egy autót (pl. auto_1), és csináld a következőket:
Írd ki az autót (pl. print(auto_1)).
Hívd meg rajta a gyorsit(30) metódust.
Írd ki újra az autót.
Hívd meg rajta a fekez(10) metódust.
Írd ki megint az autót.
Figyeld meg, hogyan változik az autó sebessége a kiírásban.





3. feladatrész – Több autó kezelése listában, egyszerű statisztikák
Cél: Megtanulni, hogyan tudunk több objektumot együtt kezelni (lista), és hogyan tudunk ezekről egyszerű statisztikákat készíteni.

1. Több autó létrehozása

A main.py fájlban hozz létre legalább 4–5 különböző autót (különböző márka, típus, gyártási év).
Tedd ezeket egy listába, pl. autok = [auto_1, auto_2, auto_3, auto_4].
2. Bejárás for ciklussal

for ciklussal járd be az autók listáját, és írd ki mindegyik autót!
3. Gyorsítás minden autóra

A main.py fájlban egy újabb for ciklusban hívd meg minden autóra a gyorsit() metódust random értékkel:
pl. 10 és 50 közötti véletlenszerű számmal.
Utána írd ki újra az összes autót (lásd, hogy mindegyik sebessége megnőtt, de különböző értékkel).
4. Egyszerű statisztika – átlagéletkor

Számold ki, hány évesek az autók
Számold ki az autók átlagéletkorát (összeg / darabszám).
Írd ki a képernyőre, pl.:
Az autók átlagéletkora: 12.5 év
5. Plusz (haladóknak): legöregebb autó

Keresd meg, melyik a legöregebb autó a listában.
Írd ki: melyik márka, típus, hány éves.


4. feladatrész – Üzemanyag, fogyasztás
Cél: Megtanulni, hogyan kezelünk több attribútumot együtt (üzemanyag, fogyasztás), és hogyan olvasunk be adatok fájlból.

1. Új attribútumok hozzáadása

Bővítsd az Auto osztályt két új attribútummal:
uzemanyag – az aktuális üzemanyag mennyisége literben (pl. 50.0).
fogyasztas – az autó fogyasztása liter/100 km-ben (pl. 7.5).
Az __init__ metódusban állítsd be az alapértelmezett értékeket:
uzemanyag: kezdő érték legyen 50.0 liter (teli tank).
fogyasztas: legyen egy paraméter, amit megadhatsz az autó létrehozásakor (pl. 7.5).
2. tankol metódus

Készíts egy tankol nevű metódust az Auto osztályban.
A metódus kapjon egy paramétert, pl. mennyiseg, ami azt mondja meg, hány litert tankolunk.
Növeld az uzemanyag értékét ezzel a paraméterrel.
Opcionálisan: ne engedd, hogy az üzemanyag 50 liter fölé menjen (ha fölé menne, állítsd 50-re – ez a tank maximális kapacitása).
3. utazik metódus

Készíts egy utazik nevű metódust az Auto osztályban.
A metódus kapjon egy paramétert, pl. km, ami azt mondja meg, hány kilométert utazunk.
Számold ki, mennyi üzemanyagot fogyasztunk: fogyasztott = (km / 100) * self.fogyasztas
Csökkentsd az uzemanyag értékét a fogyasztott mennyiséggel.
Ne engedd, hogy az üzemanyag 0 liter alá menjen (ha az alá esne, állítsd 0-ra).
Opcionálisan: ha az üzemanyag elfogy, írj ki egy üzenetet, pl. "Nincs elég üzemanyag!"
4. __str__ frissítése

Egészítsd ki a __str__ metódust úgy, hogy az üzemanyag mennyiségét is megjelenítse, pl.:
"Toyota Corolla (2015), sebesség: 50 km/h, üzemanyag: 45.2 l"
5. Tesztelés a main.py-ban

Hozz létre egy új autót fogyasztással, pl. auto_6 = Auto("BMW", "320d", 2019, 6.5) (ha a fogyasztás paraméter az __init__-ben a 4. helyen van).
Írd ki az autót.
Hívd meg rajta a utazik(200) metódust (200 km utazás).
Írd ki újra az autót (lásd, hogy csökkent az üzemanyag).
Hívd meg rajta a tankol(20) metódust.
Írd ki megint az autót (lásd, hogy nőtt az üzemanyag).



5.: Autók beolvasása fájlból
1. Fájl létrehozása

Hozz létre egy új fájlt az adatok mappában autok.txt néven.
Írd bele az alábbi autók adatait, soronként egy autó, vesszővel elválasztva:
Formátum: márka,típus,gyártási_év,fogyasztás
Példa:
márka,típus,gyártási_év,fogyasztás
Toyota,Corolla,2015,7.2
Ford,Focus,2018,6.8
Renault,Megane,2014,7.5
Seat,Leon,2019,6.5
BMW,320d,2019,6.5
Audi,A4,2017,7.8
Volkswagen,Golf,2016,6.9
2. Fájl beolvasása a fajlbeolvasas.py-ban

Olvasd be az autok.txt fájlt.
Használd a with open("autok.txt", "r", encoding="utf-8") as f: konstrukciót.
Soronként olvasd be a fájlt, és minden sorból hozz létre egy Auto objektumot.
Tipp: a gyártási év és fogyasztás szám, ezért használd a int() és float() függvényeket.
3. Listába rendezés és kiírás

Tedd az új autókat egy listába (pl. autok_fajlbol = []).
Járd be a listát for ciklussal, és írd ki mindegyik autót.
4. Opcionális: üzemanyag ellenőrzés

Minden autó kezdjen 50 liter üzemanyaggal.
Minden autó utazzon egy random távolságot (pl. 100–500 km között).
Utána írd ki, melyik autóknak van még üzemanyaguk, és melyiknek nincs.