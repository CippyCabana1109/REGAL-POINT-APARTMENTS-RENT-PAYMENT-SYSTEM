class TenantCommunication:
    def __init__(self, landlord_email):
        self.landlord_email = landlord_email

    def send_message(self, tenant_email, message):
        """
        Send a message from a tenant to the landlord.

        Args:
        - tenant_email (str): Email address of the tenant sending the message.
        - message (str): Content of the message.

        Returns:
        - bool: True if the message is successfully sent, False otherwise.
        """
        # Assuming implementation of email sending functionality
        try:
            # Send email to landlord
            print(f"Message from {tenant_email} sent to landlord ({self.landlord_email}):")
            print(message)
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Initialize TenantCommunication object with landlord's email
    tenant_communication = TenantCommunication("landlord@example.com")

    # Example message from tenant
    tenant_email = "tenant@example.com"
    message_content = "Hi, I wanted to inquire about scheduling a maintenance request for my apartment."

    # Send message
    if tenant_communication.send_message(tenant_email, message_content):
        print("Message sent successfully!")
    else:
        print("Failed to send message.")
