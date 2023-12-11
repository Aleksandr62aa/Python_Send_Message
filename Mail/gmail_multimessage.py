# https://www.geeksforgeeks.org/how-to-send-automated-email-messages-in-python/

import smtplib
import hydra
from omegaconf import DictConfig, OmegaConf
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_gmail(cfg, image,  message=None, file=None, video=None, video_path= None):
    # sender = "sender_email"
    sender = cfg.sender
    # recipient = "recipient_email"
    recipient = cfg.recipient
    # your password = "your password"
    password = cfg.password 
    # password = os.getenv("EMAIL_PASSWORD")
    
    # Initializing MIMEMultipart content
    msg = MIMEMultipart()
    msg['Subject'] = "ALARM"
    # msg.attach(MIMEText(message))
    # msg.attach(part_text)

    # 1.Attaching message
    text = f"<h1> ALARM! </h1> <b> {message} </b> "    
    html = '<html><head></head><body><p>' + text + '</p></body></html>'
    # part_text = MIMEText( text, 'plain')
    part_html = MIMEText(html, 'html')
    # Attach message to the MIMEMultipart object
    msg.attach(part_html) 

    # 2.Attaching Video on YouTube
    body = video_path
    # Attach video_path to the MIMEMultipart object
    msg.attach(MIMEText(body)) 

    try:
        # 3.Attaching image
        # Importing image
        with  open(image, 'rb') as img_data:
            # Attach image to the MIMEMultipart object
            image_path = os.path.basename(image)
            msg.attach(MIMEImage(img_data.read(), name=image_path))                       
        
        # 4.Attaching file        
        # Importing file
        with open(file, "rb") as file_data:
            # Initializing file object
            file_obj = MIMEBase('application', 'octet-stream')
            file_obj.set_payload(file_data.read())            
            # Encoding file for attaching to the email
            encoders.encode_base64(file_obj)
            file_path = os.path.basename(file)
            file_obj.add_header('Content-Disposition', 'attachment; filename={}'.format(file_path))
            # Attach file to the MIMEMultipart object
            msg.attach(file_obj)        

        # 5.Attaching video        
        # Importing video file
        with open(video, "rb") as video_data:
            # Initializing video object
            video_obj = MIMEBase('application', 'octet-stream')
            video_obj.set_payload(video_data.read())            
            # Encoding video for attaching to the email
            encoders.encode_base64(video_obj)
            video_path = os.path.basename(video)
            video_obj.add_header('Content-Disposition', 'attachment; filename={}'.format(video_path))
            # Attach video to the MIMEMultipart object
            msg.attach(video_obj)
        
        # set up a connection to our email server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()            
        server.login(sender, password)
        trecipients = [sender, recipient] 
        server.sendmail(sender, to_addrs=trecipients, msg=msg.as_string())
        server.quit()
        return "The message+image+file+video+YouTube OK!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

@hydra.main(config_name="config")
def my_main(cfg: DictConfig):
    # message = input('Type your message: ')
    message = "People on object"
    image = r'D:\CV\IMAGE\Track.jpg'
    file = r'D:\CV\result.xlsx'
    video_path = "Video on YouTube: https://www.youtube.com/watch?v=ZvAGL0EDLVY&list=RDCMUCrWWcscvUWaqdQJLQQGO6BA&start_radio=1"    
    video = r'D:\CV\IMAGE\demo.mp4'
    print(send_gmail(cfg, image, message, file, video, video_path))    

if __name__ == "__main__":
    my_main()   