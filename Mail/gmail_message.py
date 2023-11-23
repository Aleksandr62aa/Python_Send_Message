# https://www.geeksforgeeks.org/how-to-send-automated-email-messages-in-python/
# WSL2
# export EMAIL_PASSWORD='gkifsmsujmdrvaua'
# echo $EMAIL_PASSWORD

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  

def send_gmail(message):
    # sender = "sender_email"
    sender = "62aa.aleksandr@gmail.com"
     
    # recipient = "recipient_email"
    recipient = "62a.aleksandr@gmail.com"   
        
    # your password = "your password"
    password = "gkifsmsujmdrvaua"
    # password = os.getenv("EMAIL_PASSWORD")
        
    # built the message content html
    msg = MIMEMultipart() 
    text = f"<h1> ALARM! </h1> <b> {message} </b> "    
    html = '<html><head></head><body><p>' + text + '</p></body></html>'
    part_text = MIMEText( text, 'plain')
    part_html = MIMEText(html, 'html')
   
    msg['Subject'] = "ALARM"
    # msg.attach(MIMEText(message))
    msg.attach(part_text)
    msg.attach(part_html)  

    try:
        # set up a connection to our email server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()        
        server.login(sender, password)        
        trecipients = [sender, recipient] 
        server.sendmail(sender,  to_addrs=trecipients, msg=msg.as_string())
        server.quit()
        return "The message OK!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

def main():
    # message = input('Type your message: ')
    message = "People on object"
    print(send_gmail(message))    

if __name__ == "__main__":
    main()