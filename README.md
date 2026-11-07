# 🛡️ Desafio Prático DIO: Simulação de Cibersegurança (Ransomware & Keylogger)

Repositório criado para fins educacionais e de pesquisa no âmbito do laboratório prático de cibersegurança da DIO, focando no entendimento de táticas de atores maliciosos, análise comportamental e implementação de contramedidas defensivas.

---

## 📂 Estrutura do Repositório

```text
├── desafio_keylogger/     # Scripts de captura de teclas e exfiltração via SMTP
└── desafio_ransomware/    # Scripts de criptografia simétrica (Fernet) e recuperação

🛡️ Reflexão sobre Defesa e Mitigação

A realização deste laboratório reforça a importância de uma estratégia de Defesa em Profundidade, englobando:

    Soluções EDR e Antivírus: Monitoramento de comportamento anómalo e blocagem de hooks globais de teclado ou criptografia em massa.

    Filtragem de Saída (Egress Filtering): Controlo de tráfego de rede para evitar exfiltração de dados por portas SMTP não autorizadas.

    Princípio do Menor Privilégio: Limitação de permissões de utilizador no sistema operativo.

    Políticas de Backup Rigorosas: Cópias de segurança offline e imutáveis para mitigação de ransomware.

    Conscientização do Utilizador: Formação contínua contra engenharia social e phishing.
