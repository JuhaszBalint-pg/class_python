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