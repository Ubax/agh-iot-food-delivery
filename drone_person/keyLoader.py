import rsa

def loadPublic():
    keyFile = ""
    with open('pub.txt', mode='rb') as public:
        keyFile = public.read()
    return rsa.PublicKey.load_pkcs1(keyFile)

def loadPrivate():
    keyFile = ""
    with open('priv.txt', mode='rb') as private:
        keyFile = private.read()
    return rsa.PrivateKey.load_pkcs1(keyFile)