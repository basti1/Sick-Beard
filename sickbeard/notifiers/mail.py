import smtplib
import sickbeard
from sickbeard import logger

from email.mime.text import MIMEText

def sendEmailNotification(message):
	server = sickbeard.SMTP_SERVER
	user = sickbeard.SMTP_USER
	password = sickbeard.SMTP_PASSWORD
	sender = sickbeard.SMTP_SENDER
	receiver = sickbeard.SMTP_RECEIVER
	
	logger.log("Sending email notification to " + receiver)
	 
	_send(message,server,user,password,sender,receiver)

def _send(message,server,user,password,sender,receiver):
    msg = """From: %s
To: %s
Subject: Sick-Beard notification
   
%s
""" % (sender, receiver, message)
	
    try:
        s = smtplib.SMTP(server)
        s.login(user,password)
        s.sendmail(sender, receiver, msg())
        s.quit()
        logger.log("Email notification sent to "+receiver)
    except Exception, e:
        logger.log("Warning: Couldn't send email notification",Exception,e)


