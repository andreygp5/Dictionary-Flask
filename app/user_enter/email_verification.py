from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import os
import uuid
from dotenv import load_dotenv


path = os.path.dirname(__file__)
dotenv_path = os.path.join(r"C:\Users\andre\Desktop\clone_test\English-Study-Flask\app", '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class SendVerificationCode:

    def __init__(self, reciever):
        self.msg = MIMEMultipart()
        self.code = uuid.uuid4().hex[2:6]
        message = "Your verification code is - " + self.code
        self.password = os.getenv('EMAIL_PASSWORD')
        self.msg['From'] = os.getenv('EMAIL_LOGIN')
        self.msg['To'] = reciever
        self.msg['Subject'] = "English Study Verification"
        self.msg.attach(MIMEText(message, 'plain'))
    
    def send_code(self):
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(self.msg['From'], self.password)
        server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        server.quit()
        return True

    def get_code(self):
        return self.code