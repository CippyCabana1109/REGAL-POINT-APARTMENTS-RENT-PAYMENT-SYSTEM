import unittest
from tenant_communication import TenantCommunication

class TestTenantCommunication(unittest.TestCase):
    def test_send_message(self):
        # Test sending a message to the landlord
        tenant_communication = TenantCommunication("landlord@example.com")
        message_content = "Test message from tenant"
        result = tenant_communication.send_message("tenant@example.com", message_content)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
