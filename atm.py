import getpass

class ATM:
    def pilih_menu():
        saldo = 10000000
        print("="*45)
        print("\t\tATM BERSAMA")
        print("\tJl.S Parman No.14 Balikpapan Tengah")
        print("\t\tTelp.0542-48215")
        print("=============== MENU PILIHAN ================")
        print("[1] Informasi Saldo")
        print("[2] Bayar")
        print("[3] Transfer")
        print("[4] Ambil Uang")
        print("[5] Keluar")
        print("="*45)
        pilih = int(input("Masukkan Menu Pilihan [1/2/3/4/5]: "))
        
        if(pilih == 1):
            n = 1
            while(n == 1):
                print("Menu: INFORMASI SALDO")
                print("Informasi Rekening Tabungan")
                print("Informasi Giro")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                   ATM.pilih_menu()
                   continue
        elif(pilih == 2):
             n = 1
             while(n == 1):
                print("Menu: BAYAR")
                print("[1] BPJS\t[3] PDAM")
                print("[2] PLN\t\t[4] PULSA PASCABAYAR")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    ATM.pilih_menu()
                    continue
        elif(pilih == 3):
             n = 1
             while(n == 1):
                print("Menu: TRANSFER")
                print("[1] Transfer Antar Bank")
                print("[2] Transfer Sesama Bank")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    ATM.pilih_menu()
                    continue
        elif(pilih == 4):
             saldo = 300000
             n = 1
             while(n == 1):
                print("Menu: AMBIL UANG")
                print("[1] Rp. 1.000.000,-")
                print("[2] Rp. 500.000,-")
                print("[3] Rp. 300.000,-")
                print("[4] Nominal Lain")
                print("="*45)
                ambil = int(input("Masukkan Nominal Yang Akan Di ambil [1/2/3/4] : "))
                uang1 = 1000000
                uang2 = 500000
                uang3 = 300000
                
                if(ambil == 1):
                    saldo = saldo - uang1
                    print('Sisa Saldo   : ',saldo)
                    print('Status       : Penarikan Berhasil!')
                    kembali = input("Masukkan Transaksi Baru [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")) :
                        ATM.pilih_menu()
                        continue           
                elif(ambil == 2):
                    saldo = saldo - uang2
                    print('Sisa Saldo   : ',saldo)
                    print('Status       : Penarikan Berhasil!')
                    kembali = input("Masukkan Transaksi Baru [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")) :
                        ATM.pilih_menu()
                        continue
                elif(ambil == 3):
                    saldo = saldo - uang3
                    print('Sisa Saldo   : ',saldo)
                    print('Status       : Penarikan Berhasil!')
                    kembali = input("Masukkan Transaksi Baru [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")) :
                        ATM.pilih_menu()
                        continue
                elif(ambil == 4):
                    uanglain = int(input("Masukkan Nominal Uang Yang Di ambil : Rp."))
                    saldo = saldo - uanglain
                    print('Sisa Saldo   : ',saldo)
                    print('Status       : Penarikan Berhasil!')
                    kembali = input("Masukkan Transaksi Baru [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")) :
                        ATM.pilih_menu()
                        continue
                else :
                    print("Maaf Saldo Anda Tidak Cukup")
                    kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                    if((kembali == "y") or (kembali == "Y")):
                        ATM.pilih_menu()
                        continue
        elif(pilih == 5):
            print("Terima Kasih, Silahkan Ambil Kartu Anda")
            exit()
            
            
    def menu_utama():
            pin = "12345"
            print("="*45)
            print("\t\tATM BERSAMA")
            print("\tJl.S Parman No.14 Balikpapan Tengah")
            print("\t\tTelp.0542-48215")
            print("=============== MENU UTAMA ================")
            for i in range(3) :
                sandi = getpass.getpass("Masukkan PIN Anda\t: ")
                if (sandi == pin):
                    ATM.pilih_menu()
                else :
                    print("PIN Anda Salah!")
                    if i == 2 :
                        print("Anda Telah Melakukan 3x Percobaan")
                        print("Kartu ATM Terblokir")
                        exit()
ATM.menu_utama()          
            
