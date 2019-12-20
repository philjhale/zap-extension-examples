#import logging

#logging.debug('***********INSIDE HOOK**********')
headers = dict({"PhilTest": "Added-by-hook"})

def sendingRequest(msg, initiator, helper): 
    #logging.debug('***********REQUEST**********')
    for x in list(headers):
      msg.getRequestHeader().setHeader(x, headers[x])


def responseReceived(msg, initiator, helper): 
    pass

