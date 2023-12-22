data = {'nama'     : 'Fathir Muhammad',
        'kelas'    : 'SI23C',
        'umur'     : '18 tahun',
        'anak ke'  : 'Pertama',
        'nim'      : '231031077',
        'jurusan'  : 'sains',
        'prodi'    : 'sistem informasi',
        'semester' : 'ganjil',
        'status'   : 'aktif',
        'angkatan' : '2023',
        'kota'     : 'barru',
        'alamat'   : 'jalan latanring',
        'hobi'     : 'mendegarkan musik',
       }

print(data)
print(len(data))
print()

#Mengakses Dictionary
print(data.get('jurusan'))
print(data['semester'])
print()

#mengakses data
print(data['nama'])
print(data['nim'])
print(data['umur'])
print(data['kelas'])
print(data['prodi'])
print(data['angkatan'])
print(data['alamat'])
print(data['hobi'])
print()

#mengupdate dan menambah data
data['hobi'] = 'belajar'
print(data)
print()
# Menghapus data
del data['anak ke']
print(data)
print()
#Nested Dictionary

bio_data = {'nama'     : 'Fathir Muhammad',
            'nim'      : '231031077',
            'nilai'    : [98,96,95,99],
            'favorite' : {'makanan' : 'gado gado',
                          'minuman' : 'susu',
                          'hobi'    : 'mendegarkan musik',
                          'warna'   : 'biru'
                         }
           }
print(bio_data)
print()
print(bio_data['favorite']['warna'])
print(bio_data['favorite']['minuman'])
print(bio_data['favorite']['makanan'])
print(bio_data['nilai'][3])
print()

print(bio_data['favorite'].keys()) # melihat seluruh keys
print()

bio_data['favorite']['belajar'] = 'semua hal'
print(bio_data['favorite'].values()) # melihat seluruh nilai/value