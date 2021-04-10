
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



import smtplib, email, ssl

#create structure of the mail

def emailing(subject, emitter, recipient, contenu, alternative):
    msg = MIMEMultipart
    msg['Subject'] = (subject)
    msg['From'] = (emitter)
    msg['To'] = (recipient)

    html = MIMEText(alternative, "html")
    plaintext = MIMEText(conenu, "plain")

    msg.attach(html)
    msg.attach(plaintext)


    with open("roasted-asparagus.jpg", 'rb') as img:
        msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                         cid=asparagus_cid)

    # Make a local copy of what we are going to send.
    with open('outgoing.msg', 'wb') as f:
        f.write(bytes(msg))

    # Send the message via local SMTP server.
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)