import smtplib
import hydra
from omegaconf import DictConfig, OmegaConf
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  

def send_gmail(cfg, message):
    # sender = "sender_email"
    sender = cfg.sender
     
    # recipient = "recipient_email"
    recipient = cfg.recipient 
        
    # your password = "your password"
    password = cfg.password
    # password = os.getenv("EMAIL_PASSWORD")
        
    # built the message content html
    msg = MIMEMultipart()    
    text = f"<h1> ALARM! </h1> <b> {message} </b> "    
    html = '<html><head></head><body><p>' + text + '</p></body></html>'
    # part_text = MIMEText( text, 'plain')
    part_html = MIMEText(html, 'html')
   
    msg['Subject'] = "ALARM"
    # msg.attach(MIMEText(message))
    # msg.attach(part_text)
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

@hydra.main(config_name="config")
def main(cfg: DictConfig):
    # message = input('Type your message: ')
    message = "People on object"
    print(send_gmail(cfg, message))    

if __name__ == "__main__":
    main()