from cryptography.fernet import Fernet, MultiFernet


#key1 = Fernet.generate_key()
#key2 = Fernet.generate_key()
#key3 = Fernet.generate_key()
nbr = int(input("\n\n which key do you want to Encrypt : \n\t 1:Key1 \n\t 2:Key2 \n\t 3:Key3\n\n"))
if nbr == 1:
    #f = MultiFernet([key1, key2, key3])
    key1 = Fernet.generate_key()
    f = Fernet(key1)
    tt = input("Enter the Message : ")
    t = bytes(tt, 'utf-8')
    token = f.encrypt(t)
    dec1 = f.decrypt(token)
    print("\n\n\t\t..............Message encripted succesfully.........")
    print("Message encryped as : ",token,"\n\nThe Key1 is : ",key1 ,"and\n Decrypted as :",dec1)
elif nbr == 2 :
    #f = MultiFernet([key2, key3, key1])
    key2 = Fernet.generate_key()
    f = Fernet(key2)
    tt = input("Enter the Message : ")
    t = bytes(tt, 'utf-8')
    token = f.encrypt(t)
    dec1 = f.decrypt(token)
    print("\n\n\t\t..............Message encripted succesfully.........")
    print("Message encryped as : ", token, "\n\nThe Key2 is : ", key2, "and\n Decrypted as :", dec1)
elif nbr == 3:
    #f = MultiFernet([key3, key2, key1])
    key3 = Fernet.generate_key()
    f = Fernet(key3)
    tt = input("Enter the Message : ")
    t = bytes(tt, 'utf-8')
    token = f.encrypt(t)
    dec1 = f.decrypt(token)
    print("\n\n\t\t..............Message encripted succesfully.........")
    print("Message encryped as : ", token, "\n\nThe Key3 is : ", key3, "and\n Decrypted as :", dec1)
else:
    print("Invalid character !!!!!!")


"""f = MultiFernet([key1, key2], key3)
    tt = input("Enter the Message : ")
    t = bytes(tt, 'utf-8')
    token = f.encrypt(t)
    dec1 = f.decrypt(token)
    print("\n\n\t\t..............Message encripted succesfully.........")
    print("Message encryped as : ",token,"\n\nThe Key1 is : ",key1 ,"and\n Decrypted as :",dec1)"""
