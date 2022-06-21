"""_summary_
_Descreption_: Email Sender with Python (Practice application)
_URL_:
_Compatibility_: Python 3.x
_Version_: 0.1.0
_Author by_: Peter Mutter <mutter.peter@protonmail.com>
_Created by_: 2022-03-30
"""

#Használt modulok:
import os
import myMailEnvVar #Saját fájl importáció.
import smtplib
import imghdr #képfájlok email csatolmányaihoz
from email.message import EmailMessage

class GmailSmtp:
 
 #Email fiók környezeti változók beállítása:
 #myMailEnvVar.setGmailEnvVars()
 #__GMAIL_ADDRESS = os.environ.get('EMAIL_USER')
 #__GMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
 #__g_msg = EmailMessage()
 #__g_msg['Subject'] = ''
 #__g_msg['From'] = ''
 #__g_msg['To'] = []
 #__g_msg.set_content(content)

 #Konstruktor
 #def __init__(self, smtp_url: str = 'smtp.gmail.com', ssl_port: int = 465, tls_port: int = 587):
 def __init__(self):
      self.__smtp_gmail_url: str = 'smtp.gmail.com'
      self.__SSL_PORT: int = 465
      self.__TLS_PORT: int = 587
      self.__GMAIL_ADDRESS = os.environ['EMAIL_USER'] = 'mutterptr@gmail.com'
      self.__GMAIL_PASSWORD = os.environ['EMAIL_PASS'] = 'Tmxnpc359Samba'
      #self.vmi = 'faszomat'
 
 #'GmailSmtp' Osztály getter/setter property -ik: 
 @property
 def GMAIL_ADDRESS(self):
     return self.__GMAIL_ADDRESS

 @GMAIL_ADDRESS.setter
 def GMAIL_ADDRESS(self, email_addr):
     self.__GMAIL_ADDRESS = email_addr

 @property
 def GMAIL_PASSWORD(self):
     return self.__GMAIL_PASSWORD
 
 @GMAIL_PASSWORD.setter
 def GMAIL_PASSWORD(self, email_passwd):
     self.__GMAIL_PASSWORD = email_passwd

 @property
 def smtp_url(self):
     return self.__smtp_gmail_url

 @smtp_url.setter
 def smtp_url(self, smtp_url):
     self.__smtp_gmail_url = smtp_url

 @property
 def SSL_PORT(self):
     return self.__SSL_PORT

 @SSL_PORT.setter
 def SSL_PORT(self, port):
     self.__SSL_PORT = port
 
 @property
 def TLS_PORT(self):
     return self.__TLS_PORT

 @TLS_PORT.setter
 def TLS_PORT(self, port):
     self.__TLS_PORT = port     

 def Sending(self, sender: str, subject: str, recipient: str, ImgAttacher):
  msg = EmailMessage()
  #msg['From'] = 'mutterptr@gmail.com'
  #msg['Subject'] = 'TESZT!!!'
  #msg['To'] = 'mupetike@gmail.com'
  msg['From'] = sender
  msg['Subject'] = subject
  msg['To'] = recipient
  msg.set_content('TESZT SZÖVEG!')
  #email_attachment = self.emailAttacher('attachment', '19.pdf')
  
      
  msg.add_attachment(file_data, maintype=main_type, subtype=file_type, filename=file_name)
  
  with smtplib.SMTP_SSL(self.__smtp_gmail_url, self.__SSL_PORT) as smtp:
   smtp.login(self.__GMAIL_ADDRESS, self.__GMAIL_PASSWORD)
   smtp.send_message(msg)
 
 def __str__(self):
     return str(self.__GMAIL_ADDRESS)  
 #'GmailSmtp' osztály Setter metódusa(i):
 
 def emailAttacher(self, subfolder: str, filename: str):
  dirname = os.path.dirname(__file__)
  source = os.path.join(dirname,subfolder,filename)
  print(source)
  with open(source, 'rb') as f:
      file_data = f.read()
      file_name = filename
      if file_name.endswith('.pdf'):
          print('PDF a Fájl!')
          file_type = 'octet-stream'
      else:
          file_type = imghdr.what(f.name)

      print(file_type)     
      return [file_data, file_type, file_name];

 #Csak a Képfájlokat beolvasó metódus:
 def ImgAttacher(self, folder: str, images: list):
   base_path = os.path.dirname(__file__)
   if folder == '':
      folder = 'attachment'
   if images != None and images != []:  
      img_files = os.path.join(base_path, folder, images)
   #jpeg/jpg/png képfájlok beolvasása kontextussal:
      for img in img_files:
        with open(img, 'rb') as f:
          file_data = f.read()
          file_type = imghdr.what(f.name)
          file_name = f.name
    #if file_type == 'jpeg' or 'png':
      img_maintype = 'image'
   else:
       images = []  
   return [file_data, file_type, file_name, img_maintype];

 #Csak a pdf fájlokat beolvasó metódus:
 def PdfAttacher(self, folder: str, files: list):
   base_path = os.path.dirname(__file__)
   if folder == '':
      folder = 'attachment'
   if files != None and files != []:  
      files = os.path.join(base_path, folder, files)
   #jpeg/jpg/png képfájlok beolvasása kontextussal:
      for file in files:
        with open(file, 'rb') as f:
          file_data = f.read()
          file_name = f.name
          if file_name.endswith('.pdf'):
             file_type = 'octet-stream'
             pdf_maintype = 'application'
          else:
           files = []  
   return [file_data, file_type, file_name, pdf_maintype];   


"""
 #NEM LESZ JÓ! NEM LEHET ÁLTALÁNOS BEOLVASÓ METÓDUS ERRE SZERINTEM
 #AZ MACERÁS LENNE, HOGY VEGYES LEHESSEN A MELLÉKLET FÁJLOK TÍPUSAI A BEÉPÍTETT 'msg.add_attachment' metódus működése miatt
 #Általános, fájlokat beolvasó metódus (képek és pdf-ek):
 def Attachment(self, folder: str, files: list):
  base_path = os.path.dirname(__file__)
  attachment_files = os.path.join(base_path, folder, files)
  #a fájlok beolvasása kontextussal:
  for file in attachment_files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        if imghdr.what(f.name) == 'jpeg' or 'png' or 'gif':
"""



"""
 def set_gmail_Subject(self, subject):
     self.g_msg['Subject'] = str(subject)

 def set_gmail_Sender(self, sender_mail_address): 
     self.g_msg['From'] = str(sender_mail_address)
 
 def set_gmail_Recipients(self, recipients):
     #static_recipients = ['mupetike@gmail.com', 'mupetya@yahoo.co.uk']
     contacts = []
     for c in recipients:
      contacts = c
     self.g_msg['To'] = ', '.join(recipients)
"""

gmail = GmailSmtp()
print(gmail)
print(gmail.GMAIL_ADDRESS)
#gmail.Sending('mutterptr@gmail.com', 'TESZT2 !!!', 'mupetike@gmail.com')
gmail.emailAttacher('attachment', '19.pdf')
#Sending metódus: Email-Feladója, Email-Tárgya, Email-Címzett(jei) 
gmail.Sending('mutterptr@gmail.com', 'TESZT12 !!!', 'mupetike@gmail.com', ImgAttacher)

class YmailSmtp:

#osztályváltozók:
 smtp_yahoo_url = 'smtp.mail.yahoo.com'
 SSL_PORT = 465
 TLS_PORT = 587
 #Email fiók környezeti változók beállítása:
 myMailEnvVar.setYmailEnvVars()
 YMAIL_ADDRESS = os.environ.get('EMAIL_USER')
 YMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
 y_msg = EmailMessage()

 #'YmailSmtp' Osztály Getter metódusai:
 def get_ymail_Address(self):
     return self.YMAIL_ADDRESS

 def get_ymail_Password(self):
     return self.YMAIL_PASSWORD

 def get_ymail_Smtp_URL(self):
     return self.smtp_yahoo_url

 def get_ymail_SSL_Port(self):
     return self.SSL_PORT

 def get_ymail_TLS_Port(self):
     return self.TLS_PORT

 #'YmailSmtp' osztály Setter metódusa(i):
 def set_ymail_Smtp_URL(self, smtp_url):        
     self.smtp_yahoo_url = smtp_url



"""
GMAIL_ADDRESS = os.environ.get('EMAIL_USER')
GMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
print(GMAIL_ADDRESS)
print(GMAIL_PASSWORD)
"""


#--Email Account tesztelése--
#print(GmailSmtp.GMAIL_ADDRESS)
#print(GmailSmtp.GMAIL_PASSWORD)
#exit()


"""
#TLS:
with smtplib.SMTP(GmailSmtp.smtp_gmail_url, GmailSmtp.TLS_PORT) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.ehlo
  smtp.login(GmailSmtp.GMAIL_ADDRESS, GmailSmtp.GMAIL_PASSWORD)
#EMAIL:    
  subject = 'Teszt email Python-bol TLS!'
  body = 'Teszt szoveg...'
  msg = f'Subject: {subject}\n\n{body}'
#Küldő metódus:    
 #smtp.sendmail(Feladó, Címzett, email)
  smtp.sendmail(GmailSmtp.GMAIL_ADDRESS, 'mupetike@gmail.com', msg)
"""

"""
#SSL:
with smtplib.SMTP_SSL(GmailSmtp.smtp_gmail_url, GmailSmtp.SSL_PORT) as smtp:
 smtp.login(GmailSmtp.GMAIL_ADDRESS, GmailSmtp.GMAIL_PASSWORD)
#EMAIL:    
 subject = 'Teszt email Python-bol SSL!'
 body = 'Teszt szoveg...'
 msg = f'Subject: {subject}\n\n{body}'
#Küldő metódus:    
#smtp.sendmail(Feladó, Címzett, email)
 smtp.sendmail(GmailSmtp.GMAIL_ADDRESS, 'mupetike@gmail.com', msg)
"""

