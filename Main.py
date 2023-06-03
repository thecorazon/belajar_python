# tipe data

# angka satuan (integer)
data_integer = 100000
print(type(data_integer))
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# float(desimal)
data_float = 1.7
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# string(kumpulan karakter)
data_string = "Kidomaru 10"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# boolean (true/false)
data_bool = False
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))



## tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data bahasa c

from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))