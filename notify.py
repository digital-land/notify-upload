import os
import logging
from notifications_python_client import prepare_upload
from notifications_python_client.notifications import NotificationsAPIClient

notifications_client = NotificationsAPIClient(os.getenv("NOTIFY_API_KEY"))
template_id = os.getenv("NOTIFY_TEMPLATE_ID")

def send(file, email):
    response = notifications_client.send_email_notification(
        email_address=email, # required string
        template_id=template_id, # required UUID string
        personalisation={'link_to_file': prepare_upload(file)}
    )
    logging.info("done sending email notification")
