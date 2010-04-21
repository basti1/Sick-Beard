import smtplib
import sickbeard
from sickbeard import logger

from email.mime.text import MIMEText

def sendEmailNotification(filename):
	server = sickbeard.SMTP_SERVER
	user = sickbeard.SMTP_USER
	password = sickbeard.SMTP_PASSWORD
	sender = sickbeard.SMTP_SENDER
	receiver = sickbeard.SMTP_RECEIVER
	
	message = "Just downloaded " + filename
	
	logger.log("Sending email notification for " + filename)
	 
	_send(message,server,user,password,sender,receiver)

def _send(message,server,user,password,sender,receiver):
    msg = MIMEText("")

    msg['Subject'] = 'SickBeard email notification'
    msg['From'] = sender
    msg['To'] = receiver
    msg['Body'] = '%s', message
	
    try:
        s = smtplib.SMTP(server)
        s.login(user,password)
        s.sendmail(sender, [receiver], msg.as_string())
        s.quit()
    except:
        logger.log("Warning: Couldn't send email notification")


