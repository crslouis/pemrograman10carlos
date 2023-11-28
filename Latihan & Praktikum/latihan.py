

b={'ari':'085267888','dina':'087677776'}
print('Daftar Kontak')
print('==============================')
print('    nama    |   nomor telepon')
print('==============================')
print('1.    ari   |   085267888','\n2.    dina    |   087677776')

# tamprintilkan kontak ari
print('\nTampilkan Kontak Ari')
print('1.    ari      |   ',b['ari'])
# Tambahkan riko ke kontak
print('\nMenambah Kontak Riko')
b['riko']='087654544'
print('1.   ari      |   ',b['ari'])
print('2.   dina     |   ',b['dina'])
print('3.   riko     |   ',b['riko'])
# Ubah Nomor dina ke nomor baru 
print('\nMengubah nomor Dina ke')
b['dina']='088999776'
print('1.   ari      |   ',b['ari'])
print('2.   dina     |   ',b['dina'])
print('3.   riko     |   ',b['riko'])
# Tampilkan semua nama
print('\nMenampilkan semua nama')
print(b.keys())
# Tampilkan semua nomor
print('\nMenampilkan semua nomor')
print(b.values())
# Tampilkan semua nama dan nomor
print('\nMenampilkan semua nama dan nomor')
print(b)
# Hapus kontak dina
print('\nMenghapus kontak dina')
del b['dina']
print(b,'\n')