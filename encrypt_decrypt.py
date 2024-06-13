def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    return encrypt(text, -shift)

# Baca file asli
with open('plaintext.txt', 'r') as file:
    plaintext = file.read()

# Enkripsi dengan shift 3
shift = 3
ciphertext = encrypt(plaintext, shift)

# Simpan hasil enkripsi ke file baru
with open('ciphertext.txt', 'w') as file:
    file.write(ciphertext)

# Untuk dekripsi (opsional, untuk verifikasi)
decrypted_text = decrypt(ciphertext, shift)

# Simpan hasil dekripsi ke file baru (opsional)
with open('decrypted_text.txt', 'w') as file:
    file.write(decrypted_text)
