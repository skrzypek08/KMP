# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:31:05 2021

@author: Someone
"""
import os

tekst = "LOREM IPSUM DOLOR SIT AMET"
wzor = "SIT"

def sprawdz_plik(plik, tekst, wzor):
    if os.path.exists(plik):
        if os.stat(plik).st_size == 0:
            with open(plik, 'a') as f:
                f.write(f'Wynik dla wzorca: {wzor} i tekstu {tekst}')
        else:
            with open(plik, 'a') as f:
                f.write(f'\n\nWynik dla wzorca: {wzor} i tekstu {tekst}')
    else:
        with open(plik, 'a') as f:
            f.write(f'Wynik dla wzorca: {wzor} i tekstu {tekst}')

def KMP_prefix(wzor):
    m = len(wzor)
    i = 1
    j = 0
    prefix = [0]
    
    while len(prefix) < m:
        if wzor[j] == wzor[i]:
            prefix.append(j + 1)
            i += 1
            j += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix.append(0)
                i += 1            
    return prefix
                
def KMP(tekst, wzor):
    j = 0
    i = 0
    T = KMP_prefix(wzor)
    ile_razy = 0
    sprawdz_plik('wyniki_alg.txt', tekst, wzor)
    
    while i != len(tekst):
        if wzor[j] == tekst[i]:
            j += 1
            i += 1
        if j == len(wzor):
            print ("Znaleziono wzorzec na indeksie nr " + str(i - j)) #a complete match
            j = T[j - 1]
            ile_razy += 1
            with open('wyniki_alg.txt', 'a') as f:
                f.write("\nZnaleziono wzorzec na indeksie nr " + str(i - j))
        elif i < len(tekst) and wzor[j] != tekst[i]:
            if j != 0:
                j = T[j - 1]
            else:
                i += 1
    print(f'Wzorzec pojawił się {ile_razy} raz/y')
    with open('wyniki_alg.txt', 'a') as f:
                f.write(f'\nWzorzec pojawił się {ile_razy} raz/y')

print(KMP_prefix(wzor))
KMP(tekst, wzor)