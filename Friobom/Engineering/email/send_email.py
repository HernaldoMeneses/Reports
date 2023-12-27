import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Configurações do servidor SMTP
smtp_host = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'hernaldomeneses@gmail.com'
smtp_password = 'wnti zbve qxgt tqnl'

# Configurações do e-mail
from_address = 'hernaldomeneses@gmail.com'
to_address = 'ramon.praticasalgados@gmail.com'
cc_addresses = ['linebylineline@gmail.com', 'hernaldomeneses@gmail.com']  # Adicione seus destinatários CC aqui
bcc_addresses = ['']  # Adicione seus destinatários BCC aqui
subject = 'AssuntoTotal'
body_email = "Matrix Total Hello The Matrix Has you by H.Meneses"
# Criar a mensagem do e-mail
message = MIMEMultipart()
message['From'] = from_address
message['To'] = to_address
message['CC'] = ', '.join(cc_addresses)  # Adicione os destinatários CC à lista

message['Subject'] = subject

# Adicionar corpo do e-mail (opcional)
body = body_email
message.attach(MIMEText(body, 'plain'))

# Anexar a planilha ao e-mail
path = 'L:\\Friobom\\Engineering\\data\\excel_files\\'
name = '322_17_3809_d_Venda_Superv_RCA.xlsx'
filename = path + name

with open(filename, 'rb') as file:
    attachment = MIMEApplication(file.read(), Name=name)

attachment['Content-Disposition'] = f'attachment; filename={filename}'
message.attach(attachment)


# Adicionar destinatários BCC à lista
message['BCC'] = ', '.join(bcc_addresses)

# Conectar-se ao servidor SMTP e enviar o e-mail
with smtplib.SMTP(smtp_host, smtp_port) as server:
    server.starttls()  # Use esta linha se estiver usando TLS
    server.login(smtp_user, smtp_password)
    server.send_message(message)

print("E-mail enviado com sucesso!")