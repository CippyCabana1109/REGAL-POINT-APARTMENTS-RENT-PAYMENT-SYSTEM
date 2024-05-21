import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    @staticmethod
    def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, username, password):
        """
        Send an email.

        Args:
        - sender_email (str): Sender's email address.
        - receiver_email (str): Receiver's email address.
        - subject (str): Email subject.
        - body (str): Email body.
        - smtp_server (str): SMTP server address.
        - smtp_port (int): SMTP server port.
        - username (str): Username for SMTP authentication.
        - password (str): Password for SMTP authentication.

        Returns:
        - bool: True if the email is sent successfully, False otherwise.
        """
        try:
            # Create a MIMEText object to represent the email
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Establish a connection to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(username, password)

            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())

            # Close the connection
            server.quit()

            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

    # Other utility functions can be added here as needed
