class LatePaymentHandler:
    def _init_(self):
        self.late_penalty = 50  # Example late payment penalty amount

    def assess_late_fee(self, days_late):
        # Placeholder for assessing late fee based on number of days late
        late_fee = self.late_penalty * days_late
        return late_fee

    def send_reminder(self, tenant_email):
        # Placeholder for sending late payment reminder to tenant
        print("Sending late payment reminder to:", tenant_email)

# Example usage:
if _name_ == "_main_":
    late_handler = LatePaymentHandler()

    days_late = int(input("Enter number of days late: "))
    late_fee = late_handler.assess_late_fee(days_late)
    print("Late fee assessed:", late_fee)

    tenant_email = input("Enter tenant email address: ")
    late_handler.send_reminder(tenant_email)