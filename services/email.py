# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config
from services.db.configDB import get_config_from_db


async def send_mail(fullname, phonenumber, course, email, **kwargs):
    body = f'<strong>{fullname} Booked for {course}!. </strong><br /> Email: {email}<br /> Contact Number: {phonenumber}<br />Full Name: {fullname}<br />Course: {course}'
    to_email = await get_config_from_db('admin_email')
    message = Mail(
        from_email='contact@fdg-capital.com',
        to_emails= to_email,
        subject=f'{fullname} Booked for {course}!',
        html_content=body)
    try:
        sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:  
        print(e)
