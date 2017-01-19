import yagmail

def send_email(recipient, subject, body):

    # Intialize yagmail
    yag = yagmail.SMTP('wcc.python', 'montypython932');

    # Send the email
    yag.send(recipient, subject, body)

# Test
recipient = 'nancy.eckenthal@gmail.com' # Update with your email address
subject = 'Testing 123...'
body = 'This is just a test.'
send_email(recipient, subject, body)

print 'Message sent to ' + recipient + '; check your inbox to make sure it arrived.'

