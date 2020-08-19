import rsa
public_key, private_key = rsa.newkeys(2048)
print (str(public_key))