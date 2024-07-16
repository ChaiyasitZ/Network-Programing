import smtplib

message = """From: From Joe <joe@blow.com>
To: To New <newz@ubuntu.org>
MINE-VERSION: 1.0
Content-Type: text/html
Subject: SMTP e-mail test

This is a test e-mail message.

<b>This is a test html Message.</b>
<h1>This is headling 1</h1>
"""

try:
    smtp = smtplib.SMTP("192.168.188.134")
    smtp.sendmail("newz@ubuntu.org", "newz@ubuntu.org", message)
    print("Successfully sent email")
    
except Exception as err:
    print(str(err))
    
    