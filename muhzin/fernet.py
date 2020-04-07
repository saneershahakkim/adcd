from cryptography.fernet import Fernet, MultiFernet


key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f = MultiFernet([key1, key2])
token = f.encrypt(b"Secret message!")
dec1 = f.decrypt(token)
print("first decrypted = ",dec1,"and it is encrypted as   ",token)


key3 = Fernet(Fernet.generate_key())
f2 = MultiFernet([key3, key1, key2])
rotated = f2.rotate(token)
dec2 = f2.decrypt(rotated)
print("secondly decrypted = ",dec2,"and it is encrypted as",rotated)



