# 📧 Disparador de E-mails Automático + Coletor de E-mails

Este repositório contém três scripts em Python que automatizam o processo de envio de currículos e coleta de e-mails a partir de websites.

---

## 💡 Descrição

Este projeto é composto por três arquivos:

### 1️⃣ `disparoEmailsCurriculos.py`

Um script que realiza o envio automático de e-mails com currículo anexado usando **SMTP**. Ideal para quem quer automatizar o envio massivo de currículos diretamente pela conta do Gmail.

**Principais funcionalidades:**
- Conexão segura via `smtplib.SMTP_SSL`.
- Carrega uma lista de destinatários a partir de um arquivo `.xlsx`.
- Anexa um currículo em PDF ao e-mail.
- Mensagem personalizável.
- Delay inteligente para evitar bloqueios.
- Reconexão automática ao servidor em caso de queda.

---

### 2️⃣ `disparoEmailsCurriculoManual.py`

Script que automatiza o envio de e-mails simulando a interação humana usando **PyAutoGUI** e **keyboard**. Indicado para casos onde o servidor SMTP não é uma opção e o envio é feito manualmente pelo navegador.

**Principais funcionalidades:**
- Simulação de cliques e digitação para preencher campos de e-mail.
- Uso de coordenadas de tela para clique nos botões (ajustável).
- Anexa currículo em PDF e preenche assunto/corpo do e-mail automaticamente.
- Cria backup da planilha de emails antes de iniciar o processo.
- Remove da planilha os e-mails já enviados, evitando duplicidade.

---

### 3️⃣ `pegarEmailSite.py`

Script feito pelo meu amigo **Wil**. Ele busca e coleta e-mails diretamente de páginas web usando **requests** e **BeautifulSoup**.

**Principais funcionalidades:**
- Extrai e-mails válidos de qualquer site.
- Gera automaticamente uma planilha `.xlsx` com os resultados.
- Simples, leve e eficaz para montar listas de e-mails.

---

## ⚙️ Requisitos

Antes de rodar os scripts, instale as dependências:

```bash
pip install pandas openpyxl beautifulsoup4 requests pyautogui keyboard
```

---

## 🚨 Aviso Importante
- **Uso consciente:** O envio massivo de e-mails pode ser considerado spam. Use essas ferramentas com ética e respeito.
- Configure suas credenciais com cuidado e **nunca compartilhe sua senha de e-mail**.
- O script manual (`disparoEmailsCurriculoManual.py`) depende de coordenadas de tela, ajuste conforme seu monitor.

---

## 📂 Organização dos Arquivos

```
📦disparo-de-emails
 ┣ 📂disparo
 ┃ ┣ 📂Anexo
 ┃ ┃ ┗ seu_curriculo.pdf
 ┃ ┣ 📂Planilha
 ┃ ┃ ┗ emails.xlsx
 ┣ disparoEmailsCurriculos.py
 ┣ disparoEmailsCurriculoManual.py
 ┣ pegarEmailSite.py
 ┗ README.md
```

---

## 🤝 Créditos

- Scripts de envio (`disparoEmailsCurriculos.py` e `disparoEmailsCurriculoManual.py`) adaptados por **Mateus**.
- Script de coleta (`pegarEmailSite.py`) criado por **Wilgne**.
