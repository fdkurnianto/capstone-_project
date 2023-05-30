import sys
import pyinputplus as pypi
import csv
import tabulate
import os

def show(database, title="\nDaftar Karyawan Existing\n"):
    """_summary_

    Args:
        Dict (dictionary): dict yang akan ditampilkan
        printFormat (string): format tampilan di prompt
        title (str, optional): judul tampilan. Defaults to "\nDaftar Karyawan Existing\n".
    """
    # menggambil baris dari index 1 dari database
    data = list(database.values())[1:]
    # variabel sementara untuk menyimpan perubahan
    data1 = []
    # menggambil columns dari index 0 sampai 5
    columns1 = columns[:6]
    # looping untuk menampilkan setiap data index i
    for i, values in enumerate(data): #[0]
        data2 = list(database.values())[1:][i][:6]
        data1.append(data2)
    # Looping untuk memilih sub menu fungsi show 
    while True:
        # pilihan sub menu untuk menampilkan total karyawan, detail karyawan, dan kembali ke menu utama
        choice = ['Tampilkan Data Karyawan Keseluruhan', 'Tampilkan Detail Profil Karyawan','Kembali ke menu utama']
        response = pypi.inputMenu(choices=choice, numbered=True)
        # menampilkan keseluruhan data karyawan
        if response == 'Tampilkan Data Karyawan Keseluruhan':
            print(title) # untuk menampilkan judul
            if data1 == []:
                # only display columns without any data
                print(tabulate.tabulate(data1, headers=columns1, tablefmt= "outline"))
                print("\nData doesn't exist!")
            else:
                # print database in tabular format
                print(tabulate.tabulate(data1, headers=columns1, tablefmt="outline"))
                print('\n')
            # Menampilkan detail salah satu karyawan yang dipilih
        elif response == 'Tampilkan Detail Profil Karyawan':
            # input untuk memasukkan nama karyawan yang akan ditampilkan detailnya
            showprofil = pypi.inputStr(prompt='Silahkan masukkan nama lengkap karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
            # input pn karyawan 
            pnprofil = pypi.inputStr(prompt='Silahkan masukkan PN karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[A-Z|a-z|?#/>,.<:;"!@$%^&*]'])
            # looping untuk validasi ketersediaan data
            for i, value in enumerate(data):
                # jika nama yang diinput terdapat pada value database maka akan ditampilkan detail data dari nama karyawan tersebut
                if showprofil and pnprofil in value:
                   datadetail = [['PN', data[i][0]],
                                 ['Nama Karyawan', data[i][1]],
                                 ['Tanggal Lahir', data[i][2]],
                                 ['Jabatan', data[i][3]],
                                 ['Gender', data[i][4]],
                                 ['Pendidikan', data[i][5]],
                                 ['Asal Kota', data[i][6]],
                                 ['Alamat Domisili', data[i][7]],
                                 ['Tanggal Masuk', data[i][8]],
                                 ['Tanggal Pensiun', data[i][9]],
                                 ['Penghargaan', data[i][10]]]
                   print(tabulate.tabulate(datadetail, headers=['Data','Detail'], tablefmt="outline"))
                   break # untuk menghentikan looping karena sudah menghasilkan true
                # validasi jika data tidak terdapat pada dictionary
                elif i == len(data) -1:
                    print('Maaf, kombinasi Nama dan PN yang anda masukkan tidak tepat')
        # jika memilih 3 akan diarahkan pada menu utama
        else :
            main()

def input1(database):
    """Fungsi input yang dapat digunakan pada menu menambah 
    karyawan, yang berisi tentang 
    inputan detail data karyawan"""

    #untuk menginput data karyawan, dengan x.title : untuk menampilkan 
    #huruf besar pada setiap kata, dan tidak dapat diinputkan data integer
    namaKaryawan = pypi.inputStr(
    prompt='Silahkan masukkan nama lengkap karyawan: ', 
    applyFunc=lambda x: x.title(), 
    blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
    
    # untuk mengisikan Personal Number karyawan, data = str
    PNinput = pypi.inputStr(prompt='Silahkan masukkan PN karyawan: ', 
    applyFunc=lambda x: x.title(), 
    blockRegexes=[r'[A-Z|a-z|?#/>,.<:;"!@$%^&*]'])

    # untuk mengisikan tanggal lahir karyawan
    TanggalLahirInput = str(pypi.inputDate(
    prompt='Masukkan tanggal lahir karyawan, format YYYY/MM/DD: '))
    
    # untuk mengisikan jabatan karyawan
    Jabataninput = pypi.inputStr(
    prompt='Silahkan masukkan Jabatan karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])

    # untuk mengisikan gender karyawan
    Genderinput = pypi.inputChoice(prompt='Silahkan masukkan gender karyawan (male/female):  ', 
    choices=['male', 'female'])

    # untuk mengisikan pendidikan karyawan
    Pendidikaninput = pypi.inputStr(
    prompt='Silahkan masukkan Pendidikan karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])

    # untuk mengisikan asal kota karyawan
    Asalkotainput = pypi.inputStr(
    prompt='Silahkan masukkan asal kota karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>.<:;"!@$%^&*]'])

    # untuk mengisikan alamat domisili karyawan
    AlamatDomisiliinput = pypi.inputStr(
    prompt='Silahkan masukkan alamat domisili karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes= [r'[0-9|?#/>,.<:;"!@$%^&*]'])

    # untuk mengisikan tanggal masuk karyawan
    TanggalMasuk = str(pypi.inputDate(
    prompt='Masukkan tanggal masuk karyawan, format YYYY/MM/DD: '))
    

    # untuk mengisikan tanggal pensiun karyawan
    TanggalPensiun = str(pypi.inputDate(
    prompt='Masukkan tanggal pensiun karyawan, format YYYY/MM/DD: '))
    

    # untuk mengisikan penghargaan karyawan
    Penghargaan = pypi.inputStr(
    prompt='Silahkan masukkan penghargaan karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes= [r'[?#/>,.<:;"!@$%^&*]'])

    # perumpaan keys dari data dictionary dictDetailProfilKaryawan
    keys1 = str(len(database))
    
    # menu input yang berisi akan menyimpan data inputan atau tidak
    response3 = pypi.inputYesNo(prompt='Pastikan data yang anda masukkan sudah benar, apakah akan menyimpan data tersebut? (yes/no): ')
    # jika memilih yes, maka akan dilakukan update pada dictionary dictDetailProfilKaryawan, dictProfilKaryawan
    if response3 == 'yes':
        database.update({keys1: [PNinput, 
                         namaKaryawan, 
                         TanggalLahirInput, 
                         Jabataninput, 
                         Genderinput, 
                         Pendidikaninput, 
                         Asalkotainput, 
                         AlamatDomisiliinput, 
                         TanggalMasuk, 
                         TanggalPensiun, 
                         Penghargaan]})
                     
    # jika tidak makan data yang diinput akan dihapus dan diarahkan pada submenu
    else:
        add()
    
def add(database):
    """menu untuk menambahkan data karyawan"""
    choice = ['Tambahkan data karyawan','Kembali ke menu utama']
    response = pypi.inputMenu(choices=choice, numbered=True)
    # jika memilih 1 maka akan diarahkan untuk memasukan nama karyawan
    if response == 'Tambahkan data karyawan':
        addkaryawan = pypi.inputStr(prompt='Silahkan masukkan nama karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
        # looping untuk validasi ketersediaan data
        for i, value in enumerate(database.values()):
            # validasi apakah nama tersebut sudah tersedia atau belum
            if addkaryawan in value:
                response1 = pypi.inputYesNo(prompt='Nama karyawan sudah tersedia, apakah tetap akan menambahkan? (yes/no): ')
                # jika tersedia dan ingin tetap menambahkan makan akan diarahkan untuk mengisi detail data karyawan
                if response1 == 'yes':
                    input1(database)
                    print('Data sudah berhasil ditambahkan!')
                    break
                # jika tidak akan diarahkan pada submenu
                else :
                    add(database)
            # validasi jika data tidak terdapat pada dictionary
            elif i == len(database) -1:
                # memastikan apakah akan tetap menambahkan data karyawan
                response2 = pypi.inputYesNo(prompt='Data yang anda masukkan belum tersedia, anda akan diarahkan untuk mengisi form (yes/no): ')
                # jika memilih yes maka akan diarahkan untuk mengisi detail data karyawan
                if response2 == 'yes':
                    input1(database)
                    add(database)
                    print('Data sudah berhasil ditambahkan')
                # jika memilih tidak akan diarahkan pada sub menu
                else:
                    add(database)
        add(database)
    # jika memilih 2 akan diarahkan pada menu utama
    else :
        main()

    return database
            
def delete(database):
    data = list(database.values())[1:]
    """fungsi delete untuk menghapus data karyawan"""
    # menu yang tersedia adalah hapus data karyawan dan kembali ke menu utama
    choice = ['Hapus data karyawan','Kembali ke menu utama']
    response = pypi.inputMenu(choices=choice, numbered=True)
    # Input nama karyawan yang akan dihapus
    if response == 'Hapus data karyawan':
        delkaryawan = pypi.inputStr(prompt='Silahkan masukkan nama karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
        # input pn karyawan 
        pndelete = pypi.inputStr(prompt='Silahkan masukkan PN karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[A-Z|a-z|?#/>,.<:;"!@$%^&*]'])
        # looping untuk validasi ketersediaan data
        j = 0 # variabel baru untuk mengganti index ke - i
        for key, value in database.copy().items():
            # jika nama karyawan tersedia akan menampilkan terlebih dahulu detail nama karyawan
            if delkaryawan and pndelete in value:
                datadetail = [['PN', value[0]],
                                 ['Nama Karyawan', value[1]],
                                 ['Tanggal Lahir', value[2]],
                                 ['Jabatan', value[3]],
                                 ['Gender', value[4]],
                                 ['Pendidikan', value[5]],
                                 ['Asal Kota', value[6]],
                                 ['Alamat Domisili', value[7]],
                                 ['Tanggal Masuk', value[8]],
                                 ['Tanggal Pensiun', value[9]],
                                 ['Penghargaan', value[10]]]
                print(tabulate.tabulate(datadetail, headers=['Data','Detail'], tablefmt="outline"))
                # validasi bahwa data tersebut akan dihapus
                response2 = pypi.inputYesNo(prompt='Nama karyawan tersebut akan dihapus, apakah anda jadi menghapus? (yes/no): ')
                # jika memilih yes maka akan menghapus data dari dictionary
                if response2 == 'yes':
                    # handling eror ketika salah masukkan 3x password
                    try:
                        password = pypi.inputChoice(prompt='Hanya CEO dan Sekretaris yang bisa menghapus data\nSilahkan masukkan password :  ', 
                        choices=['Sekre9900', 'CEO12340'], limit= 3)
                        if password == 'Sekre9900' or 'CEO12340' :
                            print(f'Data sudah berhasil dihapus!')
                            del database[key]
                        else :
                            break
                    # jika salah 3x maka akan mengembalikan pada menu delete
                    except: 
                        print('Password yang anda masukkan salah 3x!')
                        delete(database)
                # jika memilih no maka akan diarahkan pada submenu
                else :
                    delete (database)
            # jika nama tidak tersedika akan menampilkan data tidak tersedia dan diarahkan pada sub menu
            elif j == len(database)-1:
                print('Maaf, kombinasi Nama dan PN yang anda masukkan tidak tepat')
                delete(database)
            j += 1
        delete(database)
    # jika memilih 2 maka akan diarahkan pada menu utama
    else :
        main()

    return database

def update(database):
    """fungsi untuk merubah data karyawan baik sebagian maupun keseluruhan"""
    # pilihan menu fungsi update
    choice = ['Rubah data karyawan','Kembali ke menu utama']
    response = pypi.inputMenu(choices=choice, numbered=True)
    # input karyawan yang akan dirubah
    if response == 'Rubah data karyawan':
        upkaryawan = pypi.inputStr(prompt='Silahkan masukkan nama karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
        # input pn karyawan 
        pnupdate = pypi.inputStr(prompt='Silahkan masukkan PN karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[A-Z|a-z|?#/>,.<:;"!@$%^&*]'])
        j = 0 # variabel baru untuk mengganti index ke - i
        # looping untuk validasi ketersediaan data
        for key, value in database.copy().items():
            # jika nama karyawan tersedia akan menampilkan terlebih dahulu detail nama karyawan
            if upkaryawan and pnupdate in value:
                datadetail = [['PN', value[0]],
                                 ['Nama Karyawan', value[1]],
                                 ['Tanggal Lahir', value[2]],
                                 ['Jabatan', value[3]],
                                 ['Gender', value[4]],
                                 ['Pendidikan', value[5]],
                                 ['Asal Kota', value[6]],
                                 ['Alamat Domisili', value[7]],
                                 ['Tanggal Masuk', value[8]],
                                 ['Tanggal Pensiun', value[9]],
                                 ['Penghargaan', value[10]]]
                print(tabulate.tabulate(datadetail, headers=['Data','Detail'], tablefmt="outline"))
                # validasi untuk melakukan perubahan
                response1 = pypi.inputYesNo(prompt='Apa anda akan merubah data karyawan tersebut? (yes/no): ')
                # jika iya maka akan diarahkan pada data yang ingin dirubah baik sebagian atau keseluruhan
                if response1 == 'yes':
                    prompt = "Silahkan pilih data yang akan dirubah: \n"
                    choice = ['Jabatan', 'Pendidikan', 'Alamat Domisili', 'Penghargaan', 'Update keseluruhan data karyawan', 'Kembali ke menu sebelumnya']
                    response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                    # looping untuk validasi data 
                    for j, value in enumerate(database.copy().values()):
                        # k = key
                        # untuk merubah jabatan
                        if response == 'Jabatan':
                            Jabataninput = pypi.inputStr(
                            prompt='Silahkan masukkan Jabatan karyawan terbaru: ', 
                            applyFunc=lambda x: x.capitalize(), blockRegexes= [r'[0-9|?#/>.<:;"!@$%^&*]'])
                            response1 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            # validasi untuk menyimpan perubahan
                            if response1 == 'yes':
                                database[key][3] = Jabataninput
                                print(f'Data berhasil dirubah, silahkan cek pada detail data karyawan')
                                update(database)
                                break
                            else :
                                update(database)
                        # untuk merubah pendidikan
                        elif response == 'Pendidikan':
                            Pendidikaninput = pypi.inputStr(
                            prompt='Silahkan masukkan Pendidikan karyawan: ', 
                            applyFunc=lambda x: x.capitalize(), blockRegexes= [r'[0-9|?#/>.<:;"!@$%^&*]'])
                            response2 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            # validasi untuk menyimpan perubahan
                            if response2 == 'yes':
                                database[key][5] = Pendidikaninput
                                print(f'Data berhasil dirubah, silahkan cek pada detail data karyawan')
                                update(database)
                                break
                            else :
                                update(database)
                        # untuk merubah alamat domisili
                        elif response == 'Alamat Domisili':
                            AlamatDomisiliinput = pypi.inputStr(
                            prompt='Silahkan masukkan alamat domisili karyawan: ', 
                            applyFunc=lambda x: x.capitalize(),  blockRegexes= [r'[0-9|?#/>.<:;"!@$%^&*]'])
                            response3 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            # validasi untuk menyimpan perubahan
                            if response3 == 'yes':
                                database[key][7] = AlamatDomisiliinput
                                print(f'Data berhasil dirubah, silahkan cek pada detail data karyawan')
                                update(database)
                                break
                            else :
                                update(database)
                        # untuk menambah penghargaan
                        elif response == 'Penghargaan':
                            Penghargaan = pypi.inputStr(
                            prompt='Silahkan masukkan penghargaan karyawan: ', 
                            applyFunc=lambda x: x.title(),  blockRegexes= [r'[0-9|?#/>.<:;"!@$%^&*]'])
                            response4 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            # validasi untuk menyimpan perubahan
                            if response4 == 'yes':
                                database[key][10] += (f', {Penghargaan}')
                                print(f'Data berhasil dirubah, silahkan cek pada detail data karyawan')
                                update(database)
                                break
                            else : 
                                update(database)
                        # untuk merubah keseluruhan data
                        elif response == 'Update keseluruhan data karyawan' :
                            #untuk menginput data karyawan, dengan x.title : untuk menampilkan 
                            #huruf besar pada setiap kata, dan tidak dapat diinputkan data integer
                            namaKaryawan = pypi.inputStr(
                            prompt='Silahkan masukkan nama lengkap karyawan: ', 
                            applyFunc=lambda x: x.title(), 
                            blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
                            
                            # untuk mengisikan Personal Number karyawan, data = str
                            PNinput = pypi.inputStr(prompt='Silahkan masukkan PN karyawan: ', 
                            applyFunc=lambda x: x.title(), 
                            blockRegexes=[r'[A-Z|a-z|?#/>,.<:;"!@$%^&*]'])

                            # untuk mengisikan tanggal lahir karyawan
                            TanggalLahirInput = pypi.inputDate(
                            prompt='Masukkan tanggal lahir karyawan, format YYYY/MM/DD: ')
                            
                            # untuk mengisikan jabatan karyawan
                            Jabataninput = pypi.inputStr(
                            prompt='Silahkan masukkan Jabatan karyawan: ', 
                            applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])

                            # untuk mengisikan gender karyawan
                            Genderinput = pypi.inputChoice(prompt='Silahkan masukkan gender karyawan (male/female):  ', 
                            choices=['male', 'female'])

                            # untuk mengisikan pendidikan karyawan
                            Pendidikaninput = pypi.inputStr(
                            prompt='Silahkan masukkan Pendidikan karyawan: ', 
                            applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])

                            # untuk mengisikan asal kota karyawan
                            Asalkotainput = pypi.inputStr(
                            prompt='Silahkan masukkan asal kota karyawan: ', 
                            applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>.<:;"!@$%^&*]'])

                            # untuk mengisikan alamat domisili karyawan
                            AlamatDomisiliinput = pypi.inputStr(
                            prompt='Silahkan masukkan alamat domisili karyawan: ', 
                            applyFunc=lambda x: x.title(), blockRegexes= [r'[0-9|?#/>,.<:;"!@$%^&*]'])

                            # untuk mengisikan tanggal masuk karyawan
                            TanggalMasuk = pypi.inputDate(
                            prompt='Masukkan tanggal masuk karyawan, format YYYY/MM/DD: ')
                            
                            # untuk mengisikan tanggal pensiun karyawan
                            TanggalPensiun = pypi.inputDate(
                            prompt='Masukkan tanggal pensiun karyawan, format YYYY/MM/DD: ')
                            
                            # untuk mengisikan penghargaan karyawan
                            Penghargaan = pypi.inputStr(
                            prompt='Silahkan masukkan penghargaan karyawan: ', 
                            applyFunc=lambda x: x.title(), blockRegexes= [r'[?#/>,.<:;"!@$%^&*]'])
                            # validasi untuk menyimpan perubahan
                            response5 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            if response5 == 'yes':
                                database.update({key: [PNinput, 
                                                                namaKaryawan, 
                                                                TanggalLahirInput, 
                                                                Jabataninput, 
                                                                Genderinput, 
                                                                Pendidikaninput, 
                                                                Asalkotainput, 
                                                                AlamatDomisiliinput, 
                                                                TanggalMasuk, 
                                                                TanggalPensiun, 
                                                                Penghargaan]})
                                print('Data sudah tersimpan silahkan cek pada menu tampilkan data')
                                update(database)
                                break
                            else :
                                print('Data yang anda masukkan tidak tersimpan')
                                update(database)
            # validasi jika nama tidak tersedia                                   
            elif j == len(database)-1:
                print('Maaf, kombinasi Nama dan PN yang anda masukkan tidak tepat')
                update(database)
            j += 1
        update(database)
    else : 
        main()
    return database

def main():
    global db
    while True:
        while True:
            try: # ketika try dijalankan dan tidak ada eror apaapun itu, maka exept tidak dijalankan.
                # Menampilkan tampilan utama program
                prompt = f"\t-------Selamat datang!-------\nBerikut Merupakan Data Karyawan PT. Abadi Jaya:\n"
                # Input fitur yang akan dijalankan
                choice = ['Tampilkan Data Karyawan', 'Menambahkan Data Karyawan', 'Menghapus Data Karyawan', 'Memperbarui Data Karyawan', 'Exit']
                response = pypi.inputMenu(prompt=prompt, choices=choice, numbered=True)
                # Fitur menampilkan daftar karyawan
                if response == 'Tampilkan Data Karyawan':
                    show(db)
                # Fitur menambahkan karyawan
                elif response == 'Menambahkan Data Karyawan':
                    db = add(db)
                # Fitur menghapus karyawan
                elif response == 'Menghapus Data Karyawan':
                    db = delete(db)
                # Fitur memperbarui data karyawan
                elif response == 'Memperbarui Data Karyawan':
                    db = update(db)
                # Fitur exit program
                else:
                    print('Terima Kasih!')
                    break

                # membuka database
                file = open(path, 'w')

                # menyimpan database terbaru
                writer = csv.writer(file, lineterminator='\n', delimiter=';')
                columns = list(db.values())[0] # termasuk kolom dan data
                data = list(db.values())[1:]
                writer.writerow(columns) #db.values()
                data = list(db.values())[1:]
                for i in data:
                    writer.writerow(i)

            except KeyboardInterrupt:
                # membuka database
                file = open(path, 'w')

                # menyimpan database terbaru
                writer = csv.writer(file, lineterminator='\n', delimiter=';')
                columns = list(db.values())[0] # termasuk kolom dan data
                data = list(db.values())[1:]
                writer.writerow(columns) #db.values()
                data = list(db.values())[1:]
                for i in data:
                    writer.writerow(i)


            # close Program
            file.close()

        # close program
        sys.exit()

if __name__ == "__main__":
    path = r'C:\Users\user\Documents\database purwadhika\capstone_project\detailkaryawan.csv'

    if os.path.getsize(path) == 0:
        print('Database doesnt exist, please enter some data!')
    else:
        # Membaca csv file
        file = open(path, 'r')
        reader = csv.reader(file, delimiter=';')

        # substitusi column
        columns = next(reader)

        # make dictionary data type. db as a variable of dictionary data
        db = {'columns':columns}
       
        for i, row in enumerate(reader): # updating dictionary data
            #print(row[1])
            db.update({
                (str(f'{i}')) : [str(row[0]), 
                        str(row[1]),
                        str(row[2]), 
                        str(row[3]),
                        str(row[4]),
                        str(row[5]),
                        str(row[6]),
                        str(row[7]),
                        str(row[8]),
                        str(row[9]),
                        str(row[10])
                        ]})
        # close program
        file.close()

        # menjalankan main menu
        main()
