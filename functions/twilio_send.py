import os
from twilio.rest import Client
from dotenv import load_dotenv
import random
import logging
twilio_logger = logging.getLogger('twilio.http_client')
twilio_logger.setLevel(logging.WARNING)

def create_OTP():
    otp = ''
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp

def twilio_send(phoneNumber):
    load_dotenv()

    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)
    otp = create_OTP()
    message = client.messages \
      .create(
        body='Your OTP is ' + otp,
        from_='+18666967406',
        to='+1'+ phoneNumber
      )
    userOTP = input('Enter OTP: ')
    if str(userOTP) == str(otp):
        return True
    else:
        return False
   

    

