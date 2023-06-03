# Operasi Logika atau Boolean

# not, or, and, xor

# NOT
print('======NOT=====')
a = False
c = not a
print('data boolean a = ', a)
print('-----------NOT')
print('data boolean c = ', c)

# OR
print('======OR=====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=',c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=',c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=',c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=',c)

# and
print('======and=====')
a = False
b = False
c = a and b
print(a, 'and', b, '=',c)
a = False
b = True
c = a and b
print(a, 'and', b, '=',c)
a = True
b = False
c = a and b
print(a, 'and', b, '=',c)
a = True
b = True
c = a and b
print(a, 'and', b, '=',c)

# ^
print('======^=====')
a = False
b = False
c = a ^ b
print(a, '^', b, '=',c)
a = False
b = True
c = a ^ b
print(a, '^', b, '=',c)
a = True
b = False
c = a ^ b
print(a, '^', b, '=',c)
a = True
b = True
c = a ^ b
print(a, '^', b, '=',c)