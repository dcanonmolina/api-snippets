# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest.monitor import TwilioMonitorClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3094732a3c49700934481addd5ce1659"
auth_token = "{{ auth_token }}"
client = TwilioMonitorClient(account_sid, auth_token)

event = client.events.get("AE21f24380625e4aa4abec76e39b14458d")
print event.description
