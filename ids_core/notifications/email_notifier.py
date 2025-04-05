from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email_notification(recipient_email, subject, message, logger=None):
    # Get email credentials from environment variables only
    sender_email = os.environ.get("IDS_EMAIL")
    sender_password = os.environ.get("IDS_PASSWORD")

    # Check if credentials are available
    if not sender_email or not sender_password:
        error_msg = "Email notification failed: Environment variables IDS_EMAIL and/or IDS_PASSWORD not set"
        if logger:
            logger.error(error_msg)
        else:
            print(error_msg)
        return

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        with SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Encrypt the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            
        if logger:
            logger.info("Email notification sent successfully")
        else:
            print("Email sent successfully")
            
    except Exception as e:
        error_msg = f"Failed to send email notification: {e}"
        if logger:
            logger.error(error_msg)
        else:
            print(error_msg)