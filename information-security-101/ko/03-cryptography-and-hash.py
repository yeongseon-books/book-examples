from common import PasswordHasher, SymmetricCipher

hasher = PasswordHasher()
encoded = hasher.hash_password_scrypt("password123")
cipher = SymmetricCipher(b"demo-secret-key-32bytes-value!!!!")
token = cipher.encrypt(b"hello")
print(
    {
        "verify": hasher.verify("password123", encoded),
        "roundtrip": cipher.decrypt(token).decode(),
    }
)
