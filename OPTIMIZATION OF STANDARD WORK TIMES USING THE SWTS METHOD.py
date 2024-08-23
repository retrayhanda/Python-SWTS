class Program:
      def __init__(self):
            self.kegiatan_utama_list = [
                  "Pemarutan Kelapa",
                  "Penggilingan Daging",
                  "Pemerasan Santan"
            ]
            self.rincian_kegiatan_list = [
                  "Pengukuran",
                  "Pemotongan",
                  "Pengeboran",
                  "Pengelasan",
                  "Penghalusan",
                  "Pengeplongan",
                  "Pengecatan",
                  "Perakitan",
                  "Inspeksi"
            ]
            self.total_waktu_kerja = 0
            self.upah_per_hari = 0
            self.kegiatan = []

      def cover(self):
            data = (
                  'OPTIMASI WAKTU STANDAR KERJA MENGGUNAKAN METODE SWTS',
                  '',
                  'OLEH:',
                  '',
                  '  RAHMAD HARET RAYHANDA',
            )
            print(92 * '=')
            print('|{:^90}|'.format('------   OPTIMASI WAKTU STANDAR KERJA MENGGUNAKAN METODE SWTS   ------'))
            print(92 * '=')
            for line in data:
                  print('|{:^90}|'.format(line))
            print(92 * '=')

      def explain(self):
            print(92 * '-')
            print('{:^90}'.format('Program ini adalah program yang bertujuan untuk menentukan waktu standar kerja dan'))
            print('{:^90}'.format('perkiraan jumlah pekerja pada perusahaan UD Rahmat serta program ini '))
            print('{:^90}'.format('juga dirancang untuk meramalproduksi perusahaan untuk 12 bulan ke depannya'))
            print('')
            print('{:^90}'.format('Data yang diinputkan:'))
            print('{:^90}'.format('1. Waktu siklus untuk setiap kegiatan'))
            print('{:^90}'.format('2. Waktu kerja per hari'))
            print('{:^90}'.format('3. Rating pekerja'))
            print('{:^90}'.format('4. Allowance'))
            print('')
            print('{:^90}'.format('Dengan menggunakan data tersebut, program ini dapat meramal '))
            print('{:^90}'.format('produksi perusahaan untuk 12 bulan ke depannya'))
            print(92 * '-')

      def login(self):
            users = {
                  'prokom': 'password1',
                  'dara': '2027',
                  'kiya': '1035',
                  'azkal': '3007',
                  'aziz': '3019'
            }
      
            max_percobaan = 5
            percobaan = 0
            
            while percobaan < max_percobaan:
                  x = input('\nMasukkan username: ')
                  y = input('Masukkan password: ')
                  
                  if x in users and users[x] == y:
                        print('Anda berhasil login')
                        break
                  else:
                        percobaan += 1
                        pengingat_percobaan = max_percobaan - percobaan
                        if pengingat_percobaan > 0:
                              print(f'Username atau password salah. Sisa percobaan: {pengingat_percobaan}')
                        else:
                              print('Username atau password salah. Anda telah mencapai batas maksimum percobaan.')
            else:
                  print('Anda telah mencapai batas maksimum percobaan login.')
                  exit()
                        

      def hitung_waktu_baku(self, waktu_siklus, rating, allowance):
            waktu_normal = waktu_siklus * (rating / 100)
            waktu_baku = waktu_normal * (100 / (100 - allowance))
            waktu_standar = waktu_baku
            return waktu_standar, waktu_baku, waktu_normal

      def hitung_jumlah_pekerja(self, total_waktu_kerja, waktu_baku):
            jumlah_pekerja = total_waktu_kerja / waktu_baku
            return int(-(-jumlah_pekerja // 1))  # ceiling division

      def ramal_produksi_bulanan(self, total_waktu_kerja_per_hari, waktu_baku_total, waktu_standar_total, waktu_normal_total, hari_dalam_bulan=22):
            produksi_harian_baku = total_waktu_kerja_per_hari / waktu_baku_total
            produksi_bulanan_baku = produksi_harian_baku * hari_dalam_bulan
            produksi_harian_standar = total_waktu_kerja_per_hari / waktu_standar_total
            produksi_bulanan_standar = produksi_harian_standar * hari_dalam_bulan
            produksi_harian_normal = total_waktu_kerja_per_hari / waktu_normal_total
            produksi_bulanan_normal = produksi_harian_normal * hari_dalam_bulan
            jumlah_pekerja_bulanan = self.hitung_jumlah_pekerja(total_waktu_kerja_per_hari * hari_dalam_bulan, waktu_baku_total)
            
            hasil_peramalan = {
                  "produksi_bulanan_baku": produksi_bulanan_baku,
                  "produksi_bulanan_standar": produksi_bulanan_standar,
                  "produksi_bulanan_normal": produksi_bulanan_normal,
                  "jumlah_pekerja_bulanan": jumlah_pekerja_bulanan
            }
            return hasil_peramalan

      def hitung_upah_tenaga_kerja(self, jumlah_pekerja, upah_per_hari, hari_kerja_per_bulan=22):
            total_upah_bulanan = jumlah_pekerja * upah_per_hari * hari_kerja_per_bulan
            return total_upah_bulanan

      def ramal_produksi_12_bulan(self, total_waktu_kerja_per_hari, waktu_baku_total, waktu_standar_total, waktu_normal_total):
            produksi_bulanan_baku_list = []
            produksi_bulanan_standar_list = []
            produksi_bulanan_normal_list = []
            jumlah_pekerja_bulanan_list = []

            for bulan in range(1, 13):
                  hari_dalam_bulan = 22 + (7 if bulan in [1, 5, 8, 11] else 0)
                  hasil_peramalan = self.ramal_produksi_bulanan(total_waktu_kerja_per_hari, waktu_baku_total, waktu_standar_total, waktu_normal_total, hari_dalam_bulan=hari_dalam_bulan)
                  produksi_bulanan_baku_list.append(hasil_peramalan["produksi_bulanan_baku"])
                  produksi_bulanan_standar_list.append(hasil_peramalan["produksi_bulanan_standar"])
                  produksi_bulanan_normal_list.append(hasil_peramalan["produksi_bulanan_normal"])
                  jumlah_pekerja_bulanan_list.append(hasil_peramalan["jumlah_pekerja_bulanan"])

            hasil_peramalan_12_bulan = {
                  "produksi_bulanan_baku": produksi_bulanan_baku_list,
                  "produksi_bulanan_standar": produksi_bulanan_standar_list,
                  "produksi_bulanan_normal": produksi_bulanan_normal_list,
                  "jumlah_pekerja_bulanan": jumlah_pekerja_bulanan_list
            }
            return hasil_peramalan_12_bulan

      def main(self):
            self.cover()
            print(92 * '-')
            print('|{:^90}|'.format('----Selamat Datang di Program Optimasi Waktu Standar Kerja Menggunakan Metode SWDS-----'))
            print(92 * '-')
            
            while True:
                  print(8*'-')
                  print('|{:^6}|'.format('MENU'))
                  print(8*'-')
                  print('1. Login')
                  print('2. Penjelasan program')
                  print('3. Selesai')
                  pilihan = input('Masukkan pilihan Anda: ')
                  
                  if pilihan == '1':
                        print('\nSilahkan LOGIN terlebih dahulu')
                        self.login()
                        break
                  elif pilihan == '2':
                        self.explain()
                        self.login()
                        break
                  elif pilihan == '3':
                        print('\n----TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI---')
                        break
                  else:
                        print('Pilihan tidak valid, silakan coba lagi.')
            
            if pilihan == '3':
                  return  # Tambahkan ini untuk memastikan program berhenti setelah memilih "Selesai"
            
            print(92*'-')
            print ('|{:^90}|'.format('--- MENENTUKAN WAKTU STANDAR DAN JUMLAH PEKERJA DENGAN METODE SWTS ---'))
            print(92*'-')

            
            self.total_waktu_kerja = float(input("Masukkan total waktu kerja yang dibutuhkan dalam menit per hari (misalnya 480 untuk 8 jam kerja): "))
            self.upah_per_hari = float(input("Masukkan upah 1 pekerja (per hari): "))
            
            for nama_kegiatan in self.kegiatan_utama_list:
                  rincian_kegiatan = []
                  
                  print(f"\nKegiatan: {nama_kegiatan}")
                  for rincian in self.rincian_kegiatan_list:
                        waktu_siklus = float(input(f"  Masukkan waktu siklus untuk {rincian} dalam menit: "))
                        rincian_kegiatan.append({
                              "nama": rincian,
                              "waktu_siklus": waktu_siklus
                  })
                  
                  rating = float(input("  Masukkan rating kinerja dalam persen (misalnya 100 untuk standar, 110 untuk 10% lebih cepat): "))
                  allowance = float(input("  Masukkan allowance factor dalam persen (misalnya 15 untuk 15% waktu tambahan): "))
                  
                  self.kegiatan.append({
                  "nama_kegiatan": nama_kegiatan,
                  "rincian_kegiatan": rincian_kegiatan,
                  "rating": rating,
                  "allowance": allowance
                  })
            
            total_waktu_baku = 0
            total_waktu_standar = 0
            total_waktu_normal = 0
            
            for aktivitas in self.kegiatan:
                  nama_kegiatan = aktivitas["nama_kegiatan"]
                  rincian_kegiatan = aktivitas["rincian_kegiatan"]
                  rating = aktivitas["rating"]
                  allowance = aktivitas["allowance"]
                  
                  print(f"\nKegiatan Utama: {nama_kegiatan}")
                  print(f"{'-'*20} {'-'*20} {'-'*20}")
                  print('|{:^20}|{:^20}|{:^20}|'.format('Rincian Kegiatan','Waktu Normal','Waktu Standar'))
                  print(f"{'-'*20} {'-'*20} {'-'*20}")
                  
                  waktu_normal_total_kegiatan = 0
                  waktu_standar_total_kegiatan = 0
                  jumlah_rincian = len(rincian_kegiatan)
                  
                  for rincian in rincian_kegiatan:
                        nama_rincian = rincian["nama"]
                        waktu_siklus = rincian["waktu_siklus"]
                  
                        waktu_standar, waktu_baku, waktu_normal = self.hitung_waktu_baku(waktu_siklus, rating, allowance)
                        total_waktu_baku += waktu_baku
                        total_waktu_standar += waktu_standar
                        total_waktu_normal += waktu_normal

                        waktu_normal_total_kegiatan += waktu_normal
                        waktu_standar_total_kegiatan += waktu_standar
                        waktu_normal_str = f'{waktu_normal:.2f} menit'
                        waktu_standar_str = f'{waktu_standar:.2f} menit'

                        print('|{:^20}|{:^20}|{:^20}|'.format(nama_rincian, waktu_normal_str, waktu_standar_str))
            
                  print(f"{'-'*20} {'-'*20} {'-'*20}")
                  rata_rata_waktu_normal = waktu_normal_total_kegiatan / jumlah_rincian
                  rata_rata_waktu_normal_str = f'{rata_rata_waktu_normal:.2f} menit'
                  rata_rata_waktu_standar = waktu_standar_total_kegiatan / jumlah_rincian
                  rata_rata_waktu_standar_str = f'{rata_rata_waktu_standar:.2f} menit'
                  print('|{:^20}|{:^20}|{:^20}|'.format('Rata-rata', rata_rata_waktu_normal_str, rata_rata_waktu_standar_str))
                  print(f"{'-'*20} {'-'*20} {'-'*20}")
                  print()

            hasil_peramalan = self.ramal_produksi_12_bulan(self.total_waktu_kerja, total_waktu_baku, total_waktu_standar, total_waktu_normal)
            upah_bulanan = [self.hitung_upah_tenaga_kerja(jumlah_pekerja, self.upah_per_hari) for jumlah_pekerja in hasil_peramalan['jumlah_pekerja_bulanan']]

            print(f"\nHasil Perhitungan Gabungan:")
            print(f"  Total Waktu Normal: {total_waktu_normal:.2f} menit")
            print(f"  Total Waktu Standar: {total_waktu_standar:.2f} menit")

            print("\nPerkiraan untuk produksi 12 bulan ke depan:")
            for i, (produksi_baku, produksi_standar, produksi_normal, jumlah_pekerja, upah) in enumerate(zip(
                  hasil_peramalan['produksi_bulanan_baku'],
                  hasil_peramalan['produksi_bulanan_standar'],
                  hasil_peramalan['produksi_bulanan_normal'],
                  hasil_peramalan['jumlah_pekerja_bulanan'],
                  upah_bulanan
            )):
                  print(f"Bulan {i+1}:")
                  print(f"  Produksi Bulanan (Baku): {produksi_baku:.2f} unit")
                  print(f"  Produksi Bulanan (Standar): {produksi_standar:.2f} unit")
                  print(f"  Produksi Bulanan (Normal): {produksi_normal:.2f} unit")
                  print(f"  Jumlah Pekerja yang Dibutuhkan: {jumlah_pekerja} orang")
                  print(f"  Total Upah Tenaga Kerja Bulanan: Rp{upah:.2f}\n")

if __name__ == "__main__":
      Tebe = Program()
      Tebe.main()
