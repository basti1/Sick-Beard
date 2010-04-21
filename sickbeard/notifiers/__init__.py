import sickbeard

import xbmc
import growl
import mail

from sickbeard.common import * 


def testGrowl(host, password):
    growl.sendGrowl("Test Growl", "Testing Growl settings from Sick Beard", "Test", host, password)

def testXBMC(host, username, password):
    xbmc.notifyXBMC("Testing XBMC notifications from Sick Beard", "Test Notification", host, username, password)
	
def testMail(server, user, password, sender, receiver):
    mail._send("Email notification test", server, user, password, sender, receiver)

def notify(type, message):
    
    if type == NOTIFY_DOWNLOAD and sickbeard.XBMC_NOTIFY_ONDOWNLOAD == True:
            xbmc.notifyXBMC(message, notifyStrings[type])
        
    if type == NOTIFY_SNATCH and sickbeard.XBMC_NOTIFY_ONSNATCH:
            xbmc.notifyXBMC(message, notifyStrings[type])

    growl.sendGrowl(notifyStrings[type], message)
