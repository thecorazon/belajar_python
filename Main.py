# Latihan  konversi  satuan temperatur

# Program konversi celcius ke satuan lain

print("\nPROGRAM KONVESI TEMPERATUR\n")

# celcius = float(input('Masukkan suhu dalam  celcius : '))
# print('suhu adalah ', celcius, ' Celcius')

# # raemur
# reamur = (4 / 5) * celcius
# print('suhu reamur adalah ', reamur, ' Reamur')

# # fahrenheit
# fahrenheit = ((9 / 5) * celcius) + 32
# print('suhu fahrenheit adalah ', fahrenheit, ' Fahrenheit')


# # kelvin
# kelvin = celcius + 273
# print('suhu kelvin adalah ', kelvin, ' Kelvin')

# ## TUGAS
# # fahrenheit ke kelvin

# fahrenheit = float(input('Masukkan suhu dalam fahrenheit: '))
# print('suhu fahrenheit adalah ', fahrenheit, ' fahrenheit')

# # ubah dulu fahrenheit ke celcius
# # celcius = (5 / 9) * (fahrenheit - 32)
# # print('suhu celcius adalah ', celcius, ' celcius')

# # lalu ubah celcius ke kelvin

# # # kelvin
# kelvin = (5 / 9) * (fahrenheit - 32) + 273
# print('suhu kelvin adalah ', kelvin, ' Kelvin')

#kelvin ke fahrenheit

kelvin = float(input('Masukkan suhu dalam kelvin: '))
print('suhu kelvin adalah ', kelvin, ' kelvin')

fahrenheit = ((kelvin - 273) * (9 / 5)) + 32
print('suhu fahrenheit adalah ', fahrenheit, ' fahrenheit')