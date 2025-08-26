from cryptography.fernet import Fernet

# Gerar chave simétrica
def gerar_chave():
    return Fernet.generate_key()

# Criptografar
def cifrar_texto(chave, texto):
    f = Fernet(chave)
    return f.encrypt(texto.encode())

# Descriptografar
def decifrar_texto(chave, texto_cifrado):
    f = Fernet(chave)
    return f.decrypt(texto_cifrado).decode()

if __name__ == "__main__":
    chave = gerar_chave()
    print("Chave simétrica:", chave.decode())

    texto = "Dinossauro em AES!"
    print("Texto original:", texto)

    cifrado = cifrar_texto(chave, texto)
    print("Texto cifrado:", cifrado)

    decifrado = decifrar_texto(chave, cifrado)
    print("Texto decifrado:", decifrado)
