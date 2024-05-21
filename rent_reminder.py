lass RentReminder:
    def _init_(self):
        self.due_days_before = 3  # Example number of days before rent is due to send reminder

    def send_due_rent_reminder(self, tenant_email):
        # Placeholder for sending due rent reminder to tenant
        print("Sending due rent reminder to:", tenant_email)

# Example usage:
if _name_ == "_main_":
    reminder = RentReminder()

    tenant_email = input("Enter tenant email address: ")
    reminder.send_due_rent_reminder(tenant_email)