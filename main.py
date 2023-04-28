import smtplib

# Prompt the user for input
recipient_email = input("Recipient email address: ")
subject = input("Email subject: ")
message = input("Email message: ")

# Email server settings (change these for your own email server)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Email account credentials
sender_email = "@gmail.com"
password = ""

# Connect to the email server and authenticate the user
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, password)

# Compose the email message
email_message = f"Subject: {subject}\n\n{message}"

# Send the email to the specified recipient
server.sendmail(sender_email, recipient_email, email_message)

# Close the connection to the email server
server.quit()

print("Email sent successfully!")
