from tenant_communication import TenantCommunication
from rent_splitting import RentSplitting


class RentPaymentSystem:
    def __init__(self, landlord_email, num_tenants):
        self.landlord_email = landlord_email
        self.num_tenants = num_tenants

    def process_rent_payment(self, total_rent):
        """
        Process rent payment for the property.

        Args:
        - total_rent (float): Total rent amount for the property.
        """
        # Step 1: Split rent among tenants
        rent_splitting = RentSplitting(self.num_tenants)
        rent_per_tenant = rent_splitting.split_rent(total_rent)

        if rent_per_tenant is not None:
            # Step 2: Communicate rent details to tenants
            tenant_communication = TenantCommunication(self.landlord_email)
            for i in range(1, self.num_tenants + 1):
                tenant_email = f"tenant{i}@example.com"  # Example tenant email
                message_content = f"Dear Tenant {i}, your rent for this month is ${rent_per_tenant}."
                tenant_communication.send_message(tenant_email, message_content)
            print("Rent details communicated to tenants successfully!")
        else:
            print("Failed to process rent payment.")


# Example usage
if __name__ == "__main__":
    # Configuration parameters
    landlord_email = "landlord@example.com"
    num_tenants = 4
    total_rent = 2000.0

    # Initialize RentPaymentSystem object
    rent_payment_system = RentPaymentSystem(landlord_email, num_tenants)

    # Process rent payment
    rent_payment_system.process_rent_payment(total_rent)
