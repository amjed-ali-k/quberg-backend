# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail(fullname, phonenumber, course, email, **kwargs):
    body = f'<strong>{fullname} Booked for {course}!. </strong><br /> Email: {email}<br /> Contact Number: {phonenumber}<br />Full Name: {fullname}<br />Course: {course}'
    message = Mail(
        from_email='contact@fdg-capital.com',
        to_emails='katesinclair91@gmail.com',
        subject=f'{fullname} Booked for {course}!',
        html_content=body)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
