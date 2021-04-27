while True:
    nama_siswa = input ("masukan nama anda : ")
    nilai_harian = float (input("masukan nilai :"))
    nilai_uts = float (input("masukan nilai uts :"))
    nilai_uas = float (input("masukan nilai uas :"))
    nilai_akhir = float (((nilai_harian*40)/100)+((nilai_uts*30)/100)+((nilai_uas*30)/100))

    if nilai_akhir >=80:
        predikat_nilai= 'Amat_baik'
        print("nama lengkap anda = ", nama_siswa)
        print("nilai akhir anda = ", nilai_akhir)
        print("predikat anda = ", predikat_nilai)

    elif nilai_akhir>=70:
        predikat_nilai= 'Baik'
        print("nama lengkap anda = ", nama_siswa)
        print("nilai akhir anda = ", nilai_akhir)
        print("predikat anda = ", predikat_nilai)

    elif nilai_akhir>=60:
        predikat_nilai= 'Cukup'
        print("nama lengkap anda = ", nama_siswa)
        print("nilai akhir anda = ", nilai_akhir)
        print("predikat anda = ", predikat_nilai)

    elif nilai_akhir>=50:
        predikat_nilai= 'Kurang'
        print("nama lengkap anda = ", nama_siswa)
        print("nilai akhir anda = ", nilai_akhir)
        print("predikat anda = ", predikat_nilai)

    else:
        predikat_nilai= 'Kurang_sekali'
        print("nama lengkap anda =  ", nama_siswa)
        print("nilai akhir anda =", nilai_akhir)
        print("predikat anda = ", predikat_nilai)