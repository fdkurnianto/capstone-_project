
import sys
import pyinputplus as pypi

def show(Dict, printFormat, title="\nDaftar Karyawan Existing\n"):
    """_summary_

    Args:
        Dict (dictionary): dict yang akan ditampilkan
        printFormat (string): format tampilan di prompt
        title (str, optional): judul tampilan. Defaults to "\nDaftar Karyawan Existing\n".
    """
    while True:
        choice = ['Tampilkan Data Karyawan Keseluruhan', 'Tampilkan Detail Profil Karyawan','Kembali ke menu utama']
        response = pypi.inputMenu(choices=choice, numbered=True)
        if response == 'Tampilkan Data Karyawan Keseluruhan':
            print(title)
            for value in Dict.values():
                print(printFormat.format("", *value))
        elif response == 'Tampilkan Detail Profil Karyawan':
            showprofil = input(f'silahkan masukkan nama karyawan: ').title()
            for i, value in enumerate(dictDetailProfilKaryawan.values()):
                if showprofil in value:
                   print(f'''
                   \nPN: {value[0]}
                   \nNama Karyawan: {value[1]}
                   \nTTL: {value[2]}
                   \nJabatan: {value[3]}
                   \nGender: {value[4]}
                   \nPendidikan: {value[5]}
                   \nAsal Kota: {value[6]}
                   \nAlamat Domisili: {value[7]}
                   \nTanggal Masuk: {value[8]}
                   \nTanggal Pensiun: {value[9]}
                   \nPenghargaan: {value[10]}
                   \n''')
                   break
                elif i == len(dictDetailProfilKaryawan) -1:
                    print('Nama yang anda masukkan tidak ada')
        else :
            main()

def input1():

    namaKaryawan = pypi.inputStr(
    prompt='Silahkan masukkan nama lengkap karyawan: ', 
    applyFunc=lambda x: x.title(), 
    blockRegexes=[r'[0-9]'])

    PNinput = pypi.inputInt(
    prompt='Masukkan PN Karyawan: ')

    TTLinput = pypi.inputStr(
    prompt='Tanggal lahir karyawan: ',
    applyFunc=lambda x: x.title() )

    Jabataninput = pypi.inputStr(
    prompt='Silahkan masukkan Jabatan karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])

    Genderinput = pypi.inputStr(
    prompt='Silahkan masukkan gender karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])

    Pendidikaninput = pypi.inputStr(
    prompt='Silahkan masukkan Pendidikan karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])

    Asalkotainput = pypi.inputStr(
    prompt='Silahkan masukkan asal kota karyawan: ', 
    applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])

    AlamatDomisiliinput = pypi.inputStr(
    prompt='Silahkan masukkan alamat domisili karyawan: ', 
    applyFunc=lambda x: x.title())

    TanggalMasuk = pypi.inputStr(
    prompt='Silahkan masukkan Tanggal Masuk karyawan: ', 
    applyFunc=lambda x: x.title())

    TanggalPensiun = pypi.inputStr(
    prompt='Silahkan masukkan Tanggal Pensiun karyawan: ', 
    applyFunc=lambda x: x.title())

    Penghargaan = pypi.inputStr(
    prompt='Silahkan masukkan penghargaan karyawan: ', 
    applyFunc=lambda x: x.title())

    keys1 = len(dictDetailProfilKaryawan) -1
    keys2 = len(dictProfilKaryawan) -1
    
    response3 = pypi.inputYesNo(prompt='Pastikan data yang anda masukkan sudah benar, apakah akan menyimpan data tersebut? (yes/no): ')
    if response3 == 'yes':
        dictDetailProfilKaryawan.update({keys1: [PNinput, 
                         namaKaryawan, 
                         TTLinput, 
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
    else:
        add()
    

def add():
       
    choice = ['Tambahkan data karyawan','Kembali ke menu utama']
    response = pypi.inputMenu(choices=choice, numbered=True)
    if response == 'Tambahkan data karyawan':
        addkaryawan = input(f'silahkan masukkan nama karyawan: ').title()
        for i, value in enumerate(dictDetailProfilKaryawan.copy().values()):
            if addkaryawan in value:
                response1 = pypi.inputYesNo(prompt='Nama karyawan sudah tersedia, apakah tetap akan menambahkan? (yes/no): ')
                if response1 == 'yes':
                    input1()
                else :
                    add()
            elif i == len(dictDetailProfilKaryawan) -1:
                response2 = pypi.inputYesNo(prompt='Data yang anda masukkan belum tersedia, anda akan diarahkan untuk mengisi form (yes/no): ')
                # print('Data yang anda masukkan belum tersedia, silahkan lengkapi form: ')
                if response2 == 'yes':
                    input1()
                else:
                    add()
    else :
        main()

            
def delete():
    choice = ['Hapus data karyawan','Kembali ke menu utama']
    response = pypi.inputMenu(choices=choice, numbered=True)
    # Input indeks karyawan yang akan dihapus
    if response == 'Hapus data karyawan':
        delkaryawan = input(f'silahkan masukkan nama karyawan: ').title()
        # del1 = dictDetailProfilKaryawan.pop[i]
        # del2 = dictProfilKaryawan.pop[i]
        for i, value in enumerate(dictDetailProfilKaryawan.copy().values()):
            if delkaryawan in value:
                response1 = pypi.inputYesNo(prompt='Nama karyawan tersedia, apakah tetap akan menghapus? (yes/no): ')
                if response1 == 'yes':
                    response2 = pypi.inputYesNo(prompt='Nama karyawan tersebut akan dihapus, apakah anda akan menyimpannya? (yes/no): ')
                    if response2 == 'yes': 
                        del dictProfilKaryawan[f'{i}']
                        del dictDetailProfilKaryawan[f'{i}']
                else :
                    delete()
            elif i == len(dictDetailProfilKaryawan) -1:
                print('Maaf nama karyawan tidak tersedia')
                delete()
    else :
        main()

def update():
    choice = ['Rubah data karyawan','Kembali ke menu utama']
    response = pypi.inputMenu(choices=choice, numbered=True)
    if response == 'Rubah data karyawan':
        upkaryawan = input(f'silahkan masukkan nama karyawan: ').title()
        for i, value in enumerate(dictDetailProfilKaryawan.values()):
            if upkaryawan in value:
                print(f'''
                   \nPN: {value[0]}
                   \nNama Karyawan: {value[1]}
                   \nTTL: {value[2]}
                   \nJabatan: {value[3]}
                   \nGender: {value[4]}
                   \nPendidikan: {value[5]}
                   \nAsal Kota: {value[6]}
                   \nAlamat Domisili: {value[7]}
                   \nTanggal Masuk: {value[8]}
                   \nTanggal Pensiun: {value[9]}
                   \nPenghargaan: {value[10]}
                   \n''')
                response1 = pypi.inputYesNo(prompt='Apa anda akan merubah data karyawan tersebut? (yes/no): ')
                if response1 == 'yes':
                    prompt = "Silahkan pilih data yang akan dirubah\n"
                    choice = ['Jabatan', 'Pendidikan', 'Alamat Domisili', 'Penghargaan', 'Update keseluruhan data karyawan', 'Kembali ke menu sebelumnya']
                    response = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                    for j, value in enumerate(dictDetailProfilKaryawan.copy().values()):
                        k = i
                        if response == 'Jabatan':
                            Jabataninput = pypi.inputStr(
                            prompt='Silahkan masukkan Jabatan karyawan terbaru: ', 
                            applyFunc=lambda x: x.capitalize())
                            dictDetailProfilKaryawan[f'{k}'][3] = Jabataninput
                            dictProfilKaryawan[f'{k}'][2] = Jabataninput
                        elif response == 'Pendidikan':
                            Pendidikaninput = pypi.inputStr(
                            prompt='Silahkan masukkan Pendidikan karyawan: ', 
                            applyFunc=lambda x: x.capitalize())
                            dictDetailProfilKaryawan[f'{k}'][5] = Pendidikaninput
                            dictProfilKaryawan[f'{k}'][4] = Pendidikaninput
                        elif response == 'Alamat Domisili':
                            AlamatDomisiliinput = pypi.inputStr(
                            prompt='Silahkan masukkan alamat domisili karyawan: ', 
                            applyFunc=lambda x: x.capitalize())
                            dictDetailProfilKaryawan[f'{k}'][7] = AlamatDomisiliinput
                        elif response == 'Penghargaan':
                            Penghargaan = pypi.inputStr(
                            prompt='Silahkan masukkan penghargaan karyawan: ', 
                            applyFunc=lambda x: x.title())
                            dictDetailProfilKaryawan[f'{k}'][10] += (f', {Penghargaan}')
                        elif response == 'Update keseluruhan data karyawan' :
                            input1()
                            # berarti nama itu di keys berapa sama index berapa
                        break
                print(f'Data tersebut berhasil diubah silahkan cek dimenu tampilkan data')
                update()
            elif i == len(dictDetailProfilKaryawan) -1:
                print('Maaf nama karyawan tidak tersedia')
                update()

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
        'column' : ["PN", "Nama Karyawan","TTL", "Jabatan", "Gender", "Pendidikan", "Asal Kota", "Alamat Domisili", "Tanggal Masuk", "Tanggal Pensiun", "Penghargaan"],
        '1' : ["141", "John Petrucci","14 Mei 1970", "CEO", "Male", "Doctor", "Jakarta", "Sleman, Yogyakarta", "22 Des 1996", "1 Juni 2026", "Best CEO 2021"],
        '2' : ["129", "John Lennon","17 Des 1974", "CE", "Male", "Master", "Jakarta", "Sleman, Yogyakarta", "1 April 2000", "1 Jan 2031", "Best Marketing 2016"],
        '3' : ["183", "Gugun Blues","29 Juli 1976" , "Secretary", "Male", "Bachelor", "Solo", "Bantul, Yogyakarta", "19 Sep 2002", "1 Agustus 2030", "-"],
        '4' : ["137", "Dewa Budjana","2 Feb 1975", "HRD", "Male", "Master", "Bali", "Gunung, Yogyakarta", "20 Mei 2000", "1 Maret 2031", "-"],
        '5' : ["194", "Eros Candra","22 Maret 1979" , "Marketing", "Male", "Bachelor", "Yogyakarta", "Sleman, Yogyakarta", "5 Okt 2003", "1 April 2034", "2019 Best Marketing, 2022 Best Marketing"],
    }
    #deklarasi print format di menu
    printFormat = "{:<4}" + "{:<15}" * (len(dictProfilKaryawan['column']))
    main()

