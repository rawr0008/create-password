import secrets
import string

def perkuat_password(password: str, panjang: int = 24) -> str:
    karakter = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?/|~"

    pw_list = list(password)
    while len(pw_list) < panjang:
        pw_list.append(secrets.choice(karakter))

    secrets.SystemRandom().shuffle(pw_list)
    return ''.join(pw_list[:panjang])


def buat_password_random(panjang: int = 32) -> str:
    if panjang < 16:
        raise ValueError("Panjang minimal password adalah 16")

    karakter = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?/|~"

    pw_list = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+[]{};:,.<>?/|~")
    ]

    pw_list += [secrets.choice(karakter) for _ in range(panjang - 4)]
    secrets.SystemRandom().shuffle(pw_list)
    return ''.join(pw_list)


if __name__ == "__main__":
    print("Password Generator")
    print("1. Perkuat password buatan sendiri")
    print("2. Buat password random")

    pilih = input("Pilih menu (1/2): ").strip()

    if pilih == "1":
        pw = input("Masukkan password: ")
        panjang = int(input("Panjang password baru (contoh 24): "))
        hasil = perkuat_password(pw, panjang)
        print("\nPassword hasil penguatan:", hasil)

    elif pilih == "2":
        panjang = int(input("Panjang password (minimal 16): "))
        jumlah = int(input("Jumlah password yang dibuat: "))
        print("\nDaftar password:\n")
        for i in range(jumlah):
            print(f"{i+1}. {buat_password_random(panjang)}")

    else:
        print("Pilihan tidak valid.")
