import csv
import os
from pathlib import Path
from datetime import datetime as tanggal


def createHeader(judul):
    with open('dataLaundry.csv', 'w', newline='') as filecsv:
        tulis = csv.DictWriter(filecsv, fieldnames=judul,  delimiter=',')
        tulis.writeheader()


def addData():
    os.system('cls')
    with open('dataLaundry.csv', 'a', newline='') as file:
        csvTambah = csv.writer(file)
        print('='*31)
        print("="*9, 'Tambah Data', '='*9)
        print('='*31)
        nama = input('Masukkan nama anda : ')
        print("==== Kategori ====")
        print(
            "[1] Reguler (5 hari) \n[2] Express (2 hari)")
        kategori = int(input("Masukkan angka kategori : "))
        # os.system('cls')
        if kategori == 1:
            kategori = 'reguler'
            print("==== Nama Barang ====")
            print("[1] Pakaian(2k/kg) \n[2] Karpet(3k/kg) \n[3] Gorden (4k/kg)")
            barang = int(input("Masukkan angka barang : "))
            berat = int(input('masukkan berat (kg) : '))
            if barang == 1:
                barang = 'pakaian'
                harga = berat * 2000
            elif barang == 2:
                barang = 'karpet'
                harga = berat * 3000
            elif barang == 3:
                barang = 'gorden'
                harga = berat * 4000
            tgl = tanggal.now()
            tgl_masuk = (str(tgl.day) + '/' +
                         str(tgl.month) + '/' + str(tgl.year))
            kl = tgl.day
            kle = kl+5
            tgl_keluar = (str(kle)+'/'+str(tgl.month)+'/'+str(tgl.year))
        elif kategori == 2:
            kategori = 'express'
            print("==== Nama Barang ====")
            print("[1] Pakaian(5k/kg) \n[2] Karpet(6k/kg) \n[3] Gorden(7k/kg)")
            barang = int(input("Masukkan angka barang : "))
            berat = int(input('masukkan berat (kg) : '))
            if barang == 1:
                barang = 'pakaian'
                harga = berat * 5000
            elif barang == 2:
                barang = 'karpet'
                harga = berat * 6000
            elif barang == 3:
                barang = 'gorden'
                harga = berat * 7000
            tgl = tanggal.now()
            tgl_masuk = (str(tgl.day) + '/' +
                         str(tgl.month) + '/' + str(tgl.year))
            kl = tgl.day
            kle = kl+2
            tgl_keluar = (str(kle)+'/'+str(tgl.month)+'/'+str(tgl.year))

        csvTambah.writerow(
            [nama, kategori, barang, berat, tgl_masuk, tgl_keluar, harga])
        file.close()
        os.system('cls  ')
        print("Data Berhasil Diinput!!! \n")
        print('\n===================================',
              "\nnama               : ", nama,
              "\nkategori           : ", kategori,
              '\nbarang             : ', barang,
              '\ntanggal masuk      : ', tgl_masuk,
              '\ntanggal diambil    :', tgl_keluar,
              '\n===================================\n'
              '\nTotal Harga        : Rp', harga, '\n\n===================================')
        input("\n\nenter untuk lanjutkan")
        os.system('cls')
        tampilMenu()


def editData():
    tampilData()
    print("-"*103)
    
    tampilMenu()


def deleteData():
    tampilData()
    print("-"*103)

    hps = int(input("hapus nomor : "))
    rows = []
    with open("dataLaundry.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
    indeks = 0
    for data in range(len(rows)):
        if data == hps:
            rows.remove(rows[indeks])
        indeks += 1
    judul = rows.pop(0)
    with open("dataLaundry.csv", "w", newline="") as file:
        tulis = csv.DictWriter(file, fieldnames=judul)
        tulis.writeheader()
        for data in rows:
            tulis.writerow({'Nama': data[0], 'Kategori': data[1], 'Barang': data[2], 'berat': data[3],
                            'tgl_masuk': data[4], 'tgl_ambil': data[5], 'total': data[6]})
    print("Data berhasil dihapus !!!\n")
    input("Enter Untuk Kembali !!")
    tampilMenu()


def tampilData():
    os.system('cls')
    rows = []
    with open("dataLaundry.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
    judul = rows.pop(0)
    judul.insert(0, 'No')
    no = 1
    print('='*103)
    print('='*40, 'Seluruh Data Laundry', '='*41)
    print('='*103)
    print(
        f"{judul[0]}\t {judul[1]} \t\t {judul[2]} \t {judul[3]} \t {judul[4]}\t {judul[5]} \t{judul[6]}\t{judul[7]}")
    print('-'*103)
    for i in rows:
        print(
            f"{no}\t{i[0]} \t\t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {i[5]} \t {i[6]}")
        no += 1
    file.close()


def getData():
    tampilData()
    print('='*103)
    input("Enter Untuk Kembali!!")
    os.system('cls')
    tampilMenu()


def tampilMenu():
    os.system('cls')
    print('='*39)
    print("===== APLIKASI PENCATATAN LAUNDRY =====")
    print('='*39)
    print('-'*13, 'Daftar Menu', '-'*13)
    print('[1] Tampil data \n[2] Tambah data \n[3] Ubah data \n[4] Hapus data \n[5] Keluar')
    print('='*39)
    menu = int(input("Masukkan nomor menu : "))
    if menu == 1:
        getData()
    elif menu == 2:
        if not(Path('dataLaundry.csv').is_file()):
            createHeader(["Nama", "Kategori", "Barang", "berat",
                         'tgl_masuk', 'tgl_ambil', 'total'])
        addData()
    elif menu == 3:
        editData()
    elif menu == 4:
        deleteData()
    else:
        tampilMenu()


if __name__ == "__main__":
    tampilMenu()
