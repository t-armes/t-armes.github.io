# -*- coding: utf-8 -*-
"""Created on Mon Jan 29 18:19:09 2022"""
__author__ = "tom-christian armes"
__email__ = "tom-christian.armes@nmbu.no"

L = [
    [2015, 86343, 123],
    [2016, 93512, 125],
    [2017, 83935, 119],
    [2018, 91274, 128],
    [2019, 88935, 127],
    [2020, 95182, 132],
    ]

print('---------------------------------')
print('  Årstall  |   kr/bøssebærere   |')
print('---------------------------------')

index = 0
for X in L:
    print(f"    {X[0]}           {X[1]/X[2]:0.1f}")
    index += 1
    

print('---------------------------------')

print(f'{L[1][0]} ble det samlet inn mest penger per bøssebærer')


#a)
# ---------------------------------
#   Årstall  |   kr/bøssebærere   |
# ---------------------------------
#     2015           702.0
#     2016           748.1
#     2017           705.3
#     2018           713.1
#     2019           700.3
#     2020           721.1
# ---------------------------------

#b)
#2016 ble det samlet inn mest penger per bøssebærer

"""Created on 28.09.2022"""
__author__ = "Tom-Christian Armes"
__email__ = "tom-christian.armes@nmbu.no"


L = [
     ['Tore', 'Hansen'],
     ['Silje', 'Olavsen'],
     ['Aase', 'Lund'],
     ['Jens Petter', 'Oremo'],
     ['Tina', 'Kittelsen'],
     ['Dag', 'Paulsen'],
     ['Lena', 'Nilsen'],
     ['Karsten', 'Woll'],
     ['Ine', 'Ørstad'],
     ['Ravn', 'Havnås'],
     ['Jesper', 'Danberg']]

def name_check(first, family): #arg1 og arg2: "first" & "family"
    if first[0] == 'T':   #sjekker om fornavn begynner med T
        return True
    elif len (family) > 6:  #sjekker om etternavn har mer enn 6 tegn
        return True
    elif first == 'Ravn' and family == 'Havnås': #sjekker om navn er "Ravn Havnås"
        return True
    else:
        return False

for number, name in enumerate(L):
    if name_check(name[0], name[1]):
        print(f'{number + 1} {name[0]} {name[1]}')
      
#a) Output
# 1 Tore Hansen
# 2 Silje Olavsen
# 5 Tina Kittelsen
# 6 Dag Paulsen
# 10 Ravn Havnås
# 11 Jesper Danberg
