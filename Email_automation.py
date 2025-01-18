import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define email parameters
gmail_user = 'your_email@gmail.com'
gmail_password = 'your_app_password'
recipient = 'recipient_email@example.com'
subject = 'Automated Email'
body = 'This is an automated email sent using Python'

# Create a message
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = recipient
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Set up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)

# Send the email
text = msg.as_string()
server.sendmail(gmail_user, recipient, text)
server.quit()

print('Email sent successfully!')