#test
waga = float (input('podaj swoja wage (kg) '))
wzrost = input('podaj swoj wzrost (cm) ')
print("twoje BMI to: ")
bmi = ((waga/((wzrost)**2))*10000)
print bmi
if(bmi< 16.0):
    print('wyglodzenie')
elif( bmi<16.99):
    print('wychudzenie')
elif( bmi<18.49):
    print('niedowaga')
elif( bmi<24.99):
    print('waga prawidlowa')
elif( bmi<29.99):
    print('nadwaga')
elif( bmi<34.99):
    print('I stopien otylosci')
elif( bmi<39.99):
    print('II stopien otylosci')
else:
    print('otylosc skrajna')
