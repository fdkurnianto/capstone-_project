import sys
import pyinputplus as pypi
import datetime

def show(Dict, printFormat, title="\nDaftar Karyawan Existing\n"):
    """_summary_

    Args:
        Dict (dictionary): dict yang akan ditampilkan
        printFormat (string): format tampilan di prompt
        title (str, optional): judul tampilan. Defaults to "\nDaftar Karyawan Existing\n".
    """
    # Looping untuk memilih sub menu fungsi show 
    while True:
        # pilihan sub menu untuk menampilkan total karyawan, detail karyawan, dan kembali ke menu utama
        choice = ['Tampilkan Data Karyawan Keseluruhan', 'Tampilkan Detail Profil Karyawan','Kembali ke menu utama']
        response = pypi.inputMenu(choices=choice, numbered=True)
        # menampilkan keseluruhan data karyawan
        if response == 'Tampilkan Data Karyawan Keseluruhan':
            print(title) # untuk menampilkan judul
            # validasi ketersediaan data
            if len(dictProfilKaryawan) > 1 : 
                for value in Dict.values():
                    print(printFormat.format("", *value))
            elif len(dictProfilKaryawan) < 2 :  
                print('Maaf data tidak ada')
                continue
        # Menampilkan detail salah satu karyawan yang dipilih
        elif response == 'Tampilkan Detail Profil Karyawan':
            # input untuk memasukkan nama karyawan yang akan ditampilkan detailnya
            showprofil = pypi.inputStr(prompt='Silahkan masukkan nama lengkap karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
            # input pn karyawan 
            pnprofil = pypi.inputStr(prompt='Silahkan masukkan PN karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[A-Z|a-z|?#/>,.<:;"!@$%^&*]'])
            # looping untuk validasi ketersediaan data
            for i, value in enumerate(dictDetailProfilKaryawan.values()):
                # jika nama yang diinput terdapat pada value database maka akan ditampilkan detail data dari nama karyawan tersebut
                if showprofil and pnprofil in value:
                   print(f'''
                   \nPN: {value[0]}
                   \nNama Karyawan: {value[1]}
                   \nTanggal Lahir: {value[2]}
                   \nJabatan: {value[3]}
                   \nGender: {value[4]}
                   \nPendidikan: {value[5]}
                   \nAsal Kota: {value[6]}
                   \nAlamat Domisili: {value[7]}
                   \nTanggal Masuk: {value[8]}
                   \nTanggal Pensiun: {value[9]}
                   \nPenghargaan: {value[10]}
                   \n''')
                   break # untuk menghentikan looping karena sudah menghasilkan true
                # validasi jika data tidak terdapat pada dictionary
                elif i == len(dictDetailProfilKaryawan) -1:
                    print('Maaf, kombinasi Nama dan PN yang anda masukkan tidak tepat')
        # jika memilih 3 akan diarahkan pada menu utama
        else :
            main()

def input1():
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

    # perumpaan keys dari data dictionary dictDetailProfilKaryawan
    keys1 = str(len(dictDetailProfilKaryawan))
    # perumpaan keys dari data dictionary dictProfilKaryawan
    keys2 = str(len(dictProfilKaryawan))
    
    # menu input yang berisi akan menyimpan data inputan atau tidak
    response3 = pypi.inputYesNo(prompt='Pastikan data yang anda masukkan sudah benar, apakah akan menyimpan data tersebut? (yes/no): ')
    # jika memilih yes, maka akan dilakukan update pada dictionary dictDetailProfilKaryawan, dictProfilKaryawan
    if response3 == 'yes':
        dictDetailProfilKaryawan.update({keys1: [PNinput, 
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
        dictProfilKaryawan.update({keys2: [PNinput, 
                           namaKaryawan, 
                           Jabataninput, 
                           Genderinput, 
                           Pendidikaninput, 
                           Asalkotainput]})               
    # jika tidak makan data yang diinput akan dihapus dan diarahkan pada submenu
    else:
        add()
    

def add():
    """menu untuk menambahkan data karyawan"""
    choice = ['Tambahkan data karyawan','Kembali ke menu utama']
    response = pypi.inputMenu(choices=choice, numbered=True)
    # jika memilih 1 maka akan diarahkan untuk memasukan nama karyawan
    if response == 'Tambahkan data karyawan':
        addkaryawan = pypi.inputStr(prompt='Silahkan masukkan nama karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
        # looping untuk validasi ketersediaan data
        for i, value in enumerate(dictDetailProfilKaryawan.copy().values()):
            # validasi apakah nama tersebut sudah tersedia atau belum
            if addkaryawan in value:
                response1 = pypi.inputYesNo(prompt='Nama karyawan sudah tersedia, apakah tetap akan menambahkan? (yes/no): ')
                # jika tersedia dan ingin tetap menambahkan makan akan diarahkan untuk mengisi detail data karyawan
                if response1 == 'yes':
                    input1()
                    add()
                # jika tidak akan diarahkan pada submenu
                else :
                    add()
            # validasi jika data tidak terdapat pada dictionary
            elif i == len(dictDetailProfilKaryawan) -1:
                # memastikan apakah akan tetap menambahkan data karyawan
                response2 = pypi.inputYesNo(prompt='Data yang anda masukkan belum tersedia, anda akan diarahkan untuk mengisi form (yes/no): ')
                # jika memilih yes maka akan diarahkan untuk mengisi detail data karyawan
                if response2 == 'yes':
                    input1()
                    add()
                # jika memilih tidak akan diarahkan pada sub menu
                else:
                    add()
    # jika memilih 2 akan diarahkan pada menu utama
    else :
        main()

            
def delete():
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
        for i, value in enumerate(dictDetailProfilKaryawan.copy().values()):
            # jika nama karyawan tersedia akan menampilkan terlebih dahulu detail nama karyawan
            if delkaryawan and pndelete in value:
                print(f'''
                   \nPN: {value[0]}
                   \nNama Karyawan: {value[1]}
                   \nTanggal Lahir: {value[2]}
                   \nJabatan: {value[3]}
                   \nGender: {value[4]}
                   \nPendidikan: {value[5]}
                   \nAsal Kota: {value[6]}
                   \nAlamat Domisili: {value[7]}
                   \nTanggal Masuk: {value[8]}
                   \nTanggal Pensiun: {value[9]}
                   \nPenghargaan: {value[10]}
                   \n''')
                # validasi bahwa data tersebut akan dihapus
                response2 = pypi.inputYesNo(prompt='Nama karyawan tersebut akan dihapus, apakah anda akan men? (yes/no): ')
                # jika memilih yes maka akan menghapus data dari dictionary
                if response2 == 'yes': 
                    del dictProfilKaryawan[f'{i}']
                    del dictDetailProfilKaryawan[f'{i}']
                # jika memilih no maka akan diarahkan pada submenu
                else :
                    delete ()
            # jika nama tidak tersedika akan menampilkan data tidak tersedia dan diarahkan pada sub menu
            elif i == len(dictDetailProfilKaryawan) -1:
                print('Maaf, kombinasi Nama dan PN yang anda masukkan tidak tepat')
                delete()
    # jika memilih 2 maka akan diarahkan pada menu utama
    else :
        main()



def update():
    """fungsi untuk merubah data karyawan baik sebagian maupun keseluruhan"""
    # pilihan menu fungsi update
    choice = ['Rubah data karyawan','Kembali ke menu utama']
    response = pypi.inputMenu(choices=choice, numbered=True)
    # input karyawan yang akan dirubah
    if response == 'Rubah data karyawan':
        upkaryawan = pypi.inputStr(prompt='Silahkan masukkan nama karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|?#/>,.<:;"!@$%^&*]'])
        # input pn karyawan 
        pnupdate = pypi.inputStr(prompt='Silahkan masukkan PN karyawan: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[A-Z|a-z|?#/>,.<:;"!@$%^&*]'])
        # looping untuk validasi ketersediaan data
        for i, value in enumerate(dictDetailProfilKaryawan.values()):
            # jika nama karyawan tersedia akan menampilkan terlebih dahulu detail nama karyawan
            if upkaryawan and pnupdate in value:
                print(f'''
                   \nPN: {value[0]}
                   \nNama Karyawan: {value[1]}
                   \nTanggal Lahir: {value[2]}
                   \nJabatan: {value[3]}
                   \nGender: {value[4]}
                   \nPendidikan: {value[5]}
                   \nAsal Kota: {value[6]}
                   \nAlamat Domisili: {value[7]}
                   \nTanggal Masuk: {value[8]}
                   \nTanggal Pensiun: {value[9]}
                   \nPenghargaan: {value[10]}
                   \n''')
                # validasi untuk melakukan perubahan
                response1 = pypi.inputYesNo(prompt='Apa anda akan merubah data karyawan tersebut? (yes/no): ')
                # jika iya maka akan diarahkan pada data yang ingin dirubah baik sebagian atau keseluruhan
                if response1 == 'yes':
                    prompt = "Silahkan pilih data yang akan dirubah: \n"
                    choice = ['Jabatan', 'Pendidikan', 'Alamat Domisili', 'Penghargaan', 'Update keseluruhan data karyawan', 'Kembali ke menu sebelumnya']
                    response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                    # looping untuk validasi data 
                    for j, value in enumerate(dictDetailProfilKaryawan.copy().values()):
                        k = i
                        # untuk merubah jabatan
                        if response == 'Jabatan':
                            Jabataninput = pypi.inputStr(
                            prompt='Silahkan masukkan Jabatan karyawan terbaru: ', 
                            applyFunc=lambda x: x.capitalize(), blockRegexes= [r'[0-9|?#/>.<:;"!@$%^&*]'])
                            response1 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            # validasi untuk menyimpan perubahan
                            if response1 == 'yes':
                                dictDetailProfilKaryawan[f'{k}'][3] = Jabataninput
                                dictProfilKaryawan[f'{k}'][2] = Jabataninput
                                print(f'Data berhasil dirubah, silahkan cek pada detail data karyawan')
                                update()
                                break
                            else :
                                update()
                        # untuk merubah pendidikan
                        elif response == 'Pendidikan':
                            Pendidikaninput = pypi.inputStr(
                            prompt='Silahkan masukkan Pendidikan karyawan: ', 
                            applyFunc=lambda x: x.capitalize(), blockRegexes= [r'[0-9|?#/>.<:;"!@$%^&*]'])
                            response2 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            # validasi untuk menyimpan perubahan
                            if response2 == 'yes':
                                dictDetailProfilKaryawan[f'{k}'][5] = Pendidikaninput
                                dictProfilKaryawan[f'{k}'][4] = Pendidikaninput
                                print(f'Data berhasil dirubah, silahkan cek pada detail data karyawan')
                                update()
                                break
                            else :
                                update()
                        # untuk merubah alamat domisili
                        elif response == 'Alamat Domisili':
                            AlamatDomisiliinput = pypi.inputStr(
                            prompt='Silahkan masukkan alamat domisili karyawan: ', 
                            applyFunc=lambda x: x.capitalize(),  blockRegexes= [r'[0-9|?#/>.<:;"!@$%^&*]'])
                            response3 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            # validasi untuk menyimpan perubahan
                            if response3 == 'yes':
                                dictDetailProfilKaryawan[f'{k}'][7] = AlamatDomisiliinput
                                print(f'Data berhasil dirubah, silahkan cek pada detail data karyawan')
                                update()
                                break
                            else :
                                update()
                        # untuk menambah penghargaan
                        elif response == 'Penghargaan':
                            Penghargaan = pypi.inputStr(
                            prompt='Silahkan masukkan penghargaan karyawan: ', 
                            applyFunc=lambda x: x.title(),  blockRegexes= [r'[0-9|?#/>.<:;"!@$%^&*]'])
                            response4 = pypi.inputYesNo(prompt='Pastikan data yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            # validasi untuk menyimpan perubahan
                            if response4 == 'yes':
                                dictDetailProfilKaryawan[f'{k}'][10] += (f', {Penghargaan}')
                                print(f'Data berhasil dirubah, silahkan cek pada detail data karyawan')
                                update()
                                break
                            else : 
                                update()
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
                                dictDetailProfilKaryawan.update({f'{k}': [PNinput, 
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
                                dictProfilKaryawan.update({f'{k}': [PNinput, 
                                                namaKaryawan, 
                                                Jabataninput, 
                                                Genderinput, 
                                                Pendidikaninput, 
                                                Asalkotainput]})
                                print('Data sudah tersimpan silahkan cek pada menu tampilkan data')
                                update()
                                break
                            else :
                                print('Data yang anda masukkan tidak tersimpan')
                                update()
            # validasi jika nama tidak tersedia                                   
            elif i == len(dictDetailProfilKaryawan) -1:
                print('Maaf, kombinasi Nama dan PN yang anda masukkan tidak tepat')
                update()
    main()

def main():
    while True:
        # Menampilkan tampilan utama program
        prompt = f"\t-------Selamat datang!-------\nBerikut Merupakan Data Karyawan PT. Abadi Jaya:\n"
        # Input fitur yang akan dijalankan
        choice = ['Tampilkan Data Karyawan', 'Menambahkan Data Karyawan', 'Menghapus Data Karyawan', 'Memperbarui Data Karyawan', 'Exit']
        response = pypi.inputMenu(prompt=prompt, choices=choice, numbered=True)
        # Fitur menampilkan daftar karyawan
        if response == 'Tampilkan Data Karyawan':
            show(dictProfilKaryawan, printFormat)
        # Fitur menambahkan karyawan
        elif response == 'Menambahkan Data Karyawan':
            add()
        # Fitur menghapus karyawan
        elif response == 'Menghapus Data Karyawan':
            delete()
        # Fitur memperbarui data karyawan
        elif response == 'Memperbarui Data Karyawan':
            update()
        # Fitur exit program
        else:
            sys.exit()

if __name__ == "__main__":
    # deklarasi Profil karyawan
    dictProfilKaryawan = {
        'column' : ["PN", "Nama Karyawan", "Jabatan", "Gender", "Pendidikan", "Asal Kota"],
        '1' : ["141", "John Petrucci", "CEO", "Male", "Doctor", "Jakarta"],
        '2' : ["129", "John Lennon", "CE", "Male", "Master", "Jakarta"],
        '3' : ["183", "Gugun Blues", "Secretary", "Male", "Bachelor", "Solo"],
        '4' : ["137", "Dewa Budjana", "HRD", "Male", "Bachelor", "Bali"],
        '5' : ["194", "Eros Candra", "Marketing", "Male", "Bachelor", "Yogyakarta"],
    }
    # deklarasi detail profil karyawan
    dictDetailProfilKaryawan = {
        'column' : ["PN", "Nama Karyawan","Tanggal Lahir", "Jabatan", "Gender", "Pendidikan", "Asal Kota", "Alamat Domisili", "Tanggal Masuk", "Tanggal Pensiun", "Penghargaan"],
        '1' : ["141", "John Petrucci", datetime.date(1970, 5, 14), "CEO", "Male", "Doctor", "Jakarta", "Sleman, Yogyakarta", datetime.date(1996, 12, 22), datetime.date(2026, 1, 6), "Best CEO 2021"],
        '2' : ["129", "John Lennon", datetime.date(1974, 12, 17), "CE", "Male", "Master", "Jakarta", "Sleman, Yogyakarta", datetime.date(2000, 4, 1), datetime.date(2031, 1, 1), "Best Marketing 2016"],
        '3' : ["183", "Gugun Blues", datetime.date(1976, 7, 29), "Secretary", "Male", "Bachelor", "Solo", "Bantul, Yogyakarta", datetime.date(2000, 9, 19), datetime.date(2030, 1, 8), "-"],
        '4' : ["137", "Dewa Budjana", datetime.date(1975, 2, 2), "HRD", "Male", "Master", "Bali", "Gunung, Yogyakarta", datetime.date(2000, 5, 20), datetime.date(2031, 3, 1), "-"],
        '5' : ["194", "Eros Candra", datetime.date(1979, 3, 22), "Marketing", "Male", "Bachelor", "Yogyakarta", "Sleman, Yogyakarta", datetime.date(1970, 5, 14), datetime.date(2034, 1, 4), "2019 Best Marketing, 2022 Best Marketing"],
    }
    #deklarasi print format di menu
    printFormat = "{:<4}" + "{:<15}" * (len(dictProfilKaryawan['column']))
    # main menu
    main()
