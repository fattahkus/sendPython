# Import smtplib to provide email functions
import smtplib

# Import the email modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define email addresses to use
addr_to   = 'fattah.kusuma@hotmail.com'
addr_from = "Apple"

# Define SMTP email server details
smtp_server = 'smtp.gmail.com'
smtp_user   = 'Applelm9y0xljl353_deaktivierteskonto0@dekativerenkonbestellunto.services'
smtp_pass   = '@@Kontol123'

# Construct email
msg = MIMEMultipart('alternative')
msg['Bcc'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Test Email From RPi'

# Create the body of the message (a plain-text and an HTML version).
text = "This is a test message.\nText and html."
html = """\
<html>
  <head></head>
  <body>
    <p>This is a test message.</p>
    <p>Text and HTML</p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via an SMTP server
s = smtplib.SMTP(smtp_server,587)
s.login(smtp_user,smtp_pass)
s.sendmail(addr_from, addr_to, msg.as_string())
s.quit()