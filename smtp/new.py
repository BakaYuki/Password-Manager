import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server credentials
smtp_server = 'smtp-mail.outlook.com'
smtp_server = 'outlook.office365.com'
smtp_port = 587  # Port for TLS connection

sender_email = 'mukeshpzpt@outlook.com'
sender_password = 'JayNepal'

recipient_email = 'mukeshpr443@gmail.com'

# Create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Password Reset Code'

# Add body to the email
body = 'This is your password reset code:'
message.attach(MIMEText(body, 'plain'))

# Establish a connection to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Upgrade the connection to secure TLS

# Log in to the SMTP server
server.login(sender_email, sender_password)

# Send the email
server.send_message(message)

# Quit the SMTP session
server.quit()
