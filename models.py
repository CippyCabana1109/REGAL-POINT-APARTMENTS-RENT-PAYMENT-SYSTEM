class Tenant:
    def __init__(self, tenant_id, name, email, phone):
        self.tenant_id = tenant_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} (ID: {self.tenant_id})"


class Lease:
    def __init__(self, lease_id, property_name, unit_number, tenant, start_date, end_date, rent_amount):
        self.lease_id = lease_id
        self.property_name = property_name
        self.unit_number = unit_number
        self.tenant = tenant
        self.start_date = start_date
        self.end_date = end_date
        self.rent_amount = rent_amount

    def __str__(self):
        return f"Lease ID: {self.lease_id}, Property: {self.property_name}, Unit: {self.unit_number}, Tenant: {self.tenant}, Rent Amount: ${self.rent_amount}"


class Property:
    def __init__(self, property_name, address, num_units):
        self.property_name = property_name
        self.address = address
        self.num_units = num_units

    def __str__(self):
        return f"{self.property_name} - {self.address}, Units: {self.num_units}"


class Payment:
    def __init__(self, payment_id, lease_id, amount, payment_date):
        self.payment_id = payment_id
        self.lease_id = lease_id
        self.amount = amount
        self.payment_date = payment_date

    def __str__(self):
        return f"Payment ID: {self.payment_id}, Lease ID: {self.lease_id}, Amount: ${self.amount}, Date: {self.payment_date}"
