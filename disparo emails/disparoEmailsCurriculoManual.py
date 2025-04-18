# -*- coding: utf-8 -*-
import pandas as pd
from time import sleep
import pyautogui as py
import keyboard
import os
from pathlib import Path

# Configurações
py.PAUSE = 0.5
ARQUIVO_EMAILS = r"disparo\Planilha\emails.xlsx"
ARQUIVO_CURRICULO = r"disparo\Anexo\.pdf"
BACKUP_PATH = str(Path(ARQUIVO_EMAILS).with_name('BACKUP_' + Path(ARQUIVO_EMAILS).name))

# Coordenadas (ajuste conforme sua tela)
COORD = {
    'escrever': (78, 179),
    'para': (1321, 482),
    'assunto': (1287, 524),
    'corpo': (1303, 589),
    'enviar_anexo': (1428, 1003),
    'anexo_pdf': (337, 160),
    'abrir_anexo': (1539, 509),
    'enviar': (1298, 1001)
}

# Textos fixos
ASSUNTO = " - titulo - "
CORPO_EMAIL = """ - Corpo do texto do email - """

def enviar_email(destinatario):
    try:
        py.click(COORD['escrever'])
        sleep(1.5)
        
        py.click(COORD['para'])
        for letra in destinatario:
            keyboard.write(letra)
            sleep(0.08)
        sleep(1)
        py.press('enter')
        sleep(1.5)
        
        py.click(1303, 589)
        sleep(0.1)

        py.click(COORD['assunto'])
        for letra in ASSUNTO:
            keyboard.write(letra)
            sleep(0.08)
        sleep(1)
        
        py.click(COORD['corpo'])
        sleep(0.5)
        for linha in CORPO_EMAIL.split('\n'):
            for letra in linha:
                keyboard.write(letra)
                sleep(0.1)
            py.press('enter')
            sleep(0.2)
        sleep(1)
        
        py.click(COORD['enviar_anexo'])
        sleep(0.2)
        py.click(COORD['anexo_pdf'])
        sleep(1.5)
        py.press('enter')
        sleep(1)
        py.click(COORD['abrir_anexo'])
        sleep(1.5)
        
        py.click(COORD['enviar'])
        sleep(1.5)
        py.click(122,1066) # Ver onde vai
        sleep(1.5)
        return True
        
    except Exception as e:
        print(f"Erro ao enviar: {str(e)}")
        return False

def main():
    # Criar backup
    if not os.path.exists(BACKUP_PATH):
        import shutil
        shutil.copy2(ARQUIVO_EMAILS, BACKUP_PATH)
        print(f"Backup criado: {BACKUP_PATH}")
    
    df = pd.read_excel(ARQUIVO_EMAILS)
    email_column = [col for col in df.columns if 'email' in col.lower()][0]
    emails = df[email_column].dropna().str.strip().tolist()
    
    print(f"\nTotal de emails: {len(emails)}")
    print("Posicione o mouse no canto da tela para abortar")
    print("Iniciando em 5 segundos...")
    sleep(5)
    
    c = 0
    for email in emails:
        try:
            c += 1
            print(f"\n{c} - Enviando para: {email}")
            
            if enviar_email(email):
                # Remove o email enviado
                df = df[df[email_column].str.strip() != email.strip()]
                df.to_excel(ARQUIVO_EMAILS, index=False)
                print("✓ Email enviado e removido da lista")
            
            # Pausas estratégicas
            if c % 10 == 0:
                sleep(15)  # Pausa maior a cada 10 emails
            elif c >= 25:
                sleep(25)
                if c == 50:
                    print('\n50 disparos realizados!')
                    break
            else:
                sleep(6)
                
        except Exception as e:
            print(f"Erro grave: {str(e)}")
            sleep(30)
    
    # Atualizar arquivo se parou antes do final
    if c > 0:
        df.to_excel(ARQUIVO_EMAILS, index=False)
        print(f"\nProcesso concluído. Total enviados: {c}")

if __name__ == "__main__":
    print("=== DISPARADOR DE EMAILS ===")
    main()