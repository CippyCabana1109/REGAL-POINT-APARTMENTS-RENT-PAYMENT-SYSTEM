class RentSplitting:
    def __init__(self, num_tenants):
        self.num_tenants = num_tenants

    def split_rent(self, total_rent):
        """
        Split the total rent amount among the tenants.

        Args:
        - total_rent (float): Total rent amount for the property.

        Returns:
        - float: Amount of rent to be paid by each tenant.
        """
        try:
            if self.num_tenants > 0:
                rent_per_tenant = total_rent / self.num_tenants
                return rent_per_tenant
            else:
                raise ValueError("Number of tenants must be greater than zero.")
        except Exception as e:
            print(f"Error splitting rent: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize RentSplitting object with the number of tenants
    num_tenants = 4
    rent_splitting = RentSplitting(num_tenants)

    # Example total rent amount for the property
    total_rent = 2000.0

    # Split the rent among tenants
    rent_per_tenant = rent_splitting.split_rent(total_rent)

    # Display the rent amount per tenant
    if rent_per_tenant is not None:
        print(f"Rent amount per tenant: ${rent_per_tenant}")
    else:
        print("Failed to split rent.")
