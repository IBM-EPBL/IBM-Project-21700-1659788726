import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient('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')
from_email = Email("arumaa07@gmail.com")  
to_email = To("charanms394@gmail.com")  
subject = "Testing SendGrid mail service"
content = Content("text/plain", "Hi there, this email is a part of Nalaiya Thiran Project testing from the team PNT2022TMID19786")
mail = Mail(from_email, to_email, subject, content)

mail_json = mail.get()

response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)