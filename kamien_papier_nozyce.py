import random
import time

x = 0 #wynik gracza
y = 0 #wynik kompa
while True:

    a = raw_input("Wybierz: kamien, papier, nozyce: ") #wybor gracza
    b = random.choice(['kamien', 'papier', 'nozyce']) #wybor kompa


    r = 'remis'
    w = 'Wygrales'
    p = 'Przegrales'

    if a == b:
        time.sleep(1)
        print('Twoj wybor to: ' + a )
        print('Wybor komputera to: ' + b)
        time.sleep(1)
        print(r)

    elif a == 'kamien' and b == 'nozyce':
        time.sleep(1)
        print('Twoj wybor to: ' + a )
        print('Wybor komputera to: ' + b)
        time.sleep(1)
        print(w)
        x += 1
    elif a == 'kamien' and b == 'papier':
        time.sleep(1)
        print('twoj wybor to: ' + a )
        print('Wybor komputera to: ' + b)
        time.sleep(1)
        print(p)
        y += 1
    elif a == 'papier' and b == 'kamien':
        time.sleep(1)
        print('twoj wybor to: ' + a )
        print('Wybor komputera to: ' + b)
        time.sleep(1)
        print(w)
        x += 1
    elif a == 'papier' and b == 'nozyce':
        time.sleep(1)
        print('twoj wybor to: ' + a )
        print('Wybor komputera to: ' + b)
        time.sleep(1)
        print(p)
        y += 1
    elif a == 'nozyce' and b == 'papier':
        time.sleep(1)
        print('twoj wybor to: ' + a )
        print('Wybor komputera to: ' + b)
        time.sleep(1)
        print(w)
        x += 1
    elif a == 'nozyce' and b == 'kamien':
        time.sleep(1)
        print('twoj wybor to: ' + a )
        print('Wybor komputera to: ' + b)
        time.sleep(1)
        print(p)
        y += 1
    print('wynik to ' + str(x) + ':' + str(y))
    czy_jeszcze_raz = raw_input("czy Chcesz zagrac jeszcze raz T/N: ")
    if czy_jeszcze_raz in ('T', 't'):
        print('to gramy dalej :) ')
    elif czy_jeszcze_raz in ('N', 'n'):
        print('do widzienia !')
        break
    else:
        czy_jeszcze_raz not in ('N', 'n' , 'T' 't')
        print('zla wartosc')
