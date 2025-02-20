import smtplib, ssl


n=20
for i in range(n):

    port = 465  
    smtp_server = "smtp.gmail.com"
    sender_email = "SENDER@gmail.com"  
    receiver_email = "RECIEVER@gmail.com" 
    password = input('ENTER YOUR PASSWORD HERE:')
    message = """\
    YOUR MESSAGE """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)