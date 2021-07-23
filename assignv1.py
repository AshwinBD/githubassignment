import csv, smtplib
from email.message import EmailMessage
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ashwindhakade1531@gmail.com', 'Ashwin1234')
message = 'Hi, Lorem ipsum dolor sit amet'
sender = 'ashwindhakade1531@gmail.com'
with open("csvfile.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for Email in reader:
        email = EmailMessage()
        email['From'] = sender
        email['To'] = Email
        server.set_content(message)
        server.send_message(email)
        print(f' sent to {email}')
server.close()


