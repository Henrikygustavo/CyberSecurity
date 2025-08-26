# Projeto de Criptografia (AES + RSA)

Este projeto implementa dois algoritmos de criptografia:

- **Simétrica (AES - via Fernet)**
- **Assimétrica (RSA - via OAEP e SHA-256)**

## 🚀 Como executar

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/crypto-project.git
cd crypto-project
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Executar exemplos

AES (simétrica)
```bash
python symmetric.py
```
RSA (assimétrica)
```bash
python asymmetric.py
```

📖 Explicação

AES utiliza a mesma chave para criptografar e descriptografar.

RSA utiliza um par de chaves: pública (para cifrar) e privada (para decifrar).

🛠 Tecnologias

<ul>
  <li>[Python 3](https://docs.python.org/3)</li>
  <li> Biblioteca [cryptography](https://cryptography.io/en/latest>) </li>
</ul>
