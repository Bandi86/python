gyumolcsok = ["alma", "körte", "szilva", "barack"]

#nyomtassuk ki egyenként a gyümölcsöket

for gyumolcs in gyumolcsok:
    print(gyumolcs)

#az első elem le lesz bontva vagy alma
for betu in gyumolcsok[0]:
    print(betu)
    
for gyumolcs in gyumolcsok:
    for betu in gyumolcs:
        print(betu)
    print()            