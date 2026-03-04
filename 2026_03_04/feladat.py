import random
from auto import AUTO

autok = []
with open('adatok/autok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        if len(adatok) >= 4:
            marka, tipus, gyartasi_ev, fogyasztas = adatok
            auto = AUTO(marka, tipus, int(gyartasi_ev), float(fogyasztas))
            autok.append(auto)

for auto in autok:
    print(auto)

for auto in autok:
    auto.utazik(random.randrange(100, 501))

    if elfogyasztott_uzemanyag/uzemanyag > 0: