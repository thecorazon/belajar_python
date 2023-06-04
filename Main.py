
data = 'ini adalah string'
print(data)
print(type(data))



# 1. Cara membuat string

'''
1. Menggunakan single quote '...'
1. Menggunakan double quote "..."

'''

data = 'menggunakan single quote'
print(data)

data = 'menggunakan double quote'
print(data)

print('"Halo, Apa Kabar?"')
print("'Halo, Apa Kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \
# Membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')


# backslash
print("C:\\user\\Ucup")

# tab
print('ucup\t\t\totong, jauhan')
#backline
print("ucup\botong")

#newline
print('baris pertama, \nbaris kedua') # LF -> line feed -> unix macos, linux
print('baris pertama, \rbaris kedua') # CR -> carriage retun -> os dulu
print('baris pertama, \r\nbaris kedua') #CRLF -> windows


#3. string literal atau raw

# hati-hati
print('C:\new folder') #akan salah pathnya

#menggunakan raw string
print(r'C:\new folder')

# multiline liteal string
print("""
Nama : Yohanes
Kelas : 7 smp
""")

# multiline literal string dan raw

print(r"""
Nama : Yohanes
Kelas : 7 smp\covid\19
website : www.yohan.com/newId
""")
