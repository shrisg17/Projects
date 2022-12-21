import smtplib

# Set up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email@gmail.com", "your_password")

# List of recipient email addresses
recipients = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']

# Email subject and body
subject = "Hello from the email bot"
body = "This is a message from the email bot."

# Send the email to each recipient
for recipient in recipients:
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("your_email@gmail.com", recipient, msg)

# Disconnect from the server
server.quit()
