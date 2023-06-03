# Operasi Aritmatika

a = 10
b = 3

# Operasi Penjumlahan +
hasil = a + b
print(a, " + ", b, " = ", hasil)

# Operasi Pengurangan - 
hasil = a - b
print(a, " - ", b, " = ", hasil)

# Operasi Perkalian *
hasil = a * b
print(a, " * ", b, " = ", hasil)

# Operasi Pembagian /
hasil = a / b
print(a, " / ", b, " = ", hasil)

# Operasi eksponen (pangkat) **
hasil = a ** b
print(a, " ** ", b, " = ", hasil)

# Operasi modulus (sisa bagi) %
hasil = a % b
print(a, " % ", b, " = ", hasil)

# Operasi flow division (kebalikan modulus) //
hasil = a // b
print(a, " // ", b, " = ", hasil)


## prioritas operasi

x = 3
y = 2
z = 4
hasil = x ** y * (z + x) / y - y % z //x
print(x,'**',y,'*(',z,'+',x,')/',y,'-',y,'%',z,'//',x)
print(hasil)


hasil = x + y * z
print(x,'+',y,'*',z,'= ', hasil)


## Urutan prioritas
# ()
# **
# *, /, %, //
# +, -