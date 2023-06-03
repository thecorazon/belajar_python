# Casting Tipe Data
# merubah satu tipe ke tipe lain
# tipe data {int, float, str, bool}


## INTEGER
print("+++++++Integer++++++")
data_int = 9
print("data = ", data_int, " tipe = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # false hanya jika nilai int = 0


print("data = ", data_float, " tipe = ", type(data_float))
print("data = ", data_str, " tipe = ", type(data_str))
print("data = ", data_bool, " tipe = ", type(data_bool))

print('\n')

## FLOAT
print("+++++++Float++++++")
data_float = 9.8
print("data = ", data_float, " tipe = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # false hanya jika nilai float = 0

print("data = ", data_int, " tipe = ", type(data_int))
print("data = ", data_str, " tipe = ", type(data_str))
print("data = ", data_bool, " tipe = ", type(data_bool))

print('\n')

## bool
print("+++++++bool++++++")
data_bool = False
print("data = ", data_bool, " tipe = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # false hanya jika nilai float = 0

print("data = ", data_int, " tipe = ", type(data_int))
print("data = ", data_str, " tipe = ", type(data_str))
print("data = ", data_float, " tipe = ", type(data_float))

print('\n')

## str
print("+++++++str++++++")
data_str = "";
print("data = ", data_str, " tipe = ", type(data_str))

# data_int = int(data_str) # string harus angka
# data_float = float(data_str) # string harus angka
data_bool = bool(data_str) # hanya bernilai false jika string kosong -> ""

# print("data = ", data_int, " tipe = ", type(data_int))
# print("data = ", data_float, " tipe = ", type(data_float))
print("data = ", data_bool, " tipe = ", type(data_bool))