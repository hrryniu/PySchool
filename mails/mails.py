import smtplib
import time
import schedule
import openpyxl
import tkinter as tk
from tkinter import filedialog, messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from threading import Thread
import json
import os

# Ścieżka do pliku konfiguracyjnego
CONFIG_FILE = "config.json"


# Funkcja do zapisu danych konfiguracyjnych (np. e-mail nadawcy)
def save_config(email):
    config_data = {
        "sender_email": email
    }
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config_data, config_file)


# Funkcja do załadowania danych konfiguracyjnych (jeśli istnieją)
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            return json.load(config_file)
    return None


# Funkcja do załadowania danych z pliku Excel
def load_data_from_excel(file_name):
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active
    email_data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):  # Zaczynamy od drugiego wiersza (pomijamy nagłówki)
        email, language, company, message_pl, message_en, message_fr = row
        if email and language and company:
            email_data.append((email, language, company, message_pl, message_en, message_fr))

    return email_data


# Funkcja do wysłania e-maila
def send_email(receiver_email, language, company, message_pl, message_en, message_fr, attachment_path, sender_email,
               password):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Automatyczna wiadomość"

    # Wybór wiadomości na podstawie języka i dynamiczne wstawienie nazwy firmy
    if language == 'pl':
        body = message_pl.replace("{firma}", company)
    elif language == 'en':
        body = message_en.replace("{firma}", company)
    elif language == 'fr':
        body = message_fr.replace("{firma}", company)
    else:
        body = "Hello! This is an automatic email."

    msg.attach(MIMEText(body, 'plain'))

    # Załącznik
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
            msg.attach(part)

    # Połączenie z serwerem SMTP i wysyłka e-maila
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"E-mail wysłany do {receiver_email}")
    except Exception as e:
        print(f"Nie udało się wysłać e-maila do {receiver_email}. Błąd: {e}")
    finally:
        server.quit()


# Funkcja do zaplanowania wysyłki e-maili
def schedule_emails(email_data, attachment_path, interval_seconds, sender_email, password):
    for email, language, company, message_pl, message_en, message_fr in email_data:
        schedule.every(interval_seconds).seconds.do(send_email, receiver_email=email, language=language,
                                                    company=company, message_pl=message_pl, message_en=message_en,
                                                    message_fr=message_fr, attachment_path=attachment_path,
                                                    sender_email=sender_email, password=password)

    while True:
        schedule.run_pending()
        time.sleep(1)


# Funkcja wywoływana po kliknięciu "Wyślij"
def send_mails():
    sender_email = email_entry.get()
    password = password_entry.get()
    interval_seconds = int(interval_entry.get())

    if not excel_file_path or not sender_email or not password:
        messagebox.showwarning("Błąd", "Uzupełnij wszystkie pola!")
        return

    # Zapisanie adresu e-mail do pliku konfiguracyjnego
    save_config(sender_email)

    email_data = load_data_from_excel(excel_file_path)

    # Tworzenie nowego wątku, aby aplikacja GUI nie zamarzała podczas wysyłania e-maili
    t = Thread(target=schedule_emails, args=(email_data, attachment_path, interval_seconds, sender_email, password))
    t.start()


# Funkcja do wyboru pliku Excel
def choose_excel_file():
    global excel_file_path
    excel_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

    if excel_file_path:
        email_data = load_data_from_excel(excel_file_path)
        num_emails = len(email_data)
        excel_label.config(text=f"{excel_file_path} (Liczba e-maili: {num_emails})")


# Funkcja do wyboru załącznika
def choose_attachment():
    global attachment_path
    attachment_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    attachment_label.config(text=attachment_path)


# Funkcja do wyświetlenia okna z instrukcją
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Instrukcja")
    help_text = """
    Instrukcja formatowania pliku Excel:

    1. Plik musi być w formacie .xlsx.
    2. Pierwszy wiersz (nagłówek) musi zawierać następujące kolumny:
       - Kolumna 1: Adres e-mail (np. email@example.com)
       - Kolumna 2: Język wiadomości (np. pl, en, fr)
       - Kolumna 3: Nazwa firmy
       - Kolumna 4: Wiadomość w języku polskim
       - Kolumna 5: Wiadomość w języku angielskim
       - Kolumna 6: Wiadomość w języku francuskim
    3. W treści wiadomości możesz użyć placeholdera {firma}, który zostanie zastąpiony nazwą firmy odbiorcy.

    Przykład:
    -------------------------
    | email@example.com | pl  | Firma XYZ  | Witaj {firma}, to jest wiadomość po polsku | Hello {firma}, this is a message in Polish | Bonjour {firma}, ceci est un message en polonais |
    -------------------------
    """
    tk.Label(help_window, text=help_text, justify="left").pack(padx=10, pady=10)


# Tworzenie okna aplikacji
root = tk.Tk()
root.title("Automatyczne wysyłanie e-maili")

# Inicjalizacja zmiennych globalnych
excel_file_path = ""
attachment_path = ""

# Etykiety i pola dla użytkownika
tk.Label(root, text="Adres e-mail nadawcy:").grid(row=0, column=0)
email_entry = tk.Entry(root, width=50)
email_entry.grid(row=0, column=1)

tk.Label(root, text="Plik Excel z e-mailami:").grid(row=1, column=0)
excel_btn = tk.Button(root, text="Wybierz plik", command=choose_excel_file)
excel_btn.grid(row=1, column=1)
excel_label = tk.Label(root, text="")
excel_label.grid(row=1, column=2)

tk.Label(root, text="Załącznik:").grid(row=2, column=0)
attachment_btn = tk.Button(root, text="Wybierz plik", command=choose_attachment)
attachment_btn.grid(row=2, column=1)
attachment_label = tk.Label(root, text="")
attachment_label.grid(row=2, column=2)

tk.Label(root, text="Odstęp czasowy (s):").grid(row=3, column=0)
interval_entry = tk.Entry(root, width=10)
interval_entry.grid(row=3, column=1)

tk.Label(root, text="Hasło:").grid(row=4, column=0)
password_entry = tk.Entry(root, show="*", width=50)
password_entry.grid(row=4, column=1)

# Przycisk "Wyślij"
send_btn = tk.Button(root, text="Wyślij", command=send_mails)
send_btn.grid(row=5, column=1)

# Dodanie przycisku "Help"
help_btn = tk.Button(root, text="Help", command=show_help)
help_btn.grid(row=6, column=1)

# Załadowanie adresu e-mail przy starcie aplikacji (jeśli istnieje plik konfiguracyjny)
config = load_config()
if config:
    email_entry.insert(0, config.get("sender_email", ""))

# Uruchomienie aplikacji
root.mainloop()
