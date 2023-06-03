## KOMPARASI (Membandingkan nilai)

# Setiap hasil dari komparasi adalah boolean

# >,<,>=,<=,=,!=,is,is not

a = 4
b = 2

# Lebih besar dari
hasil = a > 3
print(a, '>', 3, '=', hasil)


# Sama dengan 

hasil = a == 4
print(a, '==', 4, '=', hasil)

#  Tidaj Sama dengan 

hasil = a != 4
print(a, '!=', 4, '=', hasil)

# is sebagai komparasi objek
x = 5 # assigment membuat objek 
y = 5
print('nilai x = ', x, 'id = ', hex(id(x)))
print('nilai y = ', y, 'id = ', hex(id(y)))

hasil = x is not y
print('x is y = ', hasil)

# is sebagai komparasi objek
x = 5 # assigment membuat objek 
y = 6
print('nilai x = ', x, 'id = ', hex(id(x)))
print('nilai y = ', y, 'id = ', hex(id(y)))

hasil = x is  not y
print('x is y = ', hasil)