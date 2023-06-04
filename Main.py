# Operasi dapat dilakukan dengan peningkatan
# operasi ditambah dengan assiment

a= 5 # adalah assigment
print('nilai a =', a)


a += 1 # artinya a = a + 1
print('nilai a += 1, nilai a menjadi ', a)

a -= 2 # artinya a = a - 2
print('nilai a -= 2, nilai a menjadi ', a)

a *= 5 # artinya a = a * 5
print('nilai a *= 5, nilai a menjadi ', a)


a /= 3 # artinya a = a / 3
print('nilai a /= 3, nilai a menjadi ', a)


b = 10 
print('\nnilai b = ',b)
b %= 3
print('nilai b %= 3, nilai b menjadi ', b)

b = 10 
print('\nnilai b = ',b)
b //= 3
print('nilai b //= 3, nilai b menjadi ', b)


a = 5
print('\nnilai a = ',a)
a **= 3
print('nilai a **= 3, nilai a menjadi ', a)



# OPERASI BITWISE
# OR
c = True
print('\nnilai c = ', c)
c |= False
print('nilai c |= False, nilai c menjadi ', c)
c = False
c |= False
print('nilai c |= False, nilai c menjadi ', c)


# AND
c = True
print('\nnilai c = ', c)
c &= False
print('nilai c &= False, nilai c menjadi ', c)
c = True
c &= True
print('nilai c &= True, nilai c menjadi ', c)

# XOR
c = True
print('\nnilai c = ', c)
c ^= False
print('nilai c ^= False, nilai c menjadi ', c)
c = True
c ^= True
print('nilai c ^= True, nilai c menjadi ', c)

# geser geser
d = 0b1000
print('\nnilai d = ',format(d,'04b'))
#kanan
d >>= 2
print('\nnilai d = ',format(d,'04b'))
#kiri
d <<= 1
print('\nnilai d = ',format(d,'04b'))