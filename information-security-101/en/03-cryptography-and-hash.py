from common import PasswordHasher, SymmetricCipher

hasher = PasswordHasher()
encoded = hasher.hash_password_pbkdf2("password123")
cipher = SymmetricCipher(b"demo-secret-key-32bytes-value!!!!")
token = cipher.encrypt(b"security")
print(
    {
        "verify": hasher.verify("password123", encoded),
        "roundtrip": cipher.decrypt(token).decode(),
    }
)
