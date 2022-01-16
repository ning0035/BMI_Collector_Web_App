from email.mime.text import MIMEText
import smtplib

"""
Function for sending email to user
:Package the message with BMI, number of people and average BMI, send email via smtplib
"""
def send_email(email, BMI, average_BMI, count):
    from_email = "xxx@gmail.com"
    from_password = "xxx"
    to_email = email

    subject = "Your Body Maxx Index"
    message = 'Hey there, your BMI is <strong>%s</strong>. Average BMI of all <strong>%s</strong> people is <strong>%s</strong>' % (BMI, count, average_BMI)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)