import random
from auto import AUTO

auto1 = AUTO('Toyota', 'Corolla', 2015, sebesseg_= 0, fogyasztas_= 3.7)
auto2 = AUTO('Porsche', '918', 2018, sebesseg_=0, fogyasztas_=5.5)
auto3 = AUTO('Audi', 'E-Tron GT', 2020, sebesseg_=0, fogyasztas_=6.8)
auto4 = AUTO('Ford', 'Focus', 1999, sebesseg_=0, fogyasztas_=5)
auto5 = AUTO('Volkswagen', 'Scirocco', 2008, sebesseg_=0, fogyasztas_=3.5)

autok = [auto1, auto2, auto3, auto4, auto5]
for auto in autok:
    print(auto)

for auto in autok:
    auto.gyorsit(random.randint(30, 150))

for auto in autok:
    print(auto.sebesseg)

autok_szama = len(autok)
osszeletkor = 0
for auto in autok:
    osszeletkor += 2026 - auto.gyartasiev

atlageletkor = osszeletkor/autok_szama
print(atlageletkor)

autokeletkora = []
for auto in autok:
    kor = 2026-auto.gyartasiev
    autokeletkora.append(kor)

legidosebb_auto = autokeletkora.index(max(autokeletkora))
print(f'A legidősebb autó eletkora {max(autokeletkora)} {autok[legidosebb_auto]}')

 #c version
gyartasi_evek = [auto.gyartasiev for auto in autok]
for auto in autok:
    if auto.gyartasiev == min(gyartasi_evek):
        print(f'A legidosebb auto = {auto}')

auto1.utazik(1000)
auto1.tankol(10)
print(auto1)