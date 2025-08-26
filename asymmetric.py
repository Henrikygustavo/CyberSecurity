from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Gerar chaves RSA
def gerar_chaves():
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    chave_publica = chave_privada.public_key()
    return chave_privada, chave_publica

# Cifrar com chave pública
def cifrar_texto(chave_publica, texto):
    return chave_publica.encrypt(
        texto.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Decifrar com chave privada
def decifrar_texto(chave_privada, texto_cifrado):
    return chave_privada.decrypt(
        texto_cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()

if __name__ == "__main__":
    priv, pub = gerar_chaves()

    texto = "Dinossauro em RSA!"
    print("Texto original:", texto)

    cifrado = cifrar_texto(pub, texto)
    print("Texto cifrado:", cifrado)

    decifrado = decifrar_texto(priv, cifrado)
    print("Texto decifrado:", decifrado)
