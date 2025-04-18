import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import time
import os

def disparar_emails():
    # CONFIGURAÇÕES PRINCIPAIS
    EMAIL_REMETENTE = ""
    SENHA_APP = "uedi dqox xvjq oebf"  # Senha de app gerada
    ARQUIVO_EMAILS = r"disparo\Planilha\emails.xlsx"
    ARQUIVO_CURRICULO = r"C:disparo\Anexo\.pdf"
    nomeCurriculo = ""

    # Verificar se os arquivos existem
    if not os.path.exists(ARQUIVO_EMAILS):
        print(f"Erro: Arquivo de emails não encontrado em {ARQUIVO_EMAILS}")
        return
    if not os.path.exists(ARQUIVO_CURRICULO):
        print(f"Erro: Arquivo do currículo não encontrado em {ARQUIVO_CURRICULO}")
        return

    # CONFIGURAÇÃO DA MENSAGEM
    ASSUNTO = " - titulo - "
    CORPO_EMAIL = """ - Corpo do texto do email - """

    # CONEXÃO COM O SERVIDOR
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_REMETENTE, SENHA_APP)
            print(">> Conexão estabelecida com sucesso!")
            
            # CARREGAR LISTA DE EMAILS
            try:
                df = pd.read_excel(ARQUIVO_EMAILS)
                
                # Verificar se a coluna 'Email' existe (case insensitive)
                email_columns = [col for col in df.columns if 'email' in col.lower()]
                
                if not email_columns:
                    print("Erro: Nenhuma coluna de email encontrada na planilha.")
                    print("Colunas disponíveis:", df.columns.tolist())
                    return
                
                # Usar a primeira coluna que parece ser de email
                email_column = email_columns[0]
                emails = df[email_column].dropna().str.strip().tolist()
                total = len(emails)
                print(f">> {total} emails encontrados para envio")
                
                # PROCESSO DE ENVIO
                for idx, destinatario in enumerate(emails, 1):
                    try:
                        # Verificar se o email é válido
                        if '@' not in destinatario or '.' not in destinatario:
                            print(f"{idx}/{total} - Email inválido: {destinatario}")
                            continue

                        # Testar conexão antes de enviar
                        try:
                            status = server.noop()[0]
                            if status != 250:
                                raise Exception("Conexão perdida, reconectando...")
                        except:
                            print(">> Reconectando ao servidor SMTP...")
                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                            server.login(EMAIL_REMETENTE, SENHA_APP)

                        # PREPARAR MENSAGEM
                        msg = MIMEMultipart()
                        msg['From'] = EMAIL_REMETENTE
                        msg['To'] = destinatario
                        msg['Subject'] = ASSUNTO
                        msg.attach(MIMEText(CORPO_EMAIL, 'plain'))

                        # ANEXAR CURRÍCULO
                        with open(ARQUIVO_CURRICULO, 'rb') as anexo:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(anexo.read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition',
                                            f'attachment; filename="{nomeCurriculo}.pdf"')
                            msg.attach(part)

                        # ENVIAR EMAIL
                        server.send_message(msg)
                        print(f"{idx}/{total} - Enviado para: {destinatario}")

                        # INTERVALO ENTRE ENVIOS
                        if idx < total:
                            time.sleep(15)  # Evitar bloqueio

                    except Exception as e:
                        print(f"{idx}/{total} - Erro ao enviar para {destinatario}: {str(e)}")
                        time.sleep(30)  # Espera maior se houver erro

                
                print("\n>> PROCESSO CONCLUÍDO <<")
                print(f"Total enviados: {idx}/{total}")
                
            except Exception as e:
                print(f">> Erro ao ler arquivo de emails: {str(e)}")
            
    except Exception as e:
        print(f"\n>> ERRO NA CONEXÃO: {str(e)}")
        print("Verifique sua conexão com a internet e as credenciais")

if __name__ == "__main__":
    print("=== DISPARADOR DE CURRÍCULOS ===")
    print("Iniciando processo...\n")
    disparar_emails()