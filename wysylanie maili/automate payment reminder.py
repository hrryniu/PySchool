import os
import smtplib
from email.message import  EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT= 465
EMAIL_SERVER = "smtp.gmail.com"


current_dir = Path(__file__).resolve().parent if "__file__" in locals