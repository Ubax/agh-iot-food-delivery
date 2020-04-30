import rsa

(pub, priv) = rsa.newkeys(512)

with open("pub.txt", "wb") as file:
    file.truncate()
    file.write(pub.save_pkcs1())

with open("priv.txt", "wb") as file:
    file.truncate()
    file.write(priv.save_pkcs1())