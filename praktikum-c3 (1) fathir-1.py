
nama="Fathir Muhammad"
nim="231031077"
meet="Praktikum 3(string)"
prodi="Sistem Informasi"
email="fathirmuhammad1601@gmail.com"
ttl="Pinrang, 16-Januari-2005"
alamat="Barru"
asal="Barru"
hobi="Mendengarkan Musik"
tinggi="184"
print("-"*110)
print(nama.upper().center(100))

str1= "231031077"
a= str1.center(100)
print(a)
print()
print()
str1= "Praktikum 3(String)"
a= str1.rjust(110)
print(a)
str1= "Sistem Informasi(c)"
a= str1.rjust(110)
print(a)
str1= "fathirmuhammad1601@gmail.com"
a= str1.rjust(110)
print(a)
print("-"*110)
print()
print()


print(f'''\tHalo, nama saya {nama} dengan NIM {nim} dari prodi {prodi}, ini adalah file {meet}. Terima Kasih''')
print(f''' Biodata Saya,
Nama\t: {nama}
Nim\t: {nim}
Prodi\t:{prodi}
TTL\t: {ttl}
Alamat\t:{alamat}
Asal\t:{asal}
Hobi\t:{hobi}
Tinggi\t:{tinggi} cm
''')
print()
print()
# Stat1: Issac duFort Frankel Sir
stat1 = 'duFort Frankel Sir Issac'
result1 = stat1.split()
result1 = result1[-1] + ' ' + ' '.join(result1[:-1])
print(result1)

# Stat2: d F S Issac
stat2 = 'duFort Frankel Sir Issac'
result2 = stat2.split()
result2 = ' '.join([word[0] for word in result2]) + ' ' + result2[-1]
print(result2)

# Stat3: duFort F S I
stat3 = 'duFort Frankel Sir Issac'
result3 = stat3.split()
result3 = ' '.join([word if word == 'duFort' else word[0] for word in result3])
print(result3)

# Stat4: I duFort Frankel Sir
stat4 = 'duFort Frankel Sir Issac'
result4 = stat4.split()
result4 = result4[-1] + ' ' + ' '.join(result4[:-1])
result4 = result4[0] + ' ' + result4[1:]
print(result4)

# Stat5: Issac d F S
stat5 = 'duFort Frankel Sir Issac'
result5 = stat5.split()
result5 = result5[-1] + ' ' + ' '.join(result5[:-1])
result5 = result5[0] + ' ' + result5[1:]
print(result5)

# Stat6: ISSAC D F S
stat6 = 'duFort Frankel Sir Issac'
result6 = stat6.split()
result6 = result6[-1].upper() + ' ' + ' '.join([word[0].upper() for word in result6[:-1]])
print(result6)

# Stat7: duFort Frankel Sir Issac
stat7 = '#duFort Frankel Sir Issac$'
result7 = ''.join([c for c in stat7 if c.isalpha() or c.isspace()])
print(result7)

# Stat8: duFort Frankel Sir Issac
stat8 = '#duFort-Frankel-Sir-Issac$'
result8 = ''.join([c for c in stat8 if c.isalpha() or c.isspace() or c == '-'])
print(result8)

# Stat9: duFort Frankel Sir Issac
stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
result9 = ''.join([c for c in stat9 if c.isalpha() or c.isspace()])
print(result9)

# Stat10: DUFORT FRANKEL SIR ISSAC
stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
import re
stat10 = re.findall(r'\w+', stat10)
hasil = ' '.join(stat10.upper() for stat10 in stat10)
print(hasil)
