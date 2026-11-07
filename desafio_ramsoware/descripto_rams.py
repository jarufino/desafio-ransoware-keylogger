import os
from cryptography.fernet import Fernet

# Define o diretório onde o script está guardado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Define a pasta alvo
diretorio_alvo = os.path.join(diretorio_atual, "alvo")


def carregar_chave():
    return open(os.path.join(diretorio_atual, "chave.key"), "rb").read()


def descriptografar_pasta(diretorio):
    if not os.path.exists(diretorio):
        print(f"[-] A pasta '{diretorio}' não foi encontrada.")
        return

    try:
        chave = carregar_chave()
    except FileNotFoundError:
        print(
            "[-] Ficheiro de chave ('chave.key') não encontrado! Impossível descriptografar.")
        return

    f = Fernet(chave)
    contador = 0

    for arquivo in os.listdir(diretorio):
        path = os.path.join(diretorio, arquivo)
        # Pula a chave e o ficheiro de resgate
        if os.path.isfile(path) and arquivo != "chave.key" and arquivo != "LEIA_ISSO.txt":
            with open(path, "rb") as file:
                dados = file.read()

            dados_descriptografados = f.decrypt(dados)

            with open(path, "wb") as file:
                file.write(dados_descriptografados)
            contador += 1

    # Remove a nota de resgate após a descriptografia
    nota_resgate = os.path.join(diretorio, "LEIA_ISSO.txt")
    if os.path.exists(nota_resgate):
        os.remove(nota_resgate)

    print(
        f"[+] Sucesso! {contador} ficheiro(s) descriptografado(s) e restaurados em '{diretorio}'.")


if __name__ == "__main__":
    print(f"[*] A iniciar a descriptografia na pasta: {diretorio_alvo}")
    descriptografar_pasta(diretorio_alvo)
