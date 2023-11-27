import smtplib
import hydra
from omegaconf import DictConfig, OmegaConf
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart  


def send_gmail(cfg, image, message=""):
    # sender = "sender_email"
    sender = cfg.sender
     
    # recipient = "recipient_email"
    recipient = cfg.recipient
        
    # your password = "your password"
    password = cfg.password 
    # password = os.getenv("EMAIL_PASSWORD")
    
    # built the message content
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
        # Attaching Images
        img_data = open(image, 'rb') 
        msg.attach(MIMEImage(img_data.read(),  
                    name=os.path.basename(image)))
        img_data.close()
        # set up a connection to our email server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()            
        server.login(sender, password)
        trecipients = [sender, recipient] 
        server.sendmail(sender, to_addrs=trecipients, msg=msg.as_string())
        server.quit()
        return "The message+image OK!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

@hydra.main(config_name="config")
def main(cfg: DictConfig):
    # message = input('Type your message: ')
    message = "People on object"
    image = 'D:\CV\IMAGE\Track.jpg'
    print(send_gmail(cfg, image, message))    

if __name__ == "__main__":
    main()   