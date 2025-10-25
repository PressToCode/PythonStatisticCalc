import re

# Pisah & Verifikasi
def verifyInput(daftar_angka):
    # input_terpisah adalah setiap angka (tanpa spasi) dalam daftar angka yang telah dipisah
    # berdasarkan koma JIKA angka tersebut setelah dihilangkan spasi bukan berisi kosong
    input_terpisah = [angka.replace(' ', '') for angka in daftar_angka.split(',') if angka.replace(' ', '') != '' ]
    print(input_terpisah)

    # Cek jika input terdapat bukan angka integer atau float
    for angka in input_terpisah:
        print(angka)
        if not re.fullmatch(r'^-?(\d+(\.\d*)?|\.\d+)$', angka):
            return False, None

    return True, [float(angka) for angka in input_terpisah]

def rerata(float_list):
    return str(sum(float_list) / len(float_list))

def maksimum(float_list):
    return str(max(float_list))

def minimum(float_list):
    return str(min(float_list))

def jumlahAngka(float_list):
    return str(len(float_list))

def angkaGanjilGenap(float_list):
    genap_count = 0
    ganjil_count = 0

    for angka in float_list:
        # Check if the number is an integer (no fractional part)
        if angka.is_integer():
            if int(angka) % 2 == 0:
                genap_count += 1
            else:
                ganjil_count += 1

    return genap_count, ganjil_count

# Main
if __name__ == '__main__':
    while True:
        daftar_angka = input('Masukkan daftar angka (pisahkan dengan koma): ')

        verified, float_list = verifyInput(daftar_angka)
        if verified:
            break

    # Perhitungan
    print("Rata-rata: " + rerata(float_list))
    print("Maximum: " + maksimum(float_list))
    print("Minimum: " + minimum(float_list))
    print("Jumlah-angka: " + jumlahAngka(float_list))

    genap_count, ganjil_count = angkaGanjilGenap(float_list)
    print("Angka Genap: " + genap_count)
    print("Angka Ganjil: " + ganjil_count)